# ## Задание 2 - самое частое слово в тексте

# Написать функцию, которая принимает строку текста и возвращает слово, встречающееся чаще всего.  
# Функция должна учитывать, что в тексте могут быть знаки препинания и разные регистры букв.


def most_common_word(text):
    text = text.lower()
    words = text.split(" ")

    dictionary = dict()
    for word in words:
        stripped = word.strip(".!?")
        if stripped in dictionary:
            dictionary[stripped] += 1
        else:
            dictionary[stripped] = 1

    maximum_value = 0
    maximum_key = ""
    for key, value in dictionary.items():
        if maximum_value < value:
            maximum_key = key
            maximum_value = value

    return maximum_key


assert most_common_word("кот кот собака") == "кот", "Самое частое слово — кот"
assert most_common_word("Кот кот КОТ собака") == "кот", "Регистр должен игнорироваться"
assert most_common_word("молоко, молоко! молоко? хлеб.") == "молоко", "Знаки препинания должны игнорироваться"
assert most_common_word("слово") == "слово", "Ожидалось единственное слово"
res = most_common_word("а б а б")
assert res in ("а", "б"), "Ожидалось одно из слов с максимальной частотой"
