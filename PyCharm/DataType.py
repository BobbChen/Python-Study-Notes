#!/usr/bin/env python3

# 1.数字
a, b, c, d = 20, 3.4, True, 3 + 4j # 可以同时为多个变量赋值
f = 111
a = "hahah"
''' 
    type（）不会认为子类是父类的一种类型
    isinstance() 认为子类是父类的一种类型
'''
print(type(a),type(b),type(c),type(d))
print(isinstance(f, int))

# 数值运算
print(2 / 4) # 得到一个浮点数
print(2 // 4) # 得到一个整数
print(17 % 3) # 取余数
print(2 ** 5) # 乘方

# 2.字符串 - 字符串中的元素不可变

str = 'Runoob'
print(str[0:-1]) #输出第一个到倒数第二个字符之间的字符
print(str[0]) # 输出第一个字符
print(str[2:5]) # 输出第三个到第五个字符
print(str[2:]) # 输出从第三个字符开始的所有字符
print(str + 'Test') # 链接字符串

'''
    \用来转义字符，如果不想转义，在字符串前面加上r

'''
print('Ru\noob')
print(r'Ru\noob')


# 3.列表 - 列表中的元素可以改变，元素类型可不同
list = ['abc', 784, 2.32, 70.2]
list[0] = 1.0
list[1:3] = [1, 1, 1];
print(list[1:3]) # 从第二个元素开始输出到第四个元素
print(list * 2) # 连续输出两次列表
len(list)



# 4.元组 - 元素不可变，写在（）之中 元素类型可不同
tuple = (1,'haha',2.18)


# 5.集合 - 无序不重复元素的序列,重复的元素会被剔除
parame = {1,2,2,3,23,'ha'}
parame2 = set()

print(parame,parame2)

if ('ha' in parame ):
    print("yes")
else:
    print("no")

# 可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a - b) # 差集
print(a | b) # 并集
print(a & b) # 交集
print(a ^ b) # 不同时存在的元素


# 6.字典
dict = {}
dict['one'] = "1"
dict[2] = "2" # 键为2
print(dict.values())
print(dict.keys())
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]) # 直接从键值对序列中构造字典


# 7.数据类型转换








