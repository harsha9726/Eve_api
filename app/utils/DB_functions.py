from .DB import db_fetch, db_execute
from fastapi.encoders import jsonable_encoder
import json

async def get_region_ids():
    query = """select region_id from region"""
    result = await db_fetch(query, is_one=False)
    return result


async def get_constellation_ids():
    query = """select constellation_id from constellation"""
    result = await db_fetch(query, is_one=False)
    return result


async def insert_region_data(region):
    query = """insert into region(constellations ,description, name, region_id)
                values (:constellations ,:description, :name, :region_id)"""
    values = dict(region)
    await db_execute(query, False, values)


async def get_region_constellation_ids(region_id):
    query = """select constellations from region where region_id=:region_id"""
    values = {"region_id": region_id}
    # print(query,values)
    result = await db_fetch(query, True, values)
    return result


async def insert_constellation_data(constellation):
    query = """insert into constellation(constellation_id ,name,  region_id, systems, position)
                values (:constellation_id ,:name,  :region_id, :systems, :position)"""
    constellation = dict(constellation)
    constellation["position"] = json.dumps(jsonable_encoder(constellation["position"]))
    values = constellation

    await db_execute(query, False, values)

