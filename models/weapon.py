from db import *


class Weapon(BaseModel):
    name = CharField(null=True)
    image_url = CharField(null=True)
    bullets = IntegerField(null=True)

    class Meta:
        table_name = 'weapon'
