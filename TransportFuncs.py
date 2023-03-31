


def interpret_seating(seating: str):
    if seating == "SEA":
        return "Seating Available"
    elif seating == "SDA":
        return "Standing Available"
    elif seating == "LSD":
        return "Limited Standing"
    else:
        return ""


def interpret_type(bus_type: str):
    if bus_type == "SD":
        return "Single Deck"
    elif bus_type == "DD":
        return "Double Deck"
    elif bus_type == "BD":
        return "Bendy"
    else:
        return ""


def calculate_est_duration(dur_1: int, dur_2: int, dur_3: int):
    if dur_1 != 0 and dur_2 != 0 and dur_3 != 0 and dur_1 < 1000:
        est_duration = (dur_1 + dur_2 + dur_3) / 3
    elif dur_2 != 0 and dur_3 != 0:
        est_duration = (dur_2 + dur_3) / 2
    elif dur_1 != 0 and dur_2 != 0 and dur_1 < 1000:
        est_duration = (dur_1 + dur_2) / 2
    elif dur_2 != 0:
        est_duration = dur_2
    else:
        est_duration = dur_1

    return round(est_duration, 1)