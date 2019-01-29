n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10: #当n=11时，条件满足，执行break语句
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

while True:
    print("die circle ctrl+c exit")