from .DB import db_fetch, db_execute
from psycopg2.extras import Json

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


async def insert_constellation_data(constellation, position):
    query = """insert into constellation(constellation_id ,name,  region_id, systems)
                values (:constellation_id ,:name,  :region_id, :systems)"""
    constellation = dict(constellation)
    values = constellation
    #
    # await db_execute(query, False, values)

    query = """insert into position(x, y, z, object_id, object_type)
                values (:x, :y, :z, :object_id, :object_type)"""
    values = dict(position)
    values["object_id"] = constellation["constellation_id"]
    values["object_type"] = "constellation"

    await db_execute(query, False, values)
