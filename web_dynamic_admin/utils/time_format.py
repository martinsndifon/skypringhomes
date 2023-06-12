from datetime import datetime
import pytz

def time_format(time):
    """convert isoformat to normal time format"""
    post_time = datetime.fromisoformat(time)
    current_time = datetime.utcnow().astimezone(pytz.timezone('Africa/Lagos')).replace(tzinfo=None)
    time_difference = current_time - post_time

    # Calculate the time in seconds
    seconds = time_difference.total_seconds()

    if seconds < 60:
        return 'just now'
    elif seconds < 3600:
        minutes = int(seconds / 60)
        if minutes == 1:
            return f'{minutes} minute ago'
        else:
            return f'{minutes} minutes ago'
    elif seconds < 86400:
        hours = int(seconds / 3600)
        if hours == 1:
            return f'{hours} hour ago'
        else:
            return f'{hours} hours ago'
    else:
        days = int(seconds / 86400)
        if days == 1:
            return f'{days} day ago'
        else:
            return f'{days} days ago'
