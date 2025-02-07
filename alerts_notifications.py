from twilio.rest import Client

TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"

def send_sms_alert(message, phone_number):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(to=phone_number, from_="+1234567890", body=message)

send_sms_alert("Fire detected at location! Immediate response needed.", "+9876543210")
