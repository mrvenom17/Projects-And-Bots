# utils.py

def save_flagged_content(content_type, content):
    """Save flagged content to a file."""
    with open('logs/flagged_content.txt', 'a') as f:
        f.write(f"{content_type}: {content}\n")
        