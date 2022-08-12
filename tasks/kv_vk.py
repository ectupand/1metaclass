from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.
    Например,
    flip_kv_vk({
        'tokyo': 'Токио',
        'moscow': 'Москва',
    }) == {
        'Токио': 'tokyo',
        'Москва': 'moscow',
    }
    """
    return {y: x for x, y in d.items()}

a={'key1': 'value1',
    'key2': 'value2'}
print(flip_kv_vk(a))



def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - массив ключей конфликтующих
    значений.
    Например,
    flip_kv_vk({
        'Санкт-Петербург': '+3',
        'Москва': '+3',
    }) == {
        '+3': ['Москва', 'Санкт-Петербург'],
    }
    """
    new_keys = dict.fromkeys(d.values())
    for keys in new_keys:
        new_keys[keys] = []

    for key in new_keys:

        for keys in d:

            if key == d[keys]:
                new_keys[key].append(keys)

    return new_keys


a = {'Санкт-Петербург': '+3',
        'Москва': '+3',}
print(flip_kv_vk_safe(a))
