import os
import json
import datetime

def load_json_file(file_path):
    """
    Загрузить содержимое JSON файла.

    :param file_path: Путь к JSON файлу.
    :return: Содержимое файла в виде объекта Python.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def save_to_json_file(data, file_path):
    """
    Сохранить данные в JSON файл.

    :param data: Данные для сохранения.
    :param file_path: Путь к JSON файлу.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_directory_exists(directory_path):
    """
    Убедиться, что директория существует. Если нет - создать.

    :param directory_path: Путь к директории.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def current_timestamp():
    """
    Получить текущий временной отпечаток в формате строки.

    :return: Строковое представление текущего временного отпечатка.
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Дополнительные функции могут быть добавлены по мере необходимости...
