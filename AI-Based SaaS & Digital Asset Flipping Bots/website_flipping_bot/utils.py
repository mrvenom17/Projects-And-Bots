# utils.py

def save_website_report(report):
    """Save a website report to a file."""
    with open('logs/website_report.txt', 'a') as f:
        f.write(report + '\n\n')