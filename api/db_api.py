from flask import request, jsonify
from models.game_matches import GameMatches
from utils import try_parse_int, try_parse_datetime
from datetime import datetime
from app import app


@app.route("/add_game_match", methods=["POST"])
def add_game_match():
    req_json = request.get_json()
    datestart = try_parse_datetime(req_json.get('datestart'), "%Y.%m.%d").date()
    durationmatch = try_parse_datetime(req_json.get('durationmatch'), "%M:%S").time()
    game = req_json.get('game')
    idlocation = try_parse_int(req_json.get('idlocation'))
    idsession = try_parse_int(req_json.get('idsession'))
    modes = req_json.get('modes')
    playedmaps = req_json.get('playedmaps')
    players = try_parse_int(req_json.get('players'))
    submodes = req_json.get('submodes')
    timeend = try_parse_datetime(f"{req_json.get('datestart')} {req_json.get('timeend')}", "%Y.%m.%d %H:%M:%S")
    timestart = try_parse_datetime(f"{req_json.get('datestart')} {req_json.get('timestart')}", "%Y.%m.%d %H:%M:%S")

    new_record = GameMatches.create(datestart=datestart,
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

    return jsonify(id=new_record.id)
