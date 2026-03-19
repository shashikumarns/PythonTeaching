data = []
print(data)

data = [10,20,30,40,30,10]
print(data)

print(data[2])

data = [10,20,30,40,30,10,"10,20",[100,500]]
#print(data[-1][2])
print(data[-1][1])
print(type(data[-1][1]))
#print(data[9])
print(data[::-1]) # reverse

d1 = ['abc','def','ghi']
print(d1[::-1])

# ['ihg', 'fed', 'cba']

print(d1[::-1][::-1])

print(d1[::-1][0]) #ghi
## doing multiple steps in single expression one line using indexing and slicing



a = [10,20]
b = [30,40]

#c= [10,20,30,40]
#c = [[10,20,30,40]]
#c = [[10,20],[30,40]]

print(a+b)

c= [a+b]
print(c)

c = [a] + [b]
print(c)

l = [10,20]


o = [10,20,10,20,10,20,10,20,10,20]
o = [[10,20],[10,20],[10,20],[10,20],[10,20]]
print(l*5)
print([l]*5)


l1 = [10,20,30,40,30,10]

#40 to 50

l1[3]=50
print(l1)



s1 ="abcd"
s1[2]='i'
#print(s1) # not mutable






