import random
a = random.randint(1,100)
b = 0
c = 0
print("=========ВИКТОРИНА==========")
print("Вы должны угадать число.")
while b != a:
    b = int(input())
    if b > a:
        print("число меньше")
        c += 1
    elif b < a:
        print("число больше")
        c += 1
print("Поздравляем! Вы выиграли за "+str(c) +" попыток.")
