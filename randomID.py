import datetime
import os
import json
import random
import string


# ct = datetime.datetime.now()
# YYYY = ct.strftime("%Y")
# MM = ct.strftime("%m")
# DD = ct.strftime("%d")
# return f"{YYYY}-{MM}-{DD}"

def generate_random_id(length):

    chars = string.ascii_letters + string.digits + "^&*!=@?$"
    newid = ''.join(random.choice(chars) for _ in range(length))
    return newid


def check_id_exists(id, id_set):
    exists = id in id_set
    return exists


def save_id_to_file(year, alternative, id, filename):
    try:
        with open(f"{filename}.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    axis = {f"{alternative}": year + id}
    data.append(axis)

    with open(f"{filename}.json", 'w') as f:
        json.dump(data, f, indent=4)


def random_id():
    os.chdir('ID')
    year = datetime.datetime.now().strftime("%Y")

    if os.path.exists(year) == False:
        os.mkdir(year)

    os.chdir(year)
    keyword = input("Please enter a key word: ")
    alternative = input("Please enter a alternative word: ")
    id_set = set()

    while True:
        idLength = 30
        new_id = generate_random_id(idLength)

        if check_id_exists(new_id, id_set) == False:
            id_set.add(new_id)
            save_id_to_file(year, alternative, new_id, keyword)
            break

    print(f"ID：{new_id}")
