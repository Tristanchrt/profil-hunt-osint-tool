from urllib import request
from fastapi import Body, APIRouter, HTTPException, Request, Depends
from models.common import *
from models.graph import *
import traceback
#from brokerstream import SearchType, Connectors, DtoBk
#from broker.broker import brokerStr
import dataclasses
from services.graph import GraphController
from log import logger

router = APIRouter()

@router.get("/{id}", response_description="get graph by id", response_model=Response)
async def graph_by_id(id: str):
    return response_api(200, "success", "Graph by id_search", await GraphController().find_one(id))

@router.get("/", response_description="get graphs", response_model=Response)
async def get_all_graph():
    return response_api(200, "success", "TEST GRAPH", await GraphController().find_all())

@router.post("/", response_description="creation graph", response_model=Response)
async def creation_graph(data = Body(...)):
    created = await GraphController().create(data)
    if not created:
        raise HTTPException(
            status_code=404,
            detail="Error saving graph"
        )
    return response_api(200, "success", "Graph created", created)

