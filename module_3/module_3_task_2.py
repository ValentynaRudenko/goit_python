import random


def get_numbers_tickets(min: int, max: int, quantity: int):
    lottery_numbers = []
    if max > min and min > 0 and max <= 1000 and\
            (quantity <= max and quantity >= min and quantity <= (max-min)):
        while len(lottery_numbers) < quantity:
            number = random.randint(min, max)
            if number not in lottery_numbers:
                lottery_numbers.append(number)
        else:
            lottery_numbers.sort()
            print(lottery_numbers)
    elif max < min:
        print("maximal number must be greater than ", min)
    elif min < 1:
        print("minimal number must be greater than 0")
    elif max > 1000:
        print("naximal number must be less or equal to 1000")
    elif quantity > max:
        print("quantity must be less or equal to ", max)
    elif quantity < min:
        print("quantity must be greater or equal to ", min)
    elif quantity > (max-min):
        print("quantity must be less or equal to ", max-min)


get_numbers_tickets(1, 49, 6)
