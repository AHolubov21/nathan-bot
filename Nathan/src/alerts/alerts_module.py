import slack_module
import json

class AlertsModule:
    def __init__(self):
        self.slack = slack_module.SlackWebSocketClient()

    def send_alert(self, message):
        self.slack.send_message(message)

    # Другие методы и функции для управления оповещениями.