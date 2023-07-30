# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#  Программа должна возвращать сумму и произведение* дробей.
#  Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


one = input("Введите первую дробь: ").split('/')
two = input("Введите вторую дробь: ").split('/')

num_sum = int(one[0])*int(two[1]) + int(two[0])*int(one[1])
denom_sum = int(one[1])*int(two[1])
sum_fract = [num_sum, denom_sum]
multi_fract = [int(one[0])*int(two[0]), int(two[1])*int(one[1])]
a1,b1 = sum_fract
while b1:
    a1,b1 = b1, a1 % b1
a2,b2 = multi_fract
while b2:
    a2,b2 = b2, a2 % b2
print(f'{sum_fract[0]//a1}/{sum_fract[1]//a1}', f'{multi_fract[0]//a2}/{multi_fract[1]//a2}')
one_f = Fraction(f'{one[0]}/{one[1]}')
two_f = Fraction(f'{two[0]}/{two[1]}')
print(one_f + two_f, one_f * two_f)