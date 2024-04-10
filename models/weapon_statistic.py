from db import *
from models.game_matches import GameMatches
from models.weapon import Weapon


class WeaponStatistic(BaseModel):
    game_match = ForeignKeyField(GameMatches, null=True)
    weapon = ForeignKeyField(Weapon, null=True)
    kills = IntegerField(null=True)
    headshots = IntegerField(null=True)
    shots = IntegerField(null=True)
    reloads = IntegerField(null=True)
    usage_time = TimeField(null=True)

    class Meta:
        table_name = 'weapon_statistic'
