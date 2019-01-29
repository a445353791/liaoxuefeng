def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)


#命名关键字
#与关键字**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

#命名关键字参数缺省值
def person(name,age,*,city="Beijing",job):
    print(name,age,city,job)
person('Jack', 24, job='Engineer')

#对于任意函数，都可以通过类似func(*args,**kw)的形式调用它，无论它的参数是如何定义的。
