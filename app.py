from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'SMSNews' or body == 'smsnews' or body == 'SMSnews' or body == 'Smsnews':
        resp.message('''
        Thank you for using SMS News. Please choose from the following options to make a news request: 
        - Latest (all)
        - World
        - US
        - Politics
        - Business
        - Tech
        - Health
        - Sports
        - Art
        - Fashion
        ''')
    elif body == 'Latest':
        resp.message("You have chosen: Latest")
    elif body == 'World':
        resp.message("You have chosen: World")
    elif body == 'US' or body == 'Us':
        resp.message("You have chosen: US")
    elif body == 'Politics':
        resp.message("You have chosen: Politics")
    elif body == 'Business':
        resp.message("You have chosen: Business")
    elif body == 'Tech':
        resp.message("You have chosen: Tech")
    elif body == 'Health':
        resp.message("You have chosen: Health")
    elif body == 'Sports':
        resp.message("You have chosen: Sports")
    elif body == 'Art':
        resp.message("You have chosen: Art")
    elif body == 'Fashion':
        resp.message("You have chosen: Fashion")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
