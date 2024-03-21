from phone_bot import parse_input, add_contact, \
                    change_contact, show_phone, \
                    show_all, \
                    add_birthday, \
                    show_birthday, \
                    birthdays, \
                    AddressBook
import pickle
from abc import ABC, abstractmethod


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


class UserView(ABC):
    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def get_user_input(self):
        pass


class ConsoleView(UserView):
    def display_message(self, message):
        print(message)

    def get_user_input(self):
        return input("Enter a command: ")


def main(view):
    book = load_data()
    view.display_message("Welcome to the assistant bot!")
    while True:
        user_input = view.get_user_input()
        if user_input.strip():
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                save_data(book)
                view.display_message("Good bye!")
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
    console_view = ConsoleView()
    main(console_view)
