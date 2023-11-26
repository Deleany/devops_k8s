import os
from fastapi import FastAPI
app = FastAPI()

__POD_NAME = os.getenv('__POD_NAME')
__POD_IP = os.getenv('__POD_IP')

@app.get("/")
async def root():
    return f"Hello from {__name__}.app host: {__POD_NAME} ip: {__POD_IP}"


if __name__ == "__main__":
    root()
