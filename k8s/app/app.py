import os
import requests
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()

__POD_NAME = os.getenv('__POD_NAME')
__POD_IP = os.getenv('__POD_IP')
__URL_NAME = os.getenv('__PORT_NAME')
__CLUSTER_DNS = "default.svc.cluster.local"



@app.get("/", response_class=PlainTextResponse)
async def get_from_root():
    return f"Hello from {__POD_NAME}"



