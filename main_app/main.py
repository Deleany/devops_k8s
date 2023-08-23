import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("root_Index.html")


@app.post("/calculate")
async def calculate(val1, val2) -> dict:
    return {
        "result": f"{val1 + val2}"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)
