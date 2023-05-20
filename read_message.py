import os  # Add this line to import the os module
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://slack.com/api/conversations.history" 
token =  os.getenv('SLACK_BOT_OAUTH')

header={
    "Authorization": "Bearer {}".format(token)
}

payload  = {
    "channel" : "C0582MH6Y6M"
    }

res = requests.get(url, headers=header, params=payload)
struct = res.json()

print(struct.message)