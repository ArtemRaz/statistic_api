from datetime import datetime
from uuid import uuid4


def try_parse_int(val):
    if val:
        return int(val) if val.isdigit() else None


def try_parse_datetime(val, date_format):
    if val:
        return datetime.strptime(val, date_format)


def decode_to_files(data):
    # // The 'CR1' marker prevents the data router backend to fallback to a backward compatibility version where
    # // a buggy/incomplete header was written at the beginning of the stream and the correct/valid one at the end.
    # uint8 Version[] = {'C', 'R', '1'};
    # Engine\UE5\Source\Runtime\CrashReportCore\Private\CrashUpload.cpp:77

    cursor_pos = 3  # ignore CR1 (see comment)
    file_index = 0

    while cursor_pos < len(data):
        file_length = decode_file_length(data[cursor_pos:cursor_pos + 4])
        cursor_pos += 4
        if file_index == 2:
            file_index += 1
            continue
        if file_index == 5:
            with open(f"files/{uuid4()}.xml", "wb") as file:
                file.write(data[cursor_pos:cursor_pos + file_length])
        file_index += 1
        if file_index > 30:
            break
        cursor_pos += file_length


def decode_file_length(data):
    return int.from_bytes(data, 'little')
