from datetime import datetime
from uuid import UUID
from models import WeaponStatistic, SkinStatistic


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
