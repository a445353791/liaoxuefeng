#如果要获得一个对象所有属性和方法，可以使用dir()函数
print(dir('ABC'))
print(len('ABC'))
print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
#测试obj对象的属性
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
setattr(obj,'y',19) #设置一个属性
print(getattr(obj,'y')) #获取一个属性

#如果试图取不存在的属性，会抛异常，用默认值处理
print(getattr(obj,'z',404))

#在写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性,
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。