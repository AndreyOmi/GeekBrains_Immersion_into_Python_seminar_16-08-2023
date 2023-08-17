'''
Задача № 2: Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
'''

BASE = 16

hex_chars = "0123456789ABCDEF"
hex_string = ""
minus_flag = False
decimal_number_for_validation = None

decimal_number = int(input("Введите число: "))
decimal_number_for_validation = decimal_number

# Если пользователь введет отрицательное число
if decimal_number < 0:
    decimal_number = abs(decimal_number)
    minus_flag = True

while decimal_number > 0:
    remainder = decimal_number % BASE
    hex_string = hex_chars[remainder] + hex_string
    decimal_number //= BASE

if minus_flag:
     hex_string =  "-" + hex_string

print(f'Это число в {BASE}-ой системе счисления: {hex_string}')
print(f'Это число в {BASE}-ой системе счисления с помощью hex(): {hex(decimal_number_for_validation)}')