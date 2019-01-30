class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
cat = Cat()
dog.run()
cat.run()

print(isinstance(cat,Cat))

#多态例子
#对于python这样的动态语言来说，不一定要传入一个Animal类型，只要保证对象又一个run()方法就好
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
