import random

secret = random.randint(1, 10)
temp = input("不妨猜一下小甲鱼现在心里想的是那个数字吧：")
guess = int(temp)

while guess != secret:
    temp = input("哎呀，猜错了， 请重新输入吧：")
    guess = int(temp)

    if guess == secret:
        print("猜对了，但是没有奖励")
    else:
        if guess > secret:
            print("大了")
        else:
            print("嘿， 小了")
print("游戏结束")