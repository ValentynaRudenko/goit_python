def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"


def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact changed"
    else:
        return "This name isn't in the contacts. Add it"


def show_phone(args, contacts):
    name = args[0]
    names = contacts.keys()
    if name in names:
        return f"Name {name}, phone {contacts[name]}"
    else:
        return "This name isn't in the contacts. Add it"


def show_all(args, contacts):
    if len(contacts) > 0:
        contacts = ""
        for name, phone in contacts.items():
            contacts += f"Name: {name}, tel.: {phone}\n"
            return contacts
    else:
        return "The list of contacts is empty"
