from slackclient import SlackClient
from config import SLACK


class SlackHelper:

    def __init__(self):
        self.slack_token = SLACK['BOT_TOKEN']
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = SLACK['CHANNEL_ID']
    
    def post_message_to_channel(self, msg):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=msg,
        )


if __name__ == '__main__':
    print("I was initialized!")
    print("got here without an error")