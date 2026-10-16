# M1: intentional fault from spec.md.
def is_prime(n: int) -> bool:
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def count_primes(low: int, high: int) -> int:
    count = 0
    for number in range(low, high + 1):
        if is_prime(number):
            count = count + 1
    return count


def next_prime(n: int) -> int:
    candidate = n + 1
    while not is_prime(candidate):
        candidate = candidate + 1
    return candidate
