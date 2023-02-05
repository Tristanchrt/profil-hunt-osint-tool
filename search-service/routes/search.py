from urllib import request
from fastapi import Body, APIRouter, HTTPException, Request, Depends
from models.common import *
from models.search import *
import traceback
from brokerstream import QueueMessageDTO, topics_name
from broker.broker import brokerStr, producer_job
import dataclasses
from middleware.smart_contract import is_search_paid
from log import logger
from services.search import SearchService
import datetime
import json

router = APIRouter()


def object_to_send(search_model):
    return json.dumps({
        "user_id": search_model.user_address,
        "search_id": search_model.id,
        "search_type": "FIRST_LAST_NAME",
        "connectors": "ALL",
        "params": search_model.params,
        "status": search_model.status,
        "data": {}
    }, default=str)

@router.post("/", response_description="job_first_name_last_name", response_model=Response)
async def start_job_first_last_name(data = Body(...), is_auth: bool = Depends(is_search_paid)):
    try:
        created = None
        # if is_auth and is_auth['isValide'] == True:
        #     print('AUTH SUCCESSFUL', is_auth)
        # else:
        #     print('AUTH FAILDED')
        #     raise HTTPException(status_code=403, detail="Request unauthorised : search waiting for the payment")
        
        data['date'] = str(datetime.datetime.now())
        data['is_paid'] = True
        data['link'] = ""
        data['status'] = "PROGRESS"
        params = []
        params.append(data['first_name'])
        params.append(data['last_name'])
        params.extend(data['params'])
        data['params'] = params
        created = await SearchService().create(data)
        if not created:
            raise HTTPException(
                status_code=404,
                detail="Error saving data"
            )
        
        for job in ["c.internal.extractor.facebook","c.internal.extractor.insta","c.internal.extractor.linkedin"]:
            data_dto = object_to_send(created)
            print(job, data_dto)
            brokerStr.send_message(data_dto, job)
            logger.debug('Job send : ', job, data_dto)
        
        return response_api(200, "success", "job started, search created", created)
    except Exception as e:
        logger.debug(traceback.format_exc())        
        raise HTTPException(
            status_code=404,
            detail="Error for start the job"
        )
    

@router.get("/{index_pag}", response_description="get all research", response_model=Response)
async def get_all_research(index_pag, request: Request):
    return response_api(200, "success", "get_all_research", await SearchService().find_all_pag(index_pag))

@router.get("/{id}", response_description="get research by id", response_model=Response)
async def get_one_research(id: str, request: Request):
    return response_api(200, "success", "get_one_research", "fdfdd")

