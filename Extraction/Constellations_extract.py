import requests

db_region_ids = requests.get("http://127.0.0.1:8000/v1/db/region_ids").json()
# print(db_region_ids)
count = 0

for region in db_region_ids:
    region_constellation_ids = requests.get(f"http://127.0.0.1:8000/v1/db/constellation_ids/{region}").json()
    for constellation in region_constellation_ids:
        constellation_data = requests.get(f"http://127.0.0.1:8000/v1/db/constellation_data/{constellation}")
        if constellation_data.text == "null":
            constellation_data = requests.get(f"http://127.0.0.1:8000/v1/universe/constellations/{constellation}").json()
            eve_insert = requests.post("http://127.0.0.1:8000/v1/db/constellation_insert", json=constellation_data)
            if eve_insert.status_code != 200:
                print(f"Data not inserted for constellation {constellation}")
            if eve_insert.text == "\"Constellation is created\"":
                count += 1
            elif eve_insert.text == "\"Constellation already exists\"":
                print("Constellation already exists")
    print(count)

