import randomID
import search


def main():
    while True:
        user_choice = input("Create(C) ID or Search(S), (q) for quit: ")
        if user_choice == "C":
            randomID.random_id()
        if user_choice == "S":
            search.search()
        if user_choice == "q":
            print("Thanks for using! ")
            break


if __name__ == "__main__":

    main()
