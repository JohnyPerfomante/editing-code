import os
import sys
import time
import json
import random
import re
from math import pi

DATA_FILE = "data.txt"
CONFIG_FILE = "config.ini"
GLOBAL_FLAG = True


def do_thing(x, y, z=None):
    if z is None:
        z = []
    z.extend([x, y])
    return [i * i for i in z if i > 2]


def calc_sum(numbers):
    return sum(numbers)


def parse_config(cfg_path):
    if not os.path.exists(cfg_path):
        return None

    config = {}
    with open(cfg_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key.strip()] = value.strip()
    return config


def format_user(user):
    name = user.get("Name", "Unknown")
    age = user.get("age", "N/A")
    city = user.get("City", "")
    return f"{name} - age: {age} - city: {city}"


def read_numbers_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            raw = file.read()
    except FileNotFoundError:
        raw = "1,2,3,4,5,6,7,8,9,10"

    numbers = [int(re.sub(r'\s+', '', n)) for n in raw.split(',') if n.strip()]
    return numbers


def sort_list(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value
    return lst


def main():
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else CONFIG_FILE

    big_list = list(range(1, 16))
    total = calc_sum(big_list) * 4 if GLOBAL_FLAG else None

    numbers = read_numbers_from_file(DATA_FILE)
    sorted_numbers = sort_list(numbers.copy())

    cfg_map = parse_config(cfg_path)
    if cfg_map is None:
        print("Конфігураційний файл відсутній або некоректний.")
        cfg_map = {'mode': 'x', 'retry': '3', 'debug': 'false'}

    mode = cfg_map.get('mode', 'x')

    if mode in ('x', 'y', 'z'):
        print(f"MODE: {mode}")
        print(f"TEMP = {total}")
        print(f"LEN = {len(sorted_numbers)}")
    else:
        print("UNKNOWN MODE")

    users = [
        {'Name': 'Ivan', 'age': 30, 'City': 'Kyiv'},
        {'Name': 'Olga', 'age': 25},
        {'Name': 'Stepan', 'age': 41, 'City': 'Lviv'}
    ]

    formatted_users = [format_user(u) for u in users]

    print("\n=== РЕЗУЛЬТАТ ===")
    print(f"Total: {total}")
    print(f"Numbers: {numbers}")
    print(f"Sorted: {sorted_numbers}")
    print(f"Users: {formatted_users}")
    print(f"Current dir: {os.getcwd()}")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Pi: {pi}")
    print(f"Config path: {cfg_path}")
    print(f"Data path: {DATA_FILE}")
    print("=================\n")

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())