import requests

db_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/constellation_ids").json()
# print(db_constellation_ids)

db_region_ids = requests.get("http://127.0.0.1:8000/v1/db/region_ids").json()
# print(db_region_ids)


for region in db_region_ids:
    region_constellation_ids = requests.get(f"http://127.0.0.1:8000/v1/db/constellation_ids/{region}").json()
    for constellation in region_constellation_ids:
        if constellation not in db_constellation_ids:
            constellation_data = requests.get(
                f"http://127.0.0.1:8000/v1/universe/constellations/{constellation}").json()
            eve_insert = requests.post("http://127.0.0.1:8000/v1/db/constellation_insert", json=constellation_data)
            if eve_insert.status_code!=200:
                print(f"Data not inserted for constellation {constellation}")
