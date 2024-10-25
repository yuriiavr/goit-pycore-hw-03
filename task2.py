import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []

    unique_numbers = set()
    while len(unique_numbers) < quantity:
        num = random.randint(min, max)
        unique_numbers.add(num)

    return sorted(unique_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
