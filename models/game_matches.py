from db import *


class GameMatches(BaseModel):
    datestart = CharField(null=True)
    durationmatch = CharField(null=True)
    game = CharField(null=True)
    idlocation = IntegerField(null=True)
    idsession = IntegerField(null=True)
    modes = CharField(null=True)
    playedmaps = CharField(null=True)
    players = IntegerField(null=True)
    submodes = CharField(null=True)
    timeend = CharField(null=True)
    timestart = CharField(null=True)

    class Meta:
        table_name = 'game_matches'
