from db import *
from models.game_matches import GameMatches
from models.skin import Skin


class SkinStatistic(BaseModel):
    game_match = ForeignKeyField(GameMatches, null=True)
    skin = ForeignKeyField(Skin, null=True)
    usage_time = TimeField(null=True)


    class Meta:
        table_name = 'skin_statistic'
