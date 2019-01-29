#生成list
print(list(range(1,11)))

L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

#一行用循环直接生成list
L = [ x*x for x in range(1,11) if x % 2 == 0]
print(L)

#列出当前目录下的所有文件和目录名
import os
L = [ d for d in os.listdir('.')]
print(L)

#循环两个变量
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)