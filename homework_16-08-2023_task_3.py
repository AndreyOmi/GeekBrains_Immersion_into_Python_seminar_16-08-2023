'''
Задача № 3: Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''

from fractions import Fraction

def gcd(a, b): #### функция для НОД
    while b:
        a, b = b, a % b
    return a

def add_fractions(frac1, frac2):
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))
    
    lcm = (denom1 * denom2) // gcd(denom1, denom2)
    new_num1 = num1 * (lcm // denom1)
    new_num2 = num2 * (lcm // denom2)
    
    sum_num = new_num1 + new_num2
    
    return f"{sum_num}/{lcm}"

def multiply_fractions(frac1, frac2):
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))
    
    product_num = num1 * num2
    product_denom = denom1 * denom2
    
    return f"{product_num}/{product_denom}"

frac1 = input("Введите первую дробь в виде a/b : ")
frac2 = input("Введите вторую дробь в виде a/b : ")
    
sum_result = add_fractions(frac1, frac2)
product_result = multiply_fractions(frac1, frac2)
    
print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")
print("\n")
print(f"Сумма дробей с помощью модуля fraction : {Fraction(frac1) + Fraction(frac2)}")
print(f"Произведение дробей с помощью модуля fraction : {Fraction(frac1) * Fraction(frac2)}")