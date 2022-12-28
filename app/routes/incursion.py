from fastapi import APIRouter
import requests
from utils.DB_functions import get_constellation_data, get_system_data

app_incursion = APIRouter()


@app_incursion.get("/")
async def get_incursion_json():
    json = requests.get("https://esi.evetech.net/latest/incursions/?datasource=tranquility").json()
    result = []
    for item in json:
        constellation = await get_constellation_data(item["constellation_id"])
        systems = [await get_system_data(x) for x in item["infested_solar_systems"]]
        staging = await get_system_data(item["staging_solar_system_id"])
        sec = [staging if staging is None else round(staging["security_status"], 2)]
        staging = [staging if staging is None else staging["name"]]
        systems = [x if x is None else x["name"] for x in systems]
        result.append({"constellation": constellation["name"], "Systems": systems, "Status": item["state"],
                       "Mom Spawned": "Yes" if item["has_boss"] else "No", "Staging": staging, "Sec. status": sec,
                       "Influence": item["influence"]})
    return result
