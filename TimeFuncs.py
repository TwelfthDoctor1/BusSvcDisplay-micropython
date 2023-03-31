

def time_str(value: int):
    if value <= 9:
        return f"0{value}"
    else:
        return str(value)


def get_12hr_iden(hr: int):
    if hr >= 12:
        return "PM"
    else:
        return "AM"


def convert_12hr(hr: int):
    if hr > 12:
        return time_str(hr - 12)
    elif hr == 0:
        return "12"
    else:
        return time_str(hr)
