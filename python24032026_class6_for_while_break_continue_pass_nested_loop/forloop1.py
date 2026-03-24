data = {}
if 'count' not in data:
    data['count']=1 #{'count':1}
else:
    data['count']=data['count']+1
if 'count' in data:
    data['count']=1
else:
    data['count']=data['count']+1 #{'count':2}

print(data) #{'count':1}

data = [11,22,11,44,22,11,22]

#out = [11,22,44]
#print(list(set(data)))
out = []
for i in data:
    if i not in out:
        out.append(i)
print(out)

print("**************")

data1 = [11,22,33,44]
data2 = [66,33,44,'a',11,88]

#common = [33,44]
common = []
for i in data1:
    if i not in data2:
        common.append(i)
print(common)

print("**************")

common = []
for i in data1:
    if i in data2:
        common.append(i)
print(common)

print("**************")

#create a list of 4 int objects from keyboard:

#out [1,2,3,4]
out=[]
"""
for i in range(4):
    inp = input('enter a int number:')
    print(type(inp))
    if isinstance(int(inp),int):
        out.append(int(inp))
print(out)
"""
"""
for i in range(4):
    inp = input('enter a int number:')
    print(type(inp))
    if inp.isdigit():
        out.append(int(inp))
print(out)
"""

# While Loop : condition check (no start or end)
# for loop : we define start point, end point


out = []

while (len(out)!=4):
    inp = input('enter int number')
    if inp.isdigit():
        out.append(int(inp))
        break
print(out)






















