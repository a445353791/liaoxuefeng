#返回函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#如果不需要立即求和，可以不返回求和的结果，而是返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#调用lazy_sum()时，返回并不是求和的结果，而是求和函数
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())

#当lazy_sum返回函数sum时，相关参数和变量都保存在函数中，这种称为"闭包"的程序结构具有极大的威力
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1,f2,f3 = count()
#全部都是9,原因在于返回的函数引用变量i,但它并非立即执行，等到3个函数都返回了，
#它们的引用i变成了3
#返回闭包是要牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
print("f1:"+str(f1())+" f2:"+str(f2())+" f3:"+str(f3()))

#解决方式：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print("f1:"+str(f1())+" f2:"+str(f2())+" f3:"+str(f3()))