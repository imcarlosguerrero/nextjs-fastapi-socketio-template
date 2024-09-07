from fastapi import FastAPI

from api.logger import setup_logger


logger = setup_logger("FastAPI App")

app = FastAPI()

@app.get("/api")
def main():
    logger.info("Hello World")
    return {"Message": "Hello World"}