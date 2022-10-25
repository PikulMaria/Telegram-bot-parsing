import requests


def send_telegram(text: str):
    token = '5328032499:AAGl3s1ZatvAROfdwRlsxKRK3UXG22x62uc'
    url = "https://api.telegram.org/bot"
    channel_id = '722892722'
    
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
    })

    if r.status_code != 200:
        raise Exception("post_text error")


def main():
    send_telegram('Привет, я бот с уведомлениями о сетах!')


if __name__ == '__main__':
    main()