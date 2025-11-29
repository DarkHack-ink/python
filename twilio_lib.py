import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # optional, loads .env

ACCOUNT_SID = os.environ['***************']
AUTH_TOKEN  = os.environ['****************']
FROM_NUMBER = os.environ['***************']

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(to: str, body: str, status_callback: str | None = None):
    """
    Send an SMS and return the Message SID.
    status_callback: optional URL Twilio will POST status updates to.
    """
    try:
        message = client.messages.create(
            body=body,
            from_=FROM_NUMBER,
            to=to,
            status_callback=status_callback  # optional
        )
        print("Sent:", message.sid)
        return message.sid
    except Exception as e:
        print("Error sending SMS:", e)
        raise

if __name__ == "__main__":
    # Example usage
    sid = send_sms("+91XXXXXXXXXX", "Hello from Twilio + Python!")
    print("Message SID:", sid)
