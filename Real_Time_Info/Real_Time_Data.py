from datetime import datetime

def get_real_time_data():
    """Returns the current time, date, and day."""
    now = datetime.now()
    return {
        "time": now.strftime('%I:%M %p'),
        "date": now.strftime('%d %B %Y'),
        "day": now.strftime('%A')
    }
