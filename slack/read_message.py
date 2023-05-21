import os
import requests
from dotenv import load_dotenv


def GetSlackMessage():
    load_dotenv(".env")
    url = "https://slack.com/api/conversations.history"
    token = os.getenv('SLACK_BOT_OAUTH')

    header = {
        "Authorization": "Bearer {}".format(token)
    }

    payload = {
        "channel": "C0582MH6Y6M",
        "limit": 10
    }

    res = requests.get(url, headers=header, params=payload)
    response_data = res.json()

    if response_data["ok"]:
        messages = response_data["messages"]
        if messages:
            for message in messages:
                # print(message["message"])
                print(message["text"])
        else:
            print("No messages found in the channel.")
    else:
        print("Error: {}".format(response_data["error"]))
