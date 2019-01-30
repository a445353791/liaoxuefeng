#括号中的object表示该类是从哪个类继承下来的
class Student(object):
    #注意，__init__第一个参数永远是self，
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

brat = Student('Bart Simpson1',59)
print(brat.name)
brat.print_score()
print(brat.get_grade())