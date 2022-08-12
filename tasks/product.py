from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    len1 = len(arr1)
    len2 = len(arr2)
    res = []
    if len1 == 0 or len2 == 0:
        return res
    for num in range(len1):
        for num2 in range(len2):
            res.append((arr1[num], arr2[num2]))
    return res


a = [1, 2, 5, 6]
b = [3, 4]
print(cartesian_product(a, b))
##ааааааааа
