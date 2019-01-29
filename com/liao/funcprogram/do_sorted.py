#sorted()对list排序
print(sorted([36,5,-12,9,-21]))

#接收一个key函数来实现自定义排序
print(sorted([36,5,-12,9,-21],key=abs))

list = [36, 5, -12, 9, -21]
keys = [36, 5,  12, 9,  21]

#去除大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#反向
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))