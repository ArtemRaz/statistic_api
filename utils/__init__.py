from datetime import datetime


def try_parse_int(val):
    if val:
        return int(val) if val.isdigit() else None


def try_parse_datetime(val, date_format):
    if val:
        return datetime.strptime(val, date_format)
