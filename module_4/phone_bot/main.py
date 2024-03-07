from phone_bot import parse_input, add_contact, \
                    change_contact, show_phone, \
                    show_all, \
                    add_birthday, \
                    show_birthday, \
                    birthdays, \
                    AddressBook
import pickle


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input.strip():
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                save_data(book)
                print("Good buy!")
                break
            elif command == "hello":
                print("How can I help you? ")
            elif command == "add":
                print(add_contact(args, book))
            elif command == "change":
                print(change_contact(args, book))
            elif command == "phone":
                print(show_phone(args, book))
            elif command == "all":
                print(show_all(args, book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(args, book))
            else:
                print("Invalid command.")
        else:
            print("Your input is empty")


if __name__ == "__main__":
    main()
