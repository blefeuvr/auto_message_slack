import json
import slack

# Find slack ids -> ids.json
# https://api.slack.com/methods/users.list/test

# Find app creds -> creds.json
# https://api.slack.com/apps/***/oauth


SLACK_USERNAME="Père siffleur"
MESSAGE=\
""

def send_message(client, channel, message):
    try:
        res = client.chat_postMessage(
            channel=channel,
            text=message,
            username=SLACK_USERNAME,
            unfurl_links=False
        )
    except Exception as e:
        print(e, channel)
    else:
        if res['ok']:
            print(channel)
        else:
            print('Error: '+ channel)
            print(res)

with open('creds.json', 'r') as f:
    creds = json.load(f)
client = slack.WebClient(token=creds['app_token'])
f = open('ids.list', 'r')
for line in f:
    send_message(client, line.strip(), MESSAGE)