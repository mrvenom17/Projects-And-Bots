# chatbot.py

import openai
from twilio.rest import Client
from config import OPENAI_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, FAQS

openai.api_key = OPENAI_API_KEY

# Configure logging
import logging
logging.basicConfig(filename='logs/chatbot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_response(query):
    """Generate a response using OpenAI GPT-4."""
    if query in FAQS:
        return FAQS[query]
    
    prompt = f"Answer the following customer query:\n{query}\nProvide a concise and helpful response."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def send_whatsapp_message(to_number, message):
    """Send a WhatsApp message using Twilio."""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=f"whatsapp:{to_number}"
        )
        logging.info(f"Message sent to {to_number}: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending message: {e}")

def handle_customer_query(query, customer_phone):
    """Handle customer query and send a response."""
    logging.info(f"Received query from {customer_phone}: {query}")
    response = generate_response(query)
    send_whatsapp_message(customer_phone, response)

if __name__ == "__main__":
    # Example usage
    handle_customer_query("How can I track my order?", "+1234567890")