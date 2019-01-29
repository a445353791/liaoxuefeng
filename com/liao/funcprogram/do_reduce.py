# reduce把一个函数作用在一个序列[]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素进行累积计算
from functools import reduce


def add(x, y):
    return x + y


# 累加
res = reduce(add, [1, 3, 5, 7, 9])
print(res)


# 将数组转成整数
def fn(x, y):
    return x * 10 + y


res = reduce(fn, [1, 3, 5, 7, 9])
print(res)

# 将str转为int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


res = reduce(fn, map(char2num, '2133412'))
print(res)


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('1231'))
