from yaml import safe_load

with open("config/db.yaml") as file:
    db_config = safe_load(file)
    DB_NAME = db_config["NAME"]
    DB_HOST = db_config["HOST"]
    DB_USERNAME = db_config["USERNAME"]
    DB_PASSWORD = db_config["PASSWORD"]

with open("config/server.yaml") as file:
    server_config = safe_load(file)
    SERVER_HOST = server_config["HOST"]
    SERVER_PORT = server_config["PORT"]
    SERVER_DEBUG = server_config["DEBUG"]

with open("config/telegram.yaml") as file:
    telegram_config = safe_load(file)
    TELEGRAM_TOKEN = telegram_config["TOKEN"]
    TELEGRAM_CHAT_ID = telegram_config["CHAT_ID"]


