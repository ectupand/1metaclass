__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
