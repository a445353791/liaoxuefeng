#map方法使用
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

#把一个list转成str
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

