# программа для запуска(активации) бота в телеграмме(пишем в pycharm)
import requests

url = "https://api.telegram.org/bot{token}/{method}".format(
    token="5115845739:AAHnlllRq6BgKmwA7CSeucC5DPGb6tUh6Gs",
    method="setWebhook"
    # method="getWebhookinfo"
    # method = "deleteWebhook"
)

data = {"url": "https://functions.yandexcloud.net/d4eslc0t6gu1spdidmv4"}

r = requests.post(url, data=data)
print(r.json())