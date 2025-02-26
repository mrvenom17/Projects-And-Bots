# utils.py

def save_content_to_file(content, filename):
    """Save generated content to a file."""
    with open(f'output/{filename}', 'w') as f:
        f.write(content)