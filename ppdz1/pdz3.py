from random import randint

lower_limit = 0
upper_limit = 1000
number_attempts = 10

while True:
    num_user = int(input("загадайте число: "))
    if num_user < lower_limit or num_user > upper_limit:
        print("Введите число в диапазоне от ", lower_limit, "до ", upper_limit)
    else:
        break
counter_1 = 0

while counter_1 < number_attempts:
    counter_1 += 1
    num_bot = randint(lower_limit, upper_limit)
    print("попытка №", counter_1, "  число: ", num_bot)
    if num_bot == num_user:
        print("угадал число с количеством попыток: ", counter_1)
        break
    elif num_bot > num_user:
        print("загаданное число меньше")
        upper_limit = num_bot - 1
    else:
        print("загаданное число больше")
        lower_limit = num_bot + 1
else:
    print("попытки исчерпаны,число не угадано")
    counter_1 = -1
