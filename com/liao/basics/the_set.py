# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3]);
print(s);

# 添加与移除
s.add(4);
s.remove(3);
print(s);

# 排序
a = ['c', 'b', 'a'];
a.sort();
print(a);

# 替换
a = 'abc'
print(a.replace('a', 'A'));

#replace实际是提供一个新的str，之前的str并没有改变
a = 'abc';
b = a.replace('a', 'A');
print(a);
print(b);