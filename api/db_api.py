from flask import request, jsonify

from db import database
from models import GameMatches
from utils import try_parse_datetime, create_weapon, create_skin
from app import app


@app.route("/add_game_match", methods=["POST"])
def add_game_match():
    req_json = request.get_json()
    datestart = try_parse_datetime(req_json.get('datestart'), "%Y.%m.%d")
    durationmatch = try_parse_datetime(req_json.get('durationmatch'), "%M:%S")
    game = req_json.get('game')
    idlocation = req_json.get('idlocation')
    idsession = req_json.get('idsession')
    modes = req_json.get('modes')
    playedmaps = req_json.get('playedmaps')
    players = req_json.get('players')
    submodes = req_json.get('submodes')
    timeend = try_parse_datetime(f"{req_json.get('datestart')} {req_json.get('timeend')}", "%Y.%m.%d %H:%M:%S")
    timestart = try_parse_datetime(f"{req_json.get('datestart')} {req_json.get('timestart')}", "%Y.%m.%d %H:%M:%S")
    game_version = req_json.get('game_version')
    weapons = req_json.get('weapons')
    skins = req_json.get('skins')

    with database.atomic():
        new_record = GameMatches.create(
            datestart=datestart,
            durationmatch=durationmatch,
            game=game,
            idlocation=idlocation,
            idsession=idsession,
            modes=modes,
            playedmaps=playedmaps,
            players=players,
            submodes=submodes,
            timeend=timeend,
            timestart=timestart,
            game_version=game_version
        )
        for weapon in weapons:
            create_weapon(new_record, weapon)
        for skin in skins:
            create_skin(new_record, skin)

    return jsonify(id=new_record.id)
