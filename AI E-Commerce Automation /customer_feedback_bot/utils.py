# utils.py

def save_analysis_results(sentiment_scores, topics):
    """Save sentiment scores and topics to a file."""
    with open('output/analysis_results.txt', 'w') as f:
        f.write("Sentiment Scores:\n")
        f.write("\n".join(map(str, sentiment_scores)))
        f.write("\n\nTopics:\n")
        f.write("\n".join(topics))