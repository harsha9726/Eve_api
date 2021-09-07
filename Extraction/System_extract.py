import requests

db_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/constellation_ids").json()
# print(db_region_ids)
count = 0

for constellation in db_constellation_ids:
    if count == 100:
        break
    constellation_system_ids = requests.get(f"http://127.0.0.1:8000/v1/db/system_ids/{constellation}").json()
    for system in constellation_system_ids:
        if count == 100:
            break
        system_data = requests.get(f"http://127.0.0.1:8000/v1/db/system_data/{system}")
        if system_data.text == "null":
            system_data = requests.get(f"http://127.0.0.1:8000/v1/universe/systems/{system}").json()
            eve_insert = requests.post("http://127.0.0.1:8000/v1/db/system_insert", json=system_data)
            if eve_insert.status_code != 200:
                print(f"Data not inserted for System {system}")
            if eve_insert.text == "\"System is created\"":
                count += 1
            elif eve_insert.text == "\"System already exists\"":
                print("System already exists")
    print(count)
