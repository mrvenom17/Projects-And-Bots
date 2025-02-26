# outreach.py

import smtplib
from email.mime.text import MIMEText
from config import OUTREACH_MESSAGE_TEMPLATE

def send_email(to_email, name, platform):
    """Send a personalized outreach email to an influencer."""
    message = OUTREACH_MESSAGE_TEMPLATE.format(name=name, platform=platform)
    
    msg = MIMEText(message)
    msg['Subject'] = 'Collaboration Opportunity'
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def run_outreach():
    """Main function to run the outreach bot."""
    data = pd.read_csv('output/evaluated_influencers.csv')
    
    for _, row in data.iterrows():
        send_email(row['email'], row['name'], row['platform'])

if __name__ == "__main__":
    run_outreach()