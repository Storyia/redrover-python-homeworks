"""Домашнее задание (занятие 6)"""
from lesson_05.hw_05 import (
    sum_ignore_non_numbers,
    is_triangle,
    average,
    common_strings,
    wave_text
)

"""
1
Модуль.
-
-
Перенесите ваши функции из прошлого домашнего задания в отдельный
файл и импортируйте их в основной (исполняемый) файл.
Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.
"""
print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))

print(is_triangle(2, 4, 9))
print(is_triangle(3, 4, 5))

print(average(1, 2, 3, 4, 5, 6, 7, 8))

fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
print(common_strings(fruits_1, fruits_2))

text = input("Введите строку: ")
print(wave_text(text))

"""2
Анонимная функция 🎭.
-
Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
Функция должна возвращать x, возведенное в степень y.
"""
my_pow = lambda x, y: x ** y

print(my_pow(2, 3))
print(my_pow(5, 2))
"""
3
Змея 🐍.
-
-
-
Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
Функция должна создать новую строку, где все гласные буквы
aeiouyAEIOUY в строке text дублируются.
Например, такой вызовы функции snake_talk(“Harry”) должен вернуть
строку “Haaryy”.
"""
def snake_talk(text):
    vowels = "aeiouyAEIOUY"
    return "".join(x * 2 if x in vowels else x for x in text)
print(snake_talk("Harry"))
print(snake_talk("snake"))

"""
Повторение прошлого материала.
Ответьте на следующие вопросы:
•
•
•
Что такое изменяемый и неизменяемый объект?
Как НЕЛЬЗЯ называть переменную?
Зачем нужна строка документации в функции?
"""



