from flask import request
from models import GameMatches
from utils import try_parse_int
from app import app


@app.route("/add_statistic", methods=["POST"])
def add_statistic():
    datestart = request.form.get('datestart')
    durationmatch = request.form.get('durationmatch')
    game = request.form.get('game')
    idlocation = try_parse_int(request.form.get('idlocation'))
    idsession = try_parse_int(request.form.get('idsession'))
    modes = request.form.get('modes')
    playedmaps = request.form.get('playedmaps')
    players = try_parse_int(request.form.get('players'))
    submodes = request.form.get('submodes')
    timeend = request.form.get('timeend')
    timestart = request.form.get('timestart')

    id = GameMatches.create(datestart=datestart,
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


