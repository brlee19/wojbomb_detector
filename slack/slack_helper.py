from slackclient import SlackClient
from config import BOT_TOKEN, CHANNEL

class SlackHelper:

    def __init__(self):
        self.slack_token = BOT_TOKEN
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = CHANNEL
    
    def post_message_to_channel(self, msg):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=msg,
        )

if __name__ == '__main__':
    print("I was initialized!")
    helper = SlackHelper()
    helper.post_message_to_channel("Hello world")
    print("got here without an error")