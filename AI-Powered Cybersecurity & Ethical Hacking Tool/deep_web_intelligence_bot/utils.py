# utils.py

def save_threat_report(report):
    """Save a threat report to a file."""
    with open('logs/threat_report.txt', 'a') as f:
        f.write(report + '\n\n')