# utils.py

def parse_date_time(date_time_str):
    """Parse date and time strings into datetime objects."""
    return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')