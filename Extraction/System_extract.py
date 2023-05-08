import requests

db_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/constellation_ids").json()
# db_system_ids = requests.get("http://127.0.0.1:8000/v1/db/system_ids").json()
db_system_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/system/constellation/ids").json()
db_constellation_ids = [x for x in db_constellation_ids if x not in db_system_constellation_ids]
# print(len(db_system_ids))
count = 0

for constellation in db_constellation_ids:
    # if count >= 500:
    #     break
    constellation_system_ids = requests.get(f"http://127.0.0.1:8000/v1/db/system_ids/{constellation}").json()
    for system in constellation_system_ids:
        system_data = requests.get(f"http://127.0.0.1:8000/v1/universe/systems/{system}").json()
        # print(system_data)
        eve_insert = requests.post("http://127.0.0.1:8000/v1/db/system_insert", json=system_data)
        if eve_insert.status_code != 200:
            print(f"Data not inserted for System {system}")
        if eve_insert.text == "\"System is created\"":
            count += 1
        elif eve_insert.text == "\"System already exists\"":
            print("System already exists")
    print(count)
#
# db_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/constellation_ids").json()
# db_system_ids = requests.get("http://127.0.0.1:8000/v1/db/system_ids").json()
# db_system_constellation_ids = requests.get("http://127.0.0.1:8000/v1/db/system/constellation/ids").json()
# # db_constellation_ids = [x for x in db_constellation_ids if x not in db_system_constellation_ids]
# # print(len(db_system_ids))
# count = 0
#
# for constellation in db_constellation_ids:
#     if count >= 20:
#         break
#     constellation_system_ids = requests.get(f"http://127.0.0.1:8000/v1/db/system_ids/{constellation}").json()
#     for system in constellation_system_ids:
#         if system not in db_system_ids:
#             system_data = requests.get(f"http://127.0.0.1:8000/v1/universe/systems/{system}").json()
#             eve_insert = requests.post("http://127.0.0.1:8000/v1/db/system_insert", json=system_data)
#             if eve_insert.status_code != 200:
#                 print(f"Data not inserted for System {system}")
#             if eve_insert.text == "\"System is created\"":
#                 count += 1
#             elif eve_insert.text == "\"System already exists\"":
#                 print("System already exists")
#     print(count)