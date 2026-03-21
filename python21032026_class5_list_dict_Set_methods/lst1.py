# LIST

data = [10,20,30,'ajay','kumar']
print(data[3])

#print(data[6]) #index out of range


#out = [10,20,30,'AJAY','Kumar']

data[3]=data[3].upper()
data[4]=data[4].title()

print(data)

# append => inserts data element at the last index of list (RHS)

data = [10,20,30,'ajay','kumar']

data.append('abcd')

print(data) #[10, 20, 30, 'ajay', 'kumar', 'abcd']

##data.append('abcd','def') # only one arg allowed not more than one # error

data.append([1,2])
print(data)

lst = []
#[10,20]
lst.append(10)
lst.append(20)
print(lst)

#inser() -> to insert the object at any index/ position of the list
#list.insert(index,value)

lst.insert(1,30)
print(lst)


lst = [1,2,3,4,5,6]
lst.insert(2,54)
print(lst)

lst.insert(-2,54)
print(lst)

lst.insert(15,54) # by default it will insert at last incase if we provide invalid/not present index number which is +ve
print(lst)


lst.insert(-15,54) # by default it will insert at first incase if we provide invalid/not present index number which is -ve
print(lst)

data1 = [1,2,3]
data2 = [4,5,6]
#data3 = [1,2,3,4,5,6]
data3 = data1+data2
print(data3)
data5=[]
data5=data1.append(data2)
print(data1) # [1, 2, 3, [4, 5, 6]]
print(data5) # None

print(type(data5))

# remove() => removes the object from the list
# list.remove(object_name)

data = ['abcd','def','ghi','ijk']
data.remove('def')
print(data) #['abcd', 'ghi', 'ijk']

#data.remove('xyz')  #ValueError: list.remove(x): x not in list
print(data)

data11 = ['abcd','def','ghi','ijk','abcd']
data11.remove('abcd')
print(data11) #['def', 'ghi', 'ijk', 'abcd']

#data11.remove() # cannot be empty
# data11.remove('xyz') # incase some random value which is not present will give error
print(data11) #['def', 'ghi', 'ijk', 'abcd']


inp = ['abcd','def','ghi','ijk','abcd']
#data11.remove('abcd',2) #error only one args will be allowed
print(inp[-1])
inp.remove(inp[-1]) ## => decoded - data11.remove('abcd')
#inp.remove(inp[15]) # index out of range
print(inp) #['abcd','def','ghi','ijk']

#POP
#list.pop(index/position)

inp = ['abcd','def','ghi','ijk','abcd']
inp.pop(1)
print(inp) #['abcd', 'ghi', 'ijk', 'abcd']

inp = ['abcd','def','ghi','ijk','abcd']
inp.pop(-1)
print(inp)

inp = ['abcd','def','ghi','ijk','abcd']
inp.pop() # by default the index is -1 so it will remove always last index value
print(inp)

#inp.pop(15) # index out of range error
print(inp) 

inp.clear()
print(inp) #[]  # to rmeove all the elemenbts


"""
#Diff b/w the remove and pop method in list
remove => remove based on object
data.remove(object)

pop => remove based on position or index
by default -1 if empty
data.pop() or data.pop(1)
"""


data = ['ajay','ramesh','kiran','sachin']
#data= ['ajay','ramesh']
data.pop(-1)
data.pop()
print(data)



data = ['ajay','ramesh','kiran','sachin']
#out = ['ajay','ramesh','kiran','sachin','ajay']

data.append(data[0])
print(data)

data.remove('ajay')
print(data)

data.pop(0)
print(data)

data1 = ['ajay','ramesh','kiran','sachin']

out=data1.count('kiran')
print(out) #1

data1 = ['ajay','ramesh','kiran','sachin','kiran','kiran']


out=data1.count('kiran')
print(out) #3


out=data1.count('xyz')
print(out) #0

out = data1.index('ramesh')
print(out)


#list.extend(iterable)  # replacement for concateination +

data = [1,2,3]
data2 = [4,5]
#out =[1,2,3,4,5]
data.extend(data2)
print(data)

s = "abcd"
data = []
data.extend(s)
print(data) #['a', 'b', 'c', 'd']

t = (1,2,3,4,5,5,6)
d = ['abc']
d.extend(t)
print(d)

dt = {1:2,2:3,3:4,5:6}
lst = [1,2,3,4]
lst.extend(dt)
print(lst) #[1, 2, 3, 4, 1, 2, 3, 5]

'''
#diff b/w append and extend

lst.append(object)
# takes only one object
# adds only one object at the last

lst.extend(iterable)
# takes the iterable object
# extend adds multiple iterable object
'''

data = [10,20]
data.clear()
print(data) #[]

data1 =[1,2,3]
print(data1)
#data2 = [1,2,3]
data2 = data1.copy()
print(data2)

# Visualizer of python code step by step
# https://www.codechef.com/python-online-compiler
# https://cscircles.cemc.uwaterloo.ca/visualize



# append(), insert(), remove(), copy(), clear(), pop(), extend()



































