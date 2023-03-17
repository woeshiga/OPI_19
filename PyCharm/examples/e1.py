#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from datetime import date


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


def load_workers(file_name: str) -> dict:
    """
    Загрузить всех работников из файла JSON.
    :param file_name:
    :return dict:
    """
    with open(file_name, 'r', encoding='utf-8') as fin:
        return json.load(fin)


if __name__ == '__main__':
    pass
