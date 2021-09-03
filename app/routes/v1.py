from fastapi import APIRouter, Body
import requests
from utils.const import BASE_URL, TAIL_URL
from utils.DB_functions import get_region_ids, insert_region_data, get_region_constellation_ids, \
    insert_constellation_data, get_constellation_ids
from models.region import Region
from models.constellation import Constellation


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


@app_v1.get("/universe/constellations/{constellation_id}")
async def get_constellation_detail(constellation_id: int):
    url = f"{BASE_URL}/universe/constellations/{constellation_id}/{TAIL_URL}"
    region = requests.get(url)
    return region.json()


@app_v1.get("/db/region_ids")
async def get_db_region_ids():
    result = await get_region_ids()
    return result


@app_v1.get("/db/constellation_ids/{region_id}")
async def get_db_region_constellation_ids(region_id: int):
    result = await get_region_constellation_ids(region_id)
    return result


@app_v1.get("/db/constellation_ids")
async def get_db_constellation_ids():
    result = await get_constellation_ids()
    return result


@app_v1.post("/db/region_insert")
async def post_db_region_data(region: Region):
    await insert_region_data(region)
    return {"result": "region is created"}


@app_v1.post("/db/constellation_insert")
async def post_db_constellation_data(constellation: Constellation):
    await insert_constellation_data(constellation)
    return {"result": "constellation is created"}
