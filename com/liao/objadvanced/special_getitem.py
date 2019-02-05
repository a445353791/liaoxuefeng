#实现__getitem__方法后，就可以将一个类当list来使用
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L

f = Fib()
print(f[10])
print(f[40:50])

#与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值，最后还有一个__delitem__()方法，用于删除某个元素