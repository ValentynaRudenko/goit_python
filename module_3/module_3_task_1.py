from datetime import datetime


def get_days_from_today(date: str):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_days = date_object.toordinal()
        current_date = input("Enter the current date - 'YYYY-MM-DD': ")
        current_date_object = datetime.strptime(current_date,  "%Y-%m-%d")
        current_date_days = current_date_object.toordinal()
        timediff = current_date_days - date_days
        print(timediff)
    except ValueError:
        print("Data format must be : 'YYYY-MM-DD'\nTry again.")
    except TypeError:
        print("Data format must be a string: 'YYYY-MM-DD'\nTry again.")


get_days_from_today("2021-10-09")
