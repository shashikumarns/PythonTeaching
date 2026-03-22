# For Loops

"""
syntax:
for var_name in ITERABLE_OBJECT:
    statement
"""


data = [100,200,300]
for i in data:
    print(data)

"""
[100, 200, 300]
[100, 200, 300]
[100, 200, 300]
"""

print("********")

data = [100,200,300]
for i in data:
    print(i)
"""
100
200
300
"""
print("********")

# 100#200#300#

data = [100,200,300]
for i in data:
    print(i, end='#')
print('\n')
print("********")

data = [100,200,300.0,'a',set()]

for i in data:
   if isinstance(i,int):
      print(i)
	  
print('done')

"""
100
200
done
"""

print("********")

data = {'RN1' : 'ajay kumar', 'RN2' : 'Karthik'}

# i am key - RN1 and its value is ajay kumar

for i in data:
    #print(i)
    #print(data)
    #print(data[i])
    print('i am the key - ',i,' and its value is ',data[i])
"""
i am the key -  RN1  and its value is  ajay kumar
i am the key -  RN2  and its value is  Karthik
"""

print("********")

# key and value swaping

data = {'RN1' : 'ajay kumar', 'RN2' : 'Karthik'}

#out = { 'ajay kumar' :  'RN1' , 'Karthik' : 'RN2'  }
out = {}
for i in data:
	#out{data[i],i} # invalid syntax
    print(i)
    print(data[i])
    print(out)
    out[data[i]] = i
    print(out)
#print(out)

#{'ajay kumar': 'RN1', 'Karthik': 'RN2'}


print("********")

inp = "google.com"

# how many times each char is repeated and show in dictorany

for i in inp:
    print(i)

print(inp.count('g'))

# clue - how unique chars
inp1 = set(inp)
print(inp1)
out = {}
for i in inp1:
    print(i, inp.count(i))
    out[i] = inp.count(i)
print(out)

print(max(out))

print("********")

inp = "google.com"

for i in set(inp):
    out[i] = inp.count(i)
print(out)


print("********")

data1 = [11,22,33,44,55,66]

data2 = [10,20,30,40,50]

#out = {11:10,22:20,33:30,44:40}
out ={}
"""
for i in data1:
    for j in data2:
        out[data1[i]] = data2[j]
print(out)
# index out of range
"""

"""
for i in data1, data2:
    print(i)
    print(data1[i])
    print(data2[i])
    #out[data1[i]] = data2[i]
print(out)

"""

len1 = len(data1)
print(len1)
"""
for i in range(len1):
    print(i)
    print(data1[i])
    print(data2[i])
    out[data1[i]] = data2[i]

print(out)
"""
#{11: 10, 22: 20, 33: 30, 44: 40}

data1 = [11,22,33,44,55,66]

data2 = [10,20,30,40,50]

len1 = len(data1)
len2 = len(data2)

print(len1) #6
print(len2) #5
max_len = max(len1,len2) #6

for i in range(max_len):
    if i < len2:
        print(data1[i])
        print(data2[i])
        out[data1[i]] = data2[i]
    else:
        out[data1[i]] = None

print(out)

#{11: 10, 22: 20, 33: 30, 44: 40,55:50,66:None}