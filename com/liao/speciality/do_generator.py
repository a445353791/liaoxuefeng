# 生成器：使用时再推断出后续元素，不必创建完整列表，从而节省空间
g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(8)