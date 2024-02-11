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
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact changed"
    else:
        return "This name isn't in the contacts. Add it first."


@input_error
def show_phone(args, contacts):
    name = args[0]
    names = contacts.keys()
    if name in names:
        return f"Name {name}, phone {contacts[name]}"
    else:
        return "This name isn't in the contacts."


@input_error
def show_all(args, contacts):
    if len(contacts) > 0:
        all_contacts = ""
        for name, phone in contacts.items():
            all_contacts += f"Name: {name}, tel.: {phone}\n"
        return all_contacts
    else:
        return "The list of contacts is empty."
