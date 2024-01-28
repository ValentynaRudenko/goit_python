from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.now()
    today_date = today.date()
    birthdays_this_week = []

    for user in users:
        user.update({"birthday":
                     datetime.strptime(user["birthday"], "%Y.%m.%d").date()})
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
                days_to_add = 7 - user["birthday"].weekday()
                user.update({"birthday": (datetime(today.year,
                                          user["birthday"].month,
                                          user["birthday"].day) +
                                          timedelta(days=days_to_add)).date()})
                birthdays_this_week.append(user)
            elif 0 <= days_left <= 7 and user["birthday"].weekday() < 5:
                birthdays_this_week.append(user)
    return birthdays_this_week


users = [
    {"name": "John Doe", "birthday": "1985.02.03"},
    {"name": "Jane Smith", "birthday": "1990.01.30"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("The list of congratulations this week: ", upcoming_birthdays)
