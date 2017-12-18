#!/usr/bin/env python3

# 两个元素的和确定了下一个数
a,b = 0, 1
while b < 10:
    print(b)
    a,b = b ,a+b
