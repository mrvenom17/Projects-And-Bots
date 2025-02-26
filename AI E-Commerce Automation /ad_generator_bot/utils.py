# utils.py

def format_ad_for_platform(ad, platform):
    """Format ad copy for specific platforms."""
    if platform == 'facebook':
        return f"Facebook Ad:\n{ad}"
    elif platform == 'google_ads':
        return f"Google Ads:\n{ad}"
    elif platform == 'instagram':
        return f"Instagram Ad:\n{ad}"
    else:
        return ad