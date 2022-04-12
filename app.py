from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

#news api
from newsapi.newsapi_client import NewsApiClient
newsapi = NewsApiClient(api_key='b29884325c374de6a4c78d5e7d894226')
# keyword = input("Please enter the keyword to search the news for : ")


# Twilio
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message

    all_articles = newsapi.get_everything(q = body, language='en')

    for article in all_articles['articles']:

        resp.message('''
        -------------- Everything from the news channels --------------
        Source :'''  + article['source']['name'] +
         '''Title :  ''' + article['title'] +
         ''' Description : '''  + article['description'] +
        ''' website : ''' + article['url'])
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)








