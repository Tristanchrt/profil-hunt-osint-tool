import asyncio
from fastapi import FastAPI, Depends, Request
# from auth.jwt_bearer import JWTBearer
from config.config import initiate_database_datalake, initiate_database_loaded
from routes.graph import router as GraphRoute
from fastapi.middleware.cors import CORSMiddleware
import time
from starlette.concurrency import iterate_in_threadpool
from log import logger
from broker.consumer import consume_topics
import threading

app = FastAPI()

origins = ["http://localhost:4200", "http://front.ph.local"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response_body = [chunk async for chunk in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    row = f"[DEV] [BODY] {(b''.join(response_body)).decode()} [TIME] {str(process_time)} "
    logger.debug(row)
    return response



@app.on_event("startup")
async def start_database():
    await initiate_database_datalake()
    await initiate_database_loaded()
    t = threading.Thread(target=consume_topics)
    t.start()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Graph service starting..."}    

app.include_router(GraphRoute, tags=["Graph"], prefix="/graph")
