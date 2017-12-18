#!/usr/bin/env python3

import sys
# 迭代器是访问集合的一种方式,从第一个元素开始访问，直到所有元素被访问结束
# list = [1,2,3,4]
# it = iter(list) # 创建迭代器对象
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 生成器是一个返回迭代器的函数
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n) :
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
