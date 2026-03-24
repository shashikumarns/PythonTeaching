data = ['a',10,'b',20,'c',30]
#        0  1   2  3   4   5

#data1 = ['a','b','c']
#data2 = [10,20,30]

data1 =[]
data2 = []

for i in range(len(data)):
    print(i)
    if i%2 == 0:
        data1.append(data[i])
    else:
        data2.append(data[i])
        
        
print(data1)
print(data2)

print("*************")
#Break

data  =  [10,11,30,40,11,22,55,11]
for i in data:
    if i == 11:
        print('found')
     
'''       
found
found
found        
'''       
print("*************")       
for i in data:
    if i == 11:
        print('found')
        break
print("*************")       
for i in data:
    if i == 11:
        print('found')
    break      
print("*************")        
# Important -> Membership operator:

#out = OBJECT in ITERABLE
#out = OBJECT not in ITERABLE

# if the object is member in the iterable it comes out
print("*************")
##data  =  [10,11,30,40,11,22,55,11]
data  =  [10,30,40,1,22,55,1]

if 11 in data:
    print("found it")
else:
    print("not found it")
print("*************")
data  =  [10,'a',40,1,22,55,1]
if 'a' in data:
    print("found")
else:
    print("not found")
print("*************")
data = {'RN1':'ajay','RN2':'kiran'}

if 'RN1' in data:
    print('key found')
else:
    print('key not found')

print("*************")

if 'RN5' in data:
    print('key found')
else:
    print('key not found')
    
print("*************")
if 'RN1' in data.keys():
    print('key found')
else:
    print('key not found')


print("*************")


if 'ajay' in data.values():
    print('value found')
else:
    print('values found')
    
print("*************")
    
data  =  [10,'a',40,'11',22,55,1]

for i in data:
    print(i, type(i))
    if i == 11:
        print('found')     
print("*************") 


data = [11,22,33]
i=4
if i not in data:
    data.append(i) #[11,22,33,4]
if i not in data:
    data.append(i) #[11,22,33,4]
if i not in data:
    data.append(i)  #[11,22,33,4]
if i not in data:
    data.append(i) #[11,22,33,4]
print(data)


data1 = [11,22]

if 1 not in data1:
    data1.append(1) #[11,22,1]
elif 2 not in data1:
    data1.append(2) #[11,22,33,4]
elif 5 not in data1:
    data1.append(5)  #[11,22,33,4]
elif 6 not in data1:
    data1.append(6) #[11,22,33,4]
print(data1)

data1 = [11,22]
if 1 in data1:
    data1.append(1) #[11,22,1]
elif 22 not in data1:
    data1.append(2) #[11,22,33,4]
elif 55 not in data1:
    data1.append(5)  #[11,22,33,4]
elif 6 not in data1:
    data1.append(6) #[11,22,33,4]
else:
    data1.append(5)
print(data1) #[11, 22, 5]














        
        
        