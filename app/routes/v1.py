from fastapi import APIRouter
import requests
from utils.const import BASE_URL,TAIL_URL
from utils.DB_functions import get_region_ids

app_v1 = APIRouter()


@app_v1.get("/universe/regions")
async def get_universe_regions():
    url = f"{BASE_URL}/universe/regions/{TAIL_URL}"
    region = requests.get(url)
    return region.json()


@app_v1.get("/universe/regions/{region_id}")
async def get_region_detail(region_id: int):
    url = f"{BASE_URL}/universe/regions/{region_id}/{TAIL_URL}"
    region = requests.get(url)
    return region.json()


@app_v1.get("/db/region_ids")
async def get_db_region_ids():
    result = await get_region_ids()
    return result

