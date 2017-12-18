#!/usr/bin/env python3

a = 11
b = 21
"""
    %	取模 - 返回除法的余数
    **	幂 - 返回x的y次幂
    //	取整除 - 返回商的整数部分
"""


# 2.比较运算符
"""
    ==	等于 - 比较对象是否相等
    !=	不等于 - 比较两个对象是否不相等
    >=	大于等于 - 返回x是否大于等于y。
    <=	小于等于 - 返回x是否小于等于y。
"""

# 3.赋值运算符
"""
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
"""

# 4.逻辑运算符
a = 10
b = 20
if (a and b):
    print("a 和 b 都为true")
else:
    print("a 和 b 有一个部位true")

if (a or b) :
    print('a 和 b 都为true，或者其中一个为true')
else:
    print ("2 - 变量 a 和 b 都不为 true")

# 4.身份运算符
if a is b :
    print("两个对象引自同一个对象")
else:
    print("两个对象不是引自同一个对象")

if a is not b :
    print("没有相同的标识")
else:
    print("有相同的标识")


