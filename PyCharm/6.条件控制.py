#!/usr/bin/env python3

age = int(input("请输入你的年龄："))
print()
if age < 18:
    print("少年")
elif age == 20:
    print("青年")
elif age > 20:
    print("成年")

num = 7
guess = -1
print("猜数字")
while guess != num:
    guess = int(input("输入你要猜的数字："))
    if guess == num:
        print("猜对了")
    elif guess > num:
        print("大了")
    else:
        print("小了")
