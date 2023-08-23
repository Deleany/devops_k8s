from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("root_Index.html")


@app.post("/calculate")
async def calculate(val1: int, val2: int) -> dict:
    return {
        "result": f"{val1 + val2}"
    }


if __name__ == "__main__":
    root()
