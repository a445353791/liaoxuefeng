import functools
#装饰器
def now():
    print('2015-3-25')
f = now
f();

#函数对象又一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        res = func(*args, **kw)
        print('call res %s():' % func.__name__)
        return res
    return wrapper

#把@log放到now()函数定义处相当于执行了语句：now=log(now)
@log
def now():
    print('2015-3-25')
now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

#三层效果: now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')


#__name__已经从原来的'now'变为'wrapper'
now = log('execute')(now)
print(now.__name__)

#解决方式
def now():
    print('2015-3-25')
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
now = log(now)
print(now.__name__)

