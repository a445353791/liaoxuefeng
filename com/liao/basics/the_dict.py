d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
d['Jack'] = 90
print(d['Jack'])

#检查key是否存在，用in
print('Bob' in d)

#get(key,'默认值')
print(d.get('Thomas'))
print(d.get('Thomas',88888))

#删除key 用pop(key)
print(d.pop('Bob'))
print(d)
