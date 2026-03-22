# Range
"""
range(start_point, end_point, step_point)
by default step_point is +1
-3 -2 -1 0 1 2 3 4
"""
lst = []

for i in range(4): #0,1,2,3
    print(i)
    lst.append(i)

print(lst)

lst = []

for i in range(4,8): #4,5,6,7
    print(i)
    lst.append(i)

print(lst)

lst = []

for i in range(4,8,2): #4,6
    print(i)
    lst.append(i)

print(lst)

lst = []

for i in range(4,-8,2): #4,6 
    print(i)
    lst.append(i)

print(lst) # empty list

lst = []

for i in range(4,-8,-1): #4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7
    print(i)
    lst.append(i)

print(lst)

lst = []

for i in range(4,-8,-2): #4, 2, 0, -2, -4, -6
    print(i)
    lst.append(i)

print(lst)#[4, 2, 0, -2, -4, -6]



lst = []

for i in range(-8,-2): #-8, -7, -6, -5, -4, -3
    print(i)
    lst.append(i)

print(lst)#[-8, -7, -6, -5, -4, -3]




lst = []

for i in range(-8,2,2): #-8, -6, -4, -2, 0
    print(i)
    lst.append(i)

print(lst)#[-8, -6, -4, -2, 0]


data = ['bangalore','mysore','mangalore']
#out = ['mangalore','mysore','bangalore']
out = []
for i in data:
    print(i)
print("*****")
for i in range(len(data)):
    print(i)
print("*****")
for i in range(len(data),0,-1): #3,2,1
    print(i)
print("*****")
for i in range(len(data)-1,-1,-1): #2,1,0
    out.append(data[i])
    print(i)
print(out)
print("*****")
out=[]
for i in range(len(data)-1,-1,-1): #2,1,0
    out.insert(i,data[i])
    print(i)
print(out)


d = {'a':'b','c':'d'}
"""
l1 = ['a','c']
l2 = ['b','d']
"""
l1=[]
l2=[]

for i in d:
    print(i,d[i])
    l1.append(i)
    l2.append(d[i])
print(l1)
print(l2)


d = {'a':'b','c':'d'}
"""
l1 = ['a','b']
l2 = ['c','d']
"""
l1=[]
l2=[]

for i in d:
    print(i,d[i])
    l1.append(i)
    l1.append(d[i])
print(l1)


l2.append(l1[2])
l2.append(l1[3])
print(l2)

l1.pop()
l1.pop()
print(l1)



























