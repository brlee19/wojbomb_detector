import os
from flask import Flask, request, make_response, render_template
from slack import SlackHelper

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
  helper = SlackHelper()
  helper.post_message_to_channel("Hello world from Flask's main")
  return 'Hello World'

if __name__ == '__main__':
    app.run()

