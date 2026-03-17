"""Домашняя работа 5"""


"""
1
Продвинутый sum.
Встроенная функция sum() в python вызывает ошибку, если один из элементов последовательности 
не является числом, например sum([1, 2, ‘A’]).
Напишите функцию sum_ignore_non_numbers(), которая имеет один параметр items (список или кортеж).
Функция должна вернуть сумму всех чисел (int, float) в переданной последовательности. 
При этом все нечисловые значения должны игнорироваться.
Если чисел нет, то функция должна вернуть 0.
Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3
"""

def sum_ignore_non_numbers(items):
    total = 0
    for x in items:
        if isinstance(x, (int, float)):
            total += x
    return total

# print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))


"""
2
Треугольник.
Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон треугольника.
Функция должна возвращать True, если треугольник с переданными сторонами может существовать, 
и False в противном случае.
Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.
"""

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# print(is_triangle(2, 4, 9))
# print(is_triangle(3, 4, 5))


"""
3
Среднее значение.
Напишите функцию average(), которая принимает произвольное количество позиционных аргументов. 
(Можно передать любое число аргументов).
Функция должна посчитать среднее арифметическое всех переданных чисел. 
(Представим, что в функцию передаются только числа).
Если не передать ни одного аргумента, то функция должна вернуть 0.

Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5
"""

def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# print(average(1, 2, 3, 4, 5, 6, 7, 8))


"""
4
Общие строки.
Напишите функцию common_strings(), которая имеет 3 параметра: list1, list2 и ingore_case=True 
(значение по умолчанию).
Функция должна вернуть новых список из тех значений, которые встречаются в обоих списках.
 При этом, если ignore_case равен True, то функция должна игнорировать регистр и считать
  строки “string” и “STRING” одинаковыми.  В противном случае функция должна учитывать регистр
   символов и считать такие строки разными.
Все строки в результирующем списке должны быть в нижнем регистре.
Например, существуют 2 списка:
fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’]
fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’, ‘cherry’].
"""

def common_strings(list1, list2, ignore_case=True):
    result = []

    if ignore_case:
        second_list_lower = [item.lower() for item in list2]

        for item in list1:
            item_lower = item.lower()
            if item_lower in second_list_lower and item_lower not in result:
                result.append(item_lower)
    else:
        for item in list1:
            if item in list2 and item.lower() not in result:
                result.append(item.lower())

    return result
# fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
# fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

# print(common_strings(fruits_1, fruits_2))


"""
1
КаКоЕ-тО вОлНеНиЕ.

Создать переменную text, значение которой определяется через ввод данных с клавиатуры.
Каждый символ под четным индексом должен быть переведен в верхний регистр, а каждый нечетный в нижний.
Вывести полученную строку на экран.

Если была введена строка “Чтобы продать что-нибудь ненужное, нужно сначала купить что-нибудь 
ненужное, а у нас денег нет.”, то результат должен быть  “ЧтОбЫ ПрОдАтЬ ЧтО-НиБуДь нЕнУжНоЕ, 
нУжНо сНаЧаЛа кУпИтЬ ЧтО-НиБуДь нЕнУжНоЕ, а у нАс дЕнЕг нЕт.”
"""

def wave_text(text):
    result = []

    for x in range(len(text)):
        if x % 2 == 0:
            result.append(text[x].upper())
        else:
            result.append(text[x].lower())

    return "".join(result)
