__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """чет 24, нечет 13
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even =[]
    odd = []
    for i in range(0, len(arr)):
        if arr[i] % 2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    if sum(odd) == 0:
        return 0
    return sum(even)/sum(odd)

print(even_odd([1, 2, 3, 4, 5]))
