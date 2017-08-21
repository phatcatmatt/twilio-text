from twilio.rest import Client
from keys import twilio_keys

client = Client(twilio_keys['account'], twilio_keys['token'])

message = client.messages.create(to=twilio_keys['recipient'], from_=twilio_keys['twilio_phone'], body="hiya buddy")