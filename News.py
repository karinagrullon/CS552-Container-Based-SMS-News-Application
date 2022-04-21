from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC12d2e83761c42fb6789b9487b17179f8"
# Your Auth Token from twilio.com/console
auth_token  = "cd573188f42ddae3df9e9f9e624769d9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16073749303", 
    from_="+19853063991",
    body="Hello from Python!")

print(message.sid)