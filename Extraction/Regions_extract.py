import requests

db_region_ids = requests.get("http://127.0.0.1:8000/v1/db/region_ids").json()
# print(db_region_ids)
region_ids = []
for region_id in db_region_ids:
    region_ids.append(region_id["region_id"])

# print(region_ids)

eve_region_ids = requests.get("http://127.0.0.1:8000/v1/universe/regions").json()

for region_id in eve_region_ids:
    if region_id not in region_ids:
        eve_region_data = requests.get(f"http://127.0.0.1:8000/v1/universe/regions/{region_id}/").json()
        # print(eve_region_data)
        if "description" not in eve_region_data.keys():
            eve_region_data["description"]=""
        # print(eve_region_data)

        eve_region_insert = requests.post("http://127.0.0.1:8000/v1/db/region_insert", json=eve_region_data)
        status_code = eve_region_insert.status_code
        if status_code != 200:
            print("data not inserted for "+region_id)


