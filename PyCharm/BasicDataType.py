#!/usr/bin/env python3

# Filename : BasicDataType.py

# python中的变量不需要声明
counter = 100 # 整型
miles = 100.0 # 浮点型
name = "Bob" # 字符串
d = e = f = 1, 2, "kim" # 创建一个实例对象，三个变量被分配到相同的内存空间
a, b, c = 1, 2, "kim"  # 多个对象指定多个变量

print(type(a),type(b),type(c)) # type()函数可以查询变量所指向的对象类型

# 等待用户输入
input("\n\n按下 enter 键后退")

# 多行语句
import sys; x = "runoob";sys.stdout.write(x + "\n");

# Python中的模块导入 - import 导入整个模块，from...import导入特定模块
for i in sys.argv:
    print(i)

from sys import argv,path
print('path',path)  # 已经导入path成员，此时引用不需要sys.path












