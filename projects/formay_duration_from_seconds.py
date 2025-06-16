def format_duration(seconds):
    if seconds == 0:
        return "now"

    duration = {"year": 31536000, "day": 86400, "hour": 3600, "minute": 60, "second": 1}
    fin = []
    for unit, value in duration.items():
        if seconds >= value:
            count = seconds // value
            seconds %= value
            fin.append(f"{count} {unit}{'s' if count > 1 else ''}")

    if not fin:
        return "now"
    elif len(fin) == 1:
        return fin[0]
    else:
        return ", ".join(fin[:-1]) + " and " + fin[-1]


print(format_duration(35215998394546))
