from peewee import *
from config import DB_NAME, DB_HOST, DB_USERNAME, DB_PASSWORD

database = PostgresqlDatabase(DB_NAME, host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD)

class BaseModel(Model):
    class Meta:
        database = database


