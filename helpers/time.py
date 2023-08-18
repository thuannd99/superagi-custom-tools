from datetime import datetime


def is_potential_timestamp(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def convert_to_timestamp(s):
    if is_potential_timestamp(s):
        return float(s)
    else:
        dt = datetime.strptime(s, "%Y/%m/%d %H:%M:%S %z")
        return dt.timestamp()
