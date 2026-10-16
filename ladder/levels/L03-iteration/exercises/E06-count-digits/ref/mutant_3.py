# M3: intentional fault described in spec.md.
def count_digits(number: int) -> int:
    count = 1
    while True:
        count = count + 1
        number = number // 10
        if number == 0:
            break
    return count


def digit_sum(number: int) -> int:
    total = 0
    while number > 0:
        total = total + number % 10
        number = number // 10
    return total
