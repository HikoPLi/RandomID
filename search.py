
import os
import json
import datetime


def search():
    keyword = input("Please enter a key word: ")
    inputID = input("Please enter an ID: ")
    year = datetime.datetime.now().strftime("%Y")

    os.chdir(f"../RandomID/ID/{year}")

    with open(f"{keyword}.json") as idFile:
        json_data = json.load(idFile)

    search_value = str(inputID)
    try:
        for item in json_data:
            for key, value in item.items():
                if value == search_value:
                    print(f"Key with value {search_value}: {key}")
    except:
        print("Wrong input ID! ")
