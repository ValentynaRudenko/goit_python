from typing import Callable
import re
from decimal import Decimal


def generator_numbers(string: str) -> Decimal:
    pattern = r"\d+\.\d+"
    numbers = re.findall(pattern, string)
    for i in numbers:
        yield Decimal(i)


def sum_profit(string: str, generator: Callable[[str], Decimal]):
    sum_num = sum([num for num in generator(string)])
    return sum_num


text = "Загальний дохід працівника складається з декількох частин:\
        1000.01 як основний дохід, доповнений додатковими надходженнями\
              27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
