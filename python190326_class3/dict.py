data = {'RN1':'ajay','RN2':'vijay'}

##print(data[0]) #error
print(data['RN1'])

data = {'RN1':'ajay','RN2':'vijay','RN1':"sham","RN3":"abcd","rn5":"cdef"}

print(data['RN1'])

print(data)

#print(data[::-1]) #error

print(data.keys())

data['RN2'] = "xyz"
print(data)

d = {12:45, True:12.4, None:False, "abc":[1,2,3], 12:(1,2,3)}
print(d)

d1 = {1:2,3:4}
d2 = {5:6}
#print(d1*2)
#print(d1+d2)

data['RN6']='lmnop'
print(data)