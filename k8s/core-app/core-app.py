import os
import requests
import kafka
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()

__POD_NAME = os.getenv('__POD_NAME')
__POD_IP = os.getenv('__POD_IP')
__URL_NAME = os.getenv('__PORT_NAME')
__CLUSTER_DNS = "default.svc.cluster.local"


@app.get("/", response_class=PlainTextResponse)
async def get_from_root():
    return f'Hello from {__POD_NAME}'



@app.get("/app", response_class=PlainTextResponse)
async def get_from_app():
    data = requests.get(__URL_NAME)
    return data.content


@app.post("/kafka")
async def write_to(item):
    kafka.write_message(item)

