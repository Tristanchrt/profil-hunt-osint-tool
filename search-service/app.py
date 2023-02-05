import asyncio
from fastapi import FastAPI, Depends, Request
# from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.search import router as SearchingRoute
from fastapi.middleware.cors import CORSMiddleware
import time
from starlette.concurrency import iterate_in_threadpool
from log import logger
import thundra

# Monitoring
thundra.configure(
    options={
        "config": {
            "thundra.apikey": "880e37c3-1501-4d70-ae4a-324760e9a914",
            # Sample configuration, not required
            "thundra.agent.application.name": "search_service",
        }
    }
)


app = FastAPI()

# token_listener = JWTBearer()

origins = ["http://localhost:4200", "http://ph.local", "http://127.0.0.1"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    await initiate_database()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}    



app.include_router(SearchingRoute, tags=["Searching"], prefix="/search")
