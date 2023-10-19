import os
import slack

# Инициализация Slack клиента
SLACK_TOKEN = os.environ['xoxb-2130371976770-6066452493427-f7m01ZdNcAfdkQfFSSVfdxsJ'] 
client = slack.WebClient(token=SLACK_TOKEN)

def post_message(channel, text):
    """
    Отправляет сообщение в указанный Slack канал.
    """
    response = client.chat_postMessage(channel=channel, text=text)
    return response

def add_reaction(channel, timestamp, emoji):
    """
    Добавляет реакцию к сообщению в Slack.
    """
    response = client.reactions_add(channel=channel, timestamp=timestamp, name=emoji)
    return response

# Пример использования:
# post_message("#general", "Hello, World!")
# add_reaction("#general", "timestamp_of_message", "thumbsup")
