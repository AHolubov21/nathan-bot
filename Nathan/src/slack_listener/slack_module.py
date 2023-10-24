import requests
import websocket
import json

class SlackModule:

    def __init__(self, token):
        self.token = token
        self.connect_url = self.get_rtm_url()
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {self.token}"
        }

    def get_rtm_url(self):
        response = requests.get(
            "https://slack.com/api/rtm.connect",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        data = response.json()
        return data.get("url", None)

    def send_message(self, channel, text):
        data = {
            "channel": channel,
            "text": text
        }
        response = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers=self.headers,
            json=data
        )
        return response.json()

    def listen(self):
        def on_message(ws, message):
            print("Received:", message)
            # Здесь можно добавить логику обработки входящих сообщений

        ws = websocket.WebSocketApp(
            self.connect_url,
            on_message=on_message
        )
        ws.run_forever()

# Пример использования:

if __name__ == "__main__":
    SLACK_TOKEN = "YOUR_SLACK_TOKEN"
    slack_module = SlackModule(SLACK_TOKEN)
    
    # Отправка сообщения
    response = slack_module.send_message("#general", "Hello, World!")
    print(response)

    # Прослушивание входящих сообщений через веб-сокеты
    slack_module.listen()
