import requests

db_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/constellation_ids").json()
constellation_ids = []
# print(db_constellation_ids)
for constellation in db_constellation_ids:
    constellation_ids.append(constellation["constellation_id"])
# print(constellation_ids)
db_region_ids = requests.get("http://127.0.0.1:8000/v1/db/region_ids").json()
# print(db_region_ids)
region_ids = []
for region_id in db_region_ids:
    region_ids.append(region_id["region_id"])

for region in region_ids:
    db_constellation_ids = requests.get(f"http://127.0.0.1:8000/v1/db/constellation_ids/{region}").json()
    db_constellation_ids = db_constellation_ids["constellations"]
    for constellation in db_constellation_ids:
        if constellation not in constellation_ids:
            constellation_data = requests.get(
                f"http://127.0.0.1:8000/v1/universe/constellations/{constellation}").json()
            eve_insert = requests.post("http://127.0.0.1:8000/v1/db/constellation_insert", json=constellation_data)
            if eve_insert.status_code!=200:
                print(f"Data not inserted for constellation {constellation}")
