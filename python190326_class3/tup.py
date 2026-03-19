t = (10,'a',20,10.25,10,20,True,['a','b'])
print(t)
print(t[3])
print(t[::-1])
print(t[-1][0])
print(type(t[-1][0]))

#t[1] ='b' # error since not mutable
print(t)
t1 = (1,2,3)
print(t+t1)

print(t1*2)

data1 = (10,20)
data2 = (30,40)
data3 = data1+data2
print(data3)

t = ()
print(type(t))

t=('',None,'','')
print(t)