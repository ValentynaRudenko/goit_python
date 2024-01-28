import re


def normalize_phone(num):
    pattern = r"[^0-9\+]"
    repl = ""
    phone = re.sub(pattern, repl, num)
    if phone.startswith("+"):
        pass
    elif phone.startswith("38"):
        phone = "+" + phone
    else:
        phone = "+38" + phone
    return phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

updated_list = [normalize_phone(num) for num in raw_numbers]

print("Normalizized phones for SMS-messaging: ", updated_list)
