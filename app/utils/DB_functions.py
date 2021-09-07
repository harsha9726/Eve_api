from .DB import db_fetch, db_execute
from fastapi.encoders import jsonable_encoder
import json


async def get_region_ids():
    query = """select region_id from region order by 1"""
    result = await db_fetch(query, is_one=False)
    return result


async def get_region_data(region_id):
    query = """select * from region where region_id=:region_id order by 1"""
    values = {"region_id": region_id}
    result = await db_fetch(query, True, values)
    return result


async def get_constellation_ids():
    query = """select constellation_id from constellation order by 1"""
    result = await db_fetch(query, is_one=False)
    return result


async def get_region_constellation_ids(region_id):
    query = """select constellations from region where region_id=:region_id order by 1"""
    values = {"region_id": region_id}
    # print(query,values)
    result = await db_fetch(query, True, values)
    return result


async def get_constellation_data(constellation_id):
    query = """select * from constellation where constellation_id=:constellation_id order by 1"""
    values = {"constellation_id": constellation_id}
    result = await db_fetch(query, True, values)
    return result


async def get_system_ids():
    query = """select system_id from system order by 1"""
    result = await db_fetch(query, is_one=False)
    return result


async def get_constellation_system_ids(constellation_id):
    query = """select systems from constellation where constellation_id=:constellation_id order by 1"""
    values = {"constellation_id": constellation_id}
    # print(query,values)
    result = await db_fetch(query, True, values)
    return result


async def get_system_data(system_id):
    query = """select * from system where system_id=:system_id order by 1"""
    values = {"system_id": system_id}
    result = await db_fetch(query, True, values)
    return result


async def get_constellation_system_ids(constellation_id):
    query = """select systems from constellation where constellation_id=:constellation_id order by 1"""
    values = {"constellation_id": constellation_id}
    # print(query,values)
    result = await db_fetch(query, True, values)
    return result


async def insert_region_data(region):
    query = """insert into region(constellations ,description, name, region_id)
                values (:constellations ,:description, :name, :region_id)"""
    values = dict(region)
    await db_execute(query, False, values)


async def insert_constellation_data(constellation):
    query = """insert into constellation(constellation_id ,name,  region_id, systems, position)
                values (:constellation_id ,:name,  :region_id, :systems, :position)"""
    constellation = dict(constellation)
    constellation["position"] = json.dumps(jsonable_encoder(constellation["position"]))
    values = constellation

    await db_execute(query, False, values)


async def insert_system_data(system):
    query = """insert into system(constellation_id ,name,  planets, position, security_class, security_status,  
    star_id, stargates, stations, system_id) 
    values (:constellation_id ,:name,  :planets,  :position, :security_class, :security_status, :star_id,  :stargates, 
    :stations, :system_id) """
    system = dict(system)
    system["position"] = json.dumps(jsonable_encoder(system["position"]))
    system["planets"] = json.dumps(jsonable_encoder(system["planets"]))
    values = system

    await db_execute(query, False, values)
