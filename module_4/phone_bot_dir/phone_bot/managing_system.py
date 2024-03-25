from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10:
            raise ValueError("Number must have 10 digits")
        else:
            super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            value_datetime = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value_datetime)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, value):
        self.phones.append(Phone(value))

    def edit_phone(self, value, new):
        self.phones = [Phone(new) if phone.value == value else
                       phone for phone in self.phones]

    def delete_phone(self, value):
        self.phones = [phone for phone in self.phones if phone.value != value]

    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return value

    def __str__(self):
        return f"Contact name: {self.name.value}, "\
               f"phones: {'; '.join(p.value for p in self.phones)}, "\
               f"birthday: {self.birthday}"

    def __repr__(self):
        return f"{self.name.value}, "\
               f"{'; '.join(p.value for p in self.phones)}, "\
               f"{self.birthday}"

    def add_birthday(self, value):
        self.birthday = Birthday(value)


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]

    def delete(self, name):
        del self.data[name]

    def get_upcoming_birthdays(self):

        today = datetime.now()
        today_date = today.date()
        birthdays_this_week = []
        users = []

        for user, record in self.data.items():
            name = record.name.value
            birthday = record.birthday.value
            users.append({"name": name, "birthday": birthday})

        for user in users:
            user.update({"birthday": datetime(today.year,
                        user["birthday"].month,
                        user["birthday"].day).date()})
            if user["birthday"] < today_date:
                user.update({"birthday": datetime(today.year+1,
                            user["birthday"].month,
                            user["birthday"].day).date()})
            else:
                days_left = (user["birthday"] - today_date).days
                if 0 <= days_left <= 7 and user["birthday"].weekday() >= 5:
                    user.update({"birthday":
                                 datetime.strftime(user["birthday"], "%d.%m")})
                    birthdays_this_week.append(user)
                elif 0 <= days_left <= 7 and user["birthday"].weekday() < 5:
                    user.update({"birthday":
                                 datetime.strftime(user["birthday"], "%d.%m")})
                    birthdays_this_week.append(user)
        if len(birthdays_this_week) > 0:
            return birthdays_this_week
        else:
            return "There is no upcoming birthdays this week"
