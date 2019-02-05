#__str__的使用
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__ #用于指定调试服务

#__str__能使print打印指定str
print(Student('Michael'))

