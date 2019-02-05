#通过__getattr()方法，动态返回一个属性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda:25 #返回函数

#当调用不存在的属性时，python解释器会试图调用__getattr(self,'score')来尝试获得属性
s = Student()
print(s.name)
print(s.score)
print(s.age())

#注意，只有在没有属性的情况下，才调用__getattr__，对已有的属性，比如name不会在__getattr__中查找


#用__getattr__实现链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)