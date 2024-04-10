from db import *


class Skin(BaseModel):
    name = CharField(null=True)
    image_url = CharField(null=True)

    class Meta:
        table_name = 'skin'
