# dict迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)

# 判断对象是否可迭代
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# 有下标的循环:enumerate
for i,value in enumerate(['A','B','C']):
    print(i,value)