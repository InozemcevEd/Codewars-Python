# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python


import re

# Алфавит
a = ord('a')
alphabet = [chr(i) for i in range(a, a + 26)]


# Наибольий общий делитель
def greatest_common_multiple(num1, num2):
    result = num1 % num2  # старайся задвать переменным наиболее осмысленные имена и избегать общих

    # вот тут лучше использовать именованные переменные, потому что условия выносить в result это не сильно читабельно
    # и не расширяемо
    return num2 if result == 0 else greatest_common_multiple(num2, result)


# Подбираем решение сравнения
def find_solution(num, letter):
    x = 0
    while True:
        if num * x % 26 == letter:
            return x
        x += 1


# Чтобы декодировать одну букву с номером k, нужно найти решения сравнения вида:  number * x ≡ k(mod 26)
# Известно, что такое сравнение имеет решение в следующем случае:
# d = НОД(number, 26), d делит k
def decode(r):  # что такое r?
    decode_str = ''
    # Выделяем число из строки
    number = re.findall(r'\d+', r)[0]
    d = greatest_common_multiple(int(number), 26)
    r = list(re.sub(number, '', r))
    number = int(number)
    for letter in r:
        if (alphabet.index(letter) + 1) % d != 0:
            return "Impossible to decode"
        else:
            decode_str += alphabet[find_solution(int(number), alphabet.index(letter))]
    return decode_str


# над именованием переменных стоит поработать. Это приходит с опытом. Есть шутка, что в программировании всего 2
# проблемы, именование и инвалидация распределенного кеша:) Вторая часть шутки тоже приходит с опытом)