from fastapi import FastAPI
from routes.v1 import app_v1
from utils.DB_conn import db

app = FastAPI(title="Eve-online API", description="Its a API for Eve project")

app.include_router(app_v1, prefix="/v1")

@app.on_event("startup")
async def db_connect():
    await db.connect()

@app.on_event("shutdown")
async def db_disconnect():
    await db.disconnect()