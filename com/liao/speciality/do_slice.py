L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#切片
print(L[0:3])
#第一个索引是0，省略
print(L[:3])
#倒切片
print(L[-3:])

#tuple也可以用切片操作，只是结果仍然是tuple
print((0, 1, 2, 3, 4, 5)[:3])