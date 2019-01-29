import math

#自定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-998))

#空函数
def nop():
    pass

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle);
    ny = y + step * math.sin(angle);
    return nx, ny;

#通过函数获取返回值
x, y = move(100, 100, 60, math.pi/6)
print(x,y);

#返回值其实是一个tuple
r = move(100, 100, 60, math.pi/6)
print(r);