from datetime import datetime

def time_format(time):
    """convert isoformat to normal time format"""
    date = datetime.fromisoformat(time)
    return date.strftime('%Y-%m-%d %H:%M:%S')
