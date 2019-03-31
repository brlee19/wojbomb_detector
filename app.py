import os
from flask import Flask, request, make_response, render_template
from slack import SlackHelper
from twitter import TwitterStreamer

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    helper = SlackHelper()
    helper.post_message_to_channel("Hello world from Flask's main")
    return 'Hello World'

@app.route("/tweets", methods=["GET"])
def stream_tweets():
    streamer = TwitterStreamer()
    public_tweets = streamer.api.home_timeline()
    for tweet in public_tweets:
      print(tweet.text)

    return 'Hello from /tweetz'



if __name__ == '__main__':
    app.run()

