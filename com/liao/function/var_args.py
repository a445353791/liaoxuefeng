#位置参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5));

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

#注意，默认参数是一个变量[]，所以每次都要往变量中加end
print(add_end())
print(add_end())


#可变参数传参
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
print(calc())


