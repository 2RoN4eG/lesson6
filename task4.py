# ## Задание 4* - функция flatten_list()

# Написать функцию `flatten_list(lst)`, которая принимает вложенный список и возвращает плоский список.

# Пример:  
# `flatten_list([1, [2, [3, 4], 5], 6]) → [1, 2, 3, 4, 5, 6]`


def flatten_list(lst):
    res = []
    for el in lst:
        if isinstance(el, list):
            res += flatten_list(el)
        else:
            res.append(el)

    return res


assert flatten_list([1, [2, 3]]) == [1, 2, 3], "Ожидался простой плоский список"
assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4], "Ожидалась глубокая распаковка"
assert flatten_list([]) == [], "Ожидался пустой список"
assert flatten_list([[], [1], [], [2, [], 3]]) == [1, 2, 3], "Ожидалось игнорирование пустых вложенных списков"
assert flatten_list([1, ["a", ["b", "c"]], 2]) == [1, "a", "b", "c", 2], "Ожидалась корректная распаковка смешанных типов"
