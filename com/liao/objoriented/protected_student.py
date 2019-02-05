class Student(object):

    #实例的变量名如果以__开头，就变成了一个私有变量，只有内部能访问，外部不能访问
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson',59)

#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(bart._Student__name)

#python本身没有任何机制阻止你干坏事,一切全靠自觉



