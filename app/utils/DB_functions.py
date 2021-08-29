from .DB import db_fetch, db_execute


async def get_region_ids():
    query = """select region_id from region"""
    result = await db_fetch(query, is_one=False)
