# email_manager.py

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import logging
from config import GOOGLE_GMAIL_API_KEY

def setup_gmail_service():
    """Set up Gmail API service."""
    creds = Credentials(GOOGLE_GMAIL_API_KEY)
    service = build('gmail', 'v1', credentials=creds)
    return service

def send_email(to, subject, body):
    """Send an email using Gmail API."""
    service = setup_gmail_service()
    
    message = f"Subject: {subject}\n\n{body}"
    try:
        service.users().messages().send(userId='me', body={'raw': message}).execute()
        logging.info(f"Email sent to {to}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")