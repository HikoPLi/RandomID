
import json
import random
import string


def generate_random_id(length):

    chars = string.ascii_letters + string.digits + "^&*!=@?$"
    newid = ''.join(random.choice(chars) for _ in range(length))
    return newid


def check_id_exists(id, id_set):
    exists = id in id_set
    return exists


def save_id_to_file(userinput, id, filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    axis = {f"{userinput}": id}
    data.append(axis)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    userinput = input("Please enter a key word: ")
    id_set = set()

    while True:
        idLength = 30
        new_id = generate_random_id(idLength)

        if check_id_exists(new_id, id_set) == False:
            id_set.add(new_id)
            save_id_to_file(userinput, new_id, 'ids.json')
            break

    print(f"ID：{new_id}")


if __name__ == "__main__":

    main()
