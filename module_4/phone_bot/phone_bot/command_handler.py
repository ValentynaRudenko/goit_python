from .managing_system import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me a name please"
        except KeyError:
            return "This name isn't in the contact list"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book):
    name, phone = args
    # contacts[name] = phone
    # return "Contact added"
    if name not in book.keys():
        new_record = Record(name)
        new_record.add_phone(phone)
        book.add_record(new_record)
        return "Contact added"
    else:
        existing_record = book[name]
        existing_record.add_phone(phone)
        return "Contact added"


@input_error
def change_contact(args, book):
    name, phone_old, phone_new = args
    # if name in contacts.keys():
    #     contacts[name] = phone
    #     return "Contact changed"
    # else:
    #     return "This name isn't in the contacts. Add it first."
    if name in book.keys():
        existing_record = book[name]
        existing_record.edit_phone(phone_old, phone_new)
        return "Contact added"
    else:
        return "This name isn't in the contacts. Add it first."


@input_error
def show_phone(args, book):
    name = args[0]
    if book.find(name):
        for name, record in book.items():
            if name == args[0]:
                return '; '.join(p.value for p in record.phones)
    else:
        return "The contact isn't found"


@input_error
def show_all(args, book):
    if len(book) > 0:
        all_contacts = []
        for name, record in book.items():
            all_contacts.append(record)
        return all_contacts
    else:
        return "The list of contacts is empty."


@input_error
def add_birthday(args, book):
    name, birthday = args
    if name not in book.keys():
        new_record = Record(name)
        new_record.add_birthday(birthday)
        book.add_record(new_record)
        return "Contact and birthday added"
    else:
        existing_record = book[name]
        existing_record.add_birthday(birthday)
        return "Birthday added"


@input_error
def show_birthday(args, book):
    name = args[0]
    if book.find(name):
        for name, record in book.items():
            if name == args[0]:
                return record
    else:
        return "The contact isn't found"


@input_error
def birthdays(args, book):
    if len(book) > 0:
        return book.get_upcoming_birthdays()
    else:
        "The adress book is empty"
