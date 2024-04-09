from db import *


class GameMatches(BaseModel):
    datestart = DateField(null=True)
    durationmatch = TimeField(null=True)
    game = CharField(null=True)
    idlocation = IntegerField(null=True)
    idsession = IntegerField(null=True)
    modes = CharField(null=True)
    playedmaps = CharField(null=True)
    players = IntegerField(null=True)
    submodes = CharField(null=True)
    timestart = DateTimeField(null=True)
    timeend = DateTimeField(null=True)


    class Meta:
        table_name = 'game_matches'
