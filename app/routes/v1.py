import json
from typing import Union

from fastapi import APIRouter, Body
import requests
from utils.const import BASE_URL, TAIL_URL
from utils.DB_functions import get_region_ids, insert_region_data, get_region_constellation_ids, \
    insert_constellation_data, get_constellation_ids, get_region_data, get_constellation_data, \
    get_system_ids, get_system_data, insert_system_data, get_constellation_system_ids, get_constellation_region_ids, \
    get_system_constellation_ids
from models.region import Region
from models.constellation import Constellation
from models.system import System

app_v1 = APIRouter()


@app_v1.get("/universe/regions", tags=["Universe", "Region"])
async def get_universe_regions():
    url = f"{BASE_URL}/universe/regions/{TAIL_URL}"
    region = requests.get(url)
    return region.json()


@app_v1.get("/universe/regions/{region_id}", tags=["Universe", "Region"])
async def get_region_detail(region_id: int):
    url = f"{BASE_URL}/universe/regions/{region_id}/{TAIL_URL}"
    region = requests.get(url)
    return region.json()


@app_v1.get("/universe/constellations/{constellation_id}", tags=["Universe", "Constellation"])
async def get_constellation_detail(constellation_id: int):
    url = f"{BASE_URL}/universe/constellations/{constellation_id}/{TAIL_URL}"
    constellation = requests.get(url)
    return constellation.json()


@app_v1.get("/universe/systems/{system_id}", tags=["Universe", "System"])
async def get_constellation_detail(system_id: int):
    url = f"{BASE_URL}/universe/systems/{system_id}/{TAIL_URL}"
    system = requests.get(url)
    return system.json()


@app_v1.get("/db/region_ids", tags=["Region", "DB"])
async def get_db_region_ids():
    region_ids = await get_region_ids()
    result = []
    for region in region_ids:
        result.append(region["region_id"])
    return result


@app_v1.get("/db/constellation_ids", tags=["Constellation", "DB"])
async def get_db_constellation_ids():
    constellation_ids = await get_constellation_ids()
    result = []
    for constellation in constellation_ids:
        result.append(constellation["constellation_id"])
    return result


@app_v1.get("/db/system_ids", tags=["System", "DB"])
async def get_db_system_ids():
    system_ids = await get_system_ids()
    result = []
    for system in system_ids:
        result.append(system["system_id"])
    return result


@app_v1.get("/db/constellation_ids/{region_id}", tags=["Constellation", "DB"])
async def get_db_region_constellation_ids(region_id: int):
    result = await get_region_constellation_ids(region_id)
    if result:
        return result["constellations"]
    return []


@app_v1.get("/db/constellation/region/ids/", tags=["Region", "DB"])
async def get_db_constellation_region_ids():
    result = await get_constellation_region_ids()
    regions = []
    if result is None:
        return []
    for item in result:
        regions.append(item["region_id"])
    return regions


@app_v1.get("/db/system_ids/{constellation_id}", tags=["System", "DB"])
async def get_db_constellation_system_ids(constellation_id: int):
    result = await get_constellation_system_ids(constellation_id)
    if result:
        return result["systems"]
    return []


@app_v1.get("/db/system/constellation/ids/", tags=["Constellation", "DB"])
async def get_db_system_constellation_ids():
    result = await get_system_constellation_ids()
    constellations = []
    if result is None:
        return []
    for item in result:
        constellations.append(item["constellation_id"])
    return constellations


@app_v1.get("/db/region_data/{region_id}", response_model=Union[Region, None], response_model_exclude=["id"], tags=["Region", "DB"])
async def get_db_region_data(region_id: int):
    region = await get_region_data(region_id)
    return region


@app_v1.get("/db/constellation_data/{constellation_id}", response_model=Union[Constellation, None], response_model_exclude=["id"],
            tags=["Constellation", "DB"])
async def get_db_constellation_data(constellation_id: int):
    constellation = await get_constellation_data(constellation_id)
    if constellation:
        constellation["position"] = json.loads(constellation["position"])
    return constellation


@app_v1.get("/db/system_data/{system_id}", response_model=Union[System, None], response_model_exclude=["id"], tags=["System", "DB"])
async def get_db_constellation_data(system_id: int):
    system = await get_system_data(system_id)
    if system:
        system["planets"] = json.loads(system["planets"])
        system["position"] = json.loads(system["position"])
    return system


@app_v1.post("/db/region_insert", tags=["Region", "DB"])
async def post_db_region_data(region: Region):
    region_data = await get_region_data(dict(region)["region_id"])
    if region_data:
        return "Region already exists"
    await insert_region_data(region)
    return "Region is created"


@app_v1.post("/db/constellation_insert", tags=["Constellation", "DB"])
async def post_db_constellation_data(constellation: Constellation):
    constellation_data = await get_constellation_data(dict(constellation)["constellation_id"])
    if constellation_data:
        return "Constellation already exists"
    await insert_constellation_data(constellation)
    return "Constellation is created"


@app_v1.post("/db/system_insert", tags=["System", "DB"])
async def post_db_system_data(system: System):
    system_data = await get_system_data(dict(system)["system_id"])
    if system_data:
        return "System already exists"
    await insert_system_data(system)
    return "System is created"
