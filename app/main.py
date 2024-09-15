from fastapi import FastAPI
from models.datamodels import InputQuestion
from resources import load_config


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_config()










