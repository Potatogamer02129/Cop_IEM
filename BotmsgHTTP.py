import requests
def send_message(api, chat_id, text):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(api)
    data = {'chat_id': chat_id, 'text': text}
    try:
        requests.post(url, data=data, timeout=5)
    except requests.exceptions.RequestException as e:
        pass
api = "8389217347:AAG_S9-Pcm5p0YRUGN5oNjgrZvhS_wzPGsQ"
def notify(url):
    text = f"Woohoo Your product is now Available\n{url}"
    send_message(api,743282007,text)

