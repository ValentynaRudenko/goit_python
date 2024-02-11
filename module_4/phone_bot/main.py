from phone_bot import parse_input, add_contact, \
                    change_contact, show_phone, \
                    show_all


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input.strip():
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good buy!")
                break
            elif command == "hello":
                print("How can I help you? ")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(args, contacts))
            else:
                print("Invalid command.")
        else:
            print("Your input is empty")


if __name__ == "__main__":
    main()