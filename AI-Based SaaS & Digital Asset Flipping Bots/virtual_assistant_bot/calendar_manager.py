# calendar_manager.py

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime
import logging
from config import GOOGLE_CALENDAR_API_KEY

def setup_calendar_service():
    """Set up Google Calendar API service."""
    creds = Credentials(GOOGLE_CALENDAR_API_KEY)
    service = build('calendar', 'v3', credentials=creds)
    return service

def schedule_event(event_name, start_time, end_time):
    """Schedule an event in Google Calendar."""
    service = setup_calendar_service()
    
    event = {
        'summary': event_name,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
    }
    
    try:
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        logging.info(f"Event created: {event_result.get('htmlLink')}")
    except Exception as e:
        logging.error(f"Error scheduling event: {e}")