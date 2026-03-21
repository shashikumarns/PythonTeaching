# SET MEthods:

data = {11,22,33,11,22}
print(data) #{33,11,22}

data.add(50)
print(data) #{33, 50, 11, 22}

data.add(22)
print(data) #{33, 50, 11, 22}

data.add('abcd') #{33, 11, 50, 'abcd', 22}
print(data)

#data.update(iterable)
data = {11,22,33,11,22}
data.update('abcd')
print(data) # {33, 11, 'a', 'c', 22, 'b', 'd'}


data.remove(22)
print(data) #{33, 11, 'a', 'c', 22, 'b', 'd'}

data2 =data.copy()
print(data2) #{33, 11, 'a', 'c', 22, 'b', 'd'}

data2 =set()
print(set)

data2.update('abcd')
print(data2) #{'d', 'b', 'a', 'c'}
data2.add('abcd')
print(data2) #{'d', 'b', 'a', 'c'}


data2 = {'d', 'b', 'a', 'c'}
data2.clear()
print(data2) #set()


data1 = {11,22,33,44}
data2 = {55,33,22,66}
out = data1.union(data2)
print(out) # {33, 66, 11, 44, 22, 55}


data1 = {11,22,33,44}
data2 = {55,33,22,66}
out = data1.intersection(data2)
print(out) # {33,22}

data1 = {1,2,3,4,5}
data2 = {1,2}

print(data2.issubset(data1)) #true

data1 = {11,22,33,44}
data2 = {55,33,22,66}
out =data1.difference(data2)
print(out) # {11,44}


data1 = {11,22,33,44}
data2 = {55,33,22,66}
out =data2.difference(data1)
print(out) # {55,66}

data1 = {11,22,33,44}
data2 = {55,33,22,66}
out =data2.symmetric_difference(data1)
print(out) # {55,66, 11, 44}


# add() -> object, update() -> iterable, remove, clear, copy

# union, intersection, issubset, difference, symmetric_difference

















