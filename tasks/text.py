from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    a = str.split(text)
    print(a)
    if len(a) == 1:
        return (a[0], a[0])
    elif len(a) == 2 and len(a[0]) == len(a[1]):
        return (a[0], a[1])
    if len(a) == 0:
        return (None, None)

    a.sort(key=len)
    return (a[0], a[-1])


a = 'how do your'
print(find_shortest_longest_word(a))
