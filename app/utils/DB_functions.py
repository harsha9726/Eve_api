from .DB import db_fetch, db_execute



async def get_region_ids():
    query = """select region_id from region"""
    result = await db_fetch(query, is_one=True)

async def insert_region_data(region):
    query = """insert into region(constellations ,description, name, region_id)
                values (:constellations ,:description, :name, :region_id)"""
    values = dict(region)
    await db_execute(query, False, values)