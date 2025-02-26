# utils.py

def validate_post_time(post_time):
    """Validate that the post time is in the correct format."""
    from datetime import datetime
    try:
        datetime.strptime(post_time, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False