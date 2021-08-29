BASE_URL = "https://esi.evetech.net/latest"
TAIL_URL = "?datasource=tranquility&language=en"

DB_HOST = "host.docker.internal"
DB_USERNAME = "admin"
DB_PASSWORD = "admin"
DB_NAME = "Eve_api"

DB_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"