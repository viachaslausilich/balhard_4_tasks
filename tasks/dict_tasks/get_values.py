"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает значения в словаре
"""


def get_values(collection: dict):
    # TODO вставить код сюда
    result = dict.values(collection)
    return result


if __name__ == '__main__':
    assert (100, 200) == tuple(get_values({1: 100, 2: 200}))
    print('Решено!')
