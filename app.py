from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

#news api
from newsapi.newsapi_client import NewsApiClient
newsapi = NewsApiClient(api_key='b29884325c374de6a4c78d5e7d894226')
# keyword = input("Please enter the keyword to search the news for : ")


# Twilio
app = Flask(__name__)


class articles: 
    def __init__(self, source, title, description, website, publishedAt): 
        self.source = source 
        self.title = title
        self.description = description
        self.website = website
        self.publishedAt = publishedAt


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message

    all_articles = newsapi.get_everything(q = ''.join(e for e in body if e.isalnum()), language='en')

    data = [] 


    for article in all_articles['articles'][:5]:
        data.append(articles(article['source']['name'], article['title'], article['description'], article['url'], article['publishedAt']))

    c = 0

    for arti in data[:5]:
        c = c+1
        resp.message('''

        News <'''+ str(c) +'''/5>\n''' + arti.publishedAt + 
       '''
       \nTitle: ''' + arti.title +
         '''
         \nDescription: '''  + arti.description +
         '''
         \nSource: '''  + arti.source +
        '''\n''' + arti.website)
        
    
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)