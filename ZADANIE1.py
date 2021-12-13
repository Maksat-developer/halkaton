# Задание 1:
# У вас есть идея создать Back-end для игры: "Угадай число."

# Данный код генерирует рандомное число.
###################

###################
# С помощью функции:

# спрашивайте число от пользователя.

# Запустите бесконечный цикл!




# И пытайтесь спрашивать у пользователя какое-то число каждый раз.
# Если пользователь угадал число которое сгенерировал компьютер остановите цикл и скажите пользователю - "Вы угадали!"
# Если пользователь не угадал вы снова спросите у него число.
# Если пользователь 3 раза подряд не угадал число, вы останавливаете цикл и говорите: "Вы проиграли..."
#######################################################################
import random as rd
print("Игра Угадай число. У Вас есть 3 попытки")
g_d = 0
random_number = rd.randint(0,10)
while g_d < 3:
    my_number = int(input("Введите число от 0 до 10: "))
    print("Ваше число: ", my_number)
    print ("Загаданное число: ", random_number)
    g_d += 1
    if my_number != random_number:
        print ("Вы не угадали! Попробуйте ещё раз.")
    if my_number == random_number:
        break
if my_number == random_number:
    print ("ВЫ УГАДАЛИ!")
else:
    print ("Вы проиграли.")
