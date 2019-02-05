class Student(object):
    pass


#给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score

#给class绑定后，所有对象均可使用
s = Student()
s.set_score(50)
print(s.score)

#限制实例属性使用__slots__
class Student(object):
    __slots__ = ('name','age')  #这个Student类只能扩展'name'和'age'属性了


#但是，__slots__中定义的属性对其继承的子类是不起作用的。
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 999;
print(g.score)

