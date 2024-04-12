import uuid

from db import *


class Skin(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, constraints=[SQL('DEFAULT gen_random_uuid()')])
    name = CharField(null=True)
    image_url = CharField(null=True)

    class Meta:
        table_name = 'skin'
