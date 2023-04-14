#!/user/bin/env python3
# -*- coding: utf-8 -*-
import json

LETTERS = 'eyuioa'

def load_words(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def add_words(file_name: str, word: dict) -> None:
    with open(file_name, 'r', encoding='utf-8') as f:
        content_json = json.load(f)
    content_json.append(word)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(content_json, f)


def update_json(file_name: str, words: list) -> list:
    for item in words:
        for letter in item["word"]:
            if letter in LETTERS:
                item["result"] = True
            else:
                item["result"] = False
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(words, f)
    return words


def display(words):
    """
    Отобразить список работников.
    :param staff:
    :return:
    """
    if words:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} |".format(
                "№",
                "Слово",
                "Результат"
            )
        )
        print(line)

        for idx, worker in enumerate(words, 1):
            print(
                "| {:^4} | {:^30} | {:^20} |".format(
                    idx,
                    worker.get('word', ''),
                    worker.get('result', ''),
                )
            )
        print(line)
    else:
        print("Список пуст.")


def main():
    words = list()

    while True:
        command = input(">>> ")
        if command.startswith("load "):
            words = load_words(command.split(maxsplit=1)[1])
        elif command == "list":
            display(words)
        elif command == "exit":
            break
        elif command.startswith("add "):
            word = input("Введите слово >> ")
            words.append({"word": word, "result": False})
            add_words(command.split(maxsplit=1)[1], {"word": word, "result": False})
        elif command.startswith("update "):
            words = update_json(command.split(maxsplit=1)[1], words)


if __name__ == '__main__':
    main()
