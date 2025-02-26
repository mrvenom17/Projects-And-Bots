# assistant.py

import openai
import logging
from calendar_manager import schedule_event
from email_manager import send_email
from config import OPENAI_API_KEY, LOG_FILE

openai.api_key = OPENAI_API_KEY

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_query(query):
    """Process user query using OpenAI GPT-4."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Interpret the following query and determine the action: {query}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def execute_task(task, details):
    """Execute tasks based on user query."""
    if "schedule" in task.lower():
        schedule_event(details['event_name'], details['start_time'], details['end_time'])
    elif "email" in task.lower():
        send_email(details['to'], details['subject'], details['body'])
    elif "reminder" in task.lower():
        logging.info(f"Reminder set for: {details}")
    else:
        logging.warning("Task not recognized.")

def run_virtual_assistant():
    """Main function to run the virtual assistant."""
    logging.info("Starting Virtual Assistant Bot...")
    
    while True:
        query = input("What can I assist you with? ")
        task = process_query(query)
        
        if "schedule" in task:
            event_name = input("Event name: ")
            start_time = input("Start time (YYYY-MM-DD HH:MM): ")
            end_time = input("End time (YYYY-MM-DD HH:MM): ")
            execute_task(task, {'event_name': event_name, 'start_time': start_time, 'end_time': end_time})
        elif "email" in task:
            to = input("Recipient email: ")
            subject = input("Subject: ")
            body = input("Body: ")
            execute_task(task, {'to': to, 'subject': subject, 'body': body})
        else:
            logging.info("No actionable task detected.")

if __name__ == "__main__":
    run_virtual_assistant()