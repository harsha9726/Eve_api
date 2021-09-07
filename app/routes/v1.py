import json


from fastapi import APIRouter, Body
import requests
from utils.const import BASE_URL, TAIL_URL
from utils.DB_functions import get_region_ids, insert_region_data, get_region_constellation_ids, \
    insert_constellation_data, get_constellation_ids, get_region_data, get_constellation_data
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
    region_ids = await get_region_ids()
    result = []
    for region in region_ids:
        result.append(region["region_id"])
    return result


@app_v1.get("/db/region_data/{region_id}", response_model=Region, response_model_exclude=["id"])
async def get_db_region_data(region_id: int):
    region = await get_region_data(region_id)
    return region


@app_v1.get("/db/constellation_ids/{region_id}")
async def get_db_region_constellation_ids(region_id: int):
    result = await get_region_constellation_ids(region_id)
    return result["constellations"]


@app_v1.get("/db/constellation_ids")
async def get_db_constellation_ids():
    constellation_ids = await get_constellation_ids()
    result = []
    for constellation in constellation_ids:
        result.append(constellation["constellation_id"])
    return result


@app_v1.get("/db/constellation_data/{constellation_id}", response_model=Constellation, response_model_exclude=["id"])
async def get_db_constellation_data(constellation_id: int):
    constellation = await get_constellation_data(constellation_id)
    constellation["position"] = json.loads(constellation["position"])
    return constellation


@app_v1.post("/db/region_insert")
async def post_db_region_data(region: Region):
    region_data = await get_region_data(dict(region)["region_id"])
    if region_data:
        return "Region already exists"
    await insert_region_data(region)
    return "Region is created"


@app_v1.post("/db/constellation_insert")
async def post_db_constellation_data(constellation: Constellation):
    constellation_data = await get_constellation_data(dict(constellation)["constellation_id"])
    if constellation_data:
        return "Constellation already exists"
    await insert_constellation_data(constellation)
    return "Constellation is created"
