#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
Валидация с использоваением Marshmallow
"""

import sys
import json
from datetime import date
import marshmallow


class StuffSchema(marshmallow.Schema):
    name = marshmallow.fields.String()
    post = marshmallow.fields.String()
    year = marshmallow.fields.Integer()


def get_worker() -> dict:
    """
    Запросить данные о работнике.
    :return dict:
    """
    name = input("Фамилия и инициалы >> ")
    post = input("Должность >> ")
    year = int(input("Год поступления >> "))

    return {
        'name': name,
        'post': post,
        'year': year
    }


def display_workers(staff):
    """
    Отобразить список работников.
    :param staff:
    :return:
    """
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^8} |".format(
                "№",
                "Ф.И.О.",
                "Должность",
                "Год"
            )
        )
        print(line)

        for idx, worker in enumerate(staff, 1):
            print(
                "| {:^4} | {:^30} | {:^20} | {:^8} |".format(
                    idx,
                    worker.get('name', ''),
                    worker.get('post', ''),
                    worker.get('year', 0)
                )
            )
        print(line)
    else:
        print("Список сотрудников пуст.")


def select_workers(staff, period: int) -> list:
    """
    Выбрать работников с заданным стажем
    :param staff:
    :param period:
    :return result:
    """
    today = date.today()

    result = list()

    for employee in staff:
        if today.year - employee.get('year', today.year) >= period:
            result.append(employee)

    return result


def save_workers(file_name: str, staff):
    """
    Сохранить всех работников в файл JSON.
    :param file_name:
    :param staff:
    :return:
    """

    with open(file_name, 'w', encoding='utf-8') as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_workers(file_name: str) -> list:
    """
    Загрузить всех работников из файла JSON.
    :param file_name:
    :return dict:
    """
    with open(file_name, 'r', encoding='utf-8') as fin:
        schema = StuffSchema()
        res = list()
        for rec in json.load(fin):
            res.append(schema.load(rec))
        return res


def main():
    """
        Главная функция программы
        """
    # Список работников.
    workers = list()

    while True:
        # Запросить команду из терминала
        command = input(">>> ").lower()

        # Выполнить действие в соответствии с командой.
        if command == "exit":
            break

        elif command == "add":
            worker = get_worker()

            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == "list":
            display_workers(workers)

        elif command.startswith("select "):
            parts = command.split(maxsplit=1)

            period = int(parts[1])

            selected = select_workers(workers, period)

            display_workers(selected)
        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]

            save_workers(file_name, workers)

        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]

            workers = load_workers(file_name)

        elif command == "help":
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершиьт работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
