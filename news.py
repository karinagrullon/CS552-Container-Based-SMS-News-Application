from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "YOUR-TWILIO-ACCOUNT-ID"
# Your Auth Token from twilio.com/console
auth_token  = "YOUR-TWILIO-AUTH-TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+YOUR-PERSONAL-PHONE-NUMBER", 
    from_="+YOUR-TWILIO-PHONE-NUMBER",
    body="Hello from Python!")

