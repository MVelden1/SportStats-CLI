import datetime


def format_timedelta(td: datetime.timedelta) -> str:
    """Return 'H:MM:SS' if hours > 0 else 'M:SS'."""
    total = int(td.total_seconds())
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}" if hours else f"{minutes}:{seconds:02d}"


def to_seconds(time: str) -> int:
    """Convert H:M:S or M:S or S string into total seconds."""
    parts = [p.strip() for p in time.split(":") if p.strip() != ""]
    if len(parts) == 3:
        hours, minutes, seconds = parts
    elif len(parts) == 2:
        hours = "0"; minutes, seconds = parts
    elif len(parts) == 1:
        hours = "0"; minutes = "0"; seconds = parts[0]
    else:
        raise ValueError("Invalid time format, expected H:M:S, M:S or S")

    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def min_per_km(distance: float, time: int) -> str:
    pace_sec_per_km = time / distance
    return f"{format_timedelta(datetime.timedelta(seconds=pace_sec_per_km))}/km"
