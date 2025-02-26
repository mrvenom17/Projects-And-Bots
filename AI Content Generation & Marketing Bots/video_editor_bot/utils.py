# utils.py

def generate_captions(text):
    """Generate captions from raw text."""
    lines = text.split('. ')
    with open('captions.txt', 'w') as f:
        for line in lines:
            f.write(line.strip() + '\n')