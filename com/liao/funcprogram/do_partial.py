#偏函数
print(int('12345'))

#n进制转换
print(int('12345',base=8))

#functools.partial帮我们建立一个偏函数,不需要我们自定义
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))
