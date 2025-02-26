# utils.py

def save_article_to_file(topic, article):
    """Save generated article to a text file."""
    with open(f'output/{topic.replace(" ", "_")}.txt', 'w') as f:
        f.write(article)