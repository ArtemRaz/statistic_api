from flask import request
from models.game_matches_new import GameMatchesNew
from utils import try_parse_int
from datetime import datetime
from app import app


@app.route("/add_statistic", methods=["POST"])
def add_statistic():
    datestart = datetime.strptime(request.form.get('datestart'), "%Y.%m.%d").date() if request.form.get('datestart') else None
    durationmatch = datetime.strptime(request.form.get('durationmatch'), "%M:%S").time() if request.form.get('durationmatch') else None
    game = request.form.get('game')
    idlocation = try_parse_int(request.form.get('idlocation'))
    idsession = try_parse_int(request.form.get('idsession'))
    modes = request.form.get('modes')
    playedmaps = request.form.get('playedmaps')
    players = try_parse_int(request.form.get('players'))
    submodes = request.form.get('submodes')
    timeend = datetime.strptime(f"{request.form.get('datestart')} {request.form.get('timeend')}", "%Y.%m.%d %H:%M:%S") if request.form.get('timeend') else None
    timestart = datetime.strptime(f"{request.form.get('datestart')} {request.form.get('timestart')}", "%Y.%m.%d %H:%M:%S") if request.form.get('timestart') else None

    id = GameMatchesNew.create(datestart=datestart,
                               durationmatch=durationmatch,
                               game=game,
                               idlocation=idlocation,
                               idsession=idsession,
                               modes=modes,
                               playedmaps=playedmaps,
                               players=players,
                               submodes=submodes,
                               timeend=timeend,
                               timestart=timestart)

    return {'id': id.id}, 200


