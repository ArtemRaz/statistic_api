import zlib

from flask import request, jsonify
from models import GameMatches, WeaponStatistic, SkinStatistic
from utils import try_parse_int, try_parse_datetime, decode_to_files
from app import app


@app.route("/crush_report", methods=["POST", "GET"])
def crush_report():
    r = request
    data = zlib.decompress(r.data)
    decode_to_files(data)
    return ""


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

    return jsonify(id=new_record.id)


@app.route("/add_weapon_statistic", methods=["POST"])
def add_weapon_statistic():
    req_json = request.get_json()

    game_match = req_json.get('game_match')
    weapon = req_json.get('weapon')
    if not game_match:
        return jsonify(code=400, message="Parameter game_match was not provided"), 400
    if not weapon:
        return jsonify(code=400, message="Parameter weapon was not provided"), 400
    kills = req_json.get('kills')
    headshots = req_json.get('headshots')
    shots = req_json.get('shots')
    reloads = req_json.get('reloads')
    usage_time = try_parse_datetime(req_json.get('usage_time'), "%M:%S")

    new_record = WeaponStatistic.create(
        game_match=game_match,
        weapon=weapon,
        kills=kills,
        headshots=headshots,
        shots=shots,
        reloads=reloads,
        usage_time=usage_time
    )

    return jsonify(id=new_record.id)


@app.route("/add_skin_statistic", methods=["POST"])
def add_skin_statistic():
    req_json = request.get_json()

    game_match = req_json.get('game_match')
    skin = req_json.get('skin')
    if not game_match:
        return jsonify(code=400, message="Parameter game_match was not provided"), 400
    if not skin:
        return jsonify(code=400, message="Parameter skin was not provided"), 400
    usage_time = try_parse_datetime(req_json.get('usage_time'), "%M:%S")

    new_record = SkinStatistic.create(
        game_match=game_match,
        skin=skin,
        usage_time=usage_time
    )

    return jsonify(id=new_record.id)
