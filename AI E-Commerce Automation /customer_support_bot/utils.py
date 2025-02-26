# utils.py

def log_conversation(customer_id, query, response):
    """Log customer conversations for future reference."""
    with open('logs/conversations.log', 'a') as f:
        f.write(f"{customer_id} - Query: {query}\nResponse: {response}\n\n")