import os
import requests
from fastapi import FastAPI
app = FastAPI()

__POD_NAME = os.getenv('__POD_NAME')
__POD_IP = os.getenv('__POD_IP')
__PORT_NAME = os.getenv('__PORT_NAME')
__CLUSTER_DNS = "default.svc.cluster.local"

@app.get("/")
async def root():
    return f"Hello from {__name__}.app host: {__POD_NAME} ip: {__POD_IP}"


@app.get("/core")
async def get_from_pod1():
    data = requests.get(f"core-app-svc:{__PORT_NAME}")
    return data.content



