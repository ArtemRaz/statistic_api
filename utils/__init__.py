import uuid

import requests
from datetime import datetime
from models import WeaponStatistic, SkinStatistic
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def try_parse_int(val):
    if val:
        return int(val) if val.isdigit() else None


def try_parse_datetime(val, date_format):
    if val:
        return datetime.strptime(val, date_format)


def create_weapon(game_match, weapon):
    weapon_uuid = weapon.get('weapon')
    kills = weapon.get('kills')
    headshots = weapon.get('headshots')
    shots = weapon.get('shots')
    reloads = weapon.get('reloads')
    usage_time = try_parse_datetime(weapon.get('usage_time'), "%M:%S")

    WeaponStatistic.create(
        game_match=game_match,
        weapon=weapon_uuid,
        kills=kills,
        headshots=headshots,
        shots=shots,
        reloads=reloads,
        usage_time=usage_time
    )


def create_skin(game_match, skin):
    skin_uuid = skin.get('skin')
    usage_time = try_parse_datetime(skin.get('usage_time'), "%M:%S")

    SkinStatistic.create(
        game_match=game_match,
        skin=skin_uuid,
        usage_time=usage_time
    )


def send_to_tg_channel(text):
    url_req = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/sendMessage" + "?chat_id=" + TELEGRAM_CHAT_ID + "&text=" + text
    results = requests.get(url_req)
    if results.status_code == 200:
        if not results.json()['ok']:
            print(results.json())

