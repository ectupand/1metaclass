from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    len1 = len(arr1)
    len2 = len(arr2)
    res = []
    if len1 == 0 or len2 == 0:
        return res
    for num2 in range(min(len1, len2)):
        res.append((arr1[num2], arr2[num2]))
    return res
