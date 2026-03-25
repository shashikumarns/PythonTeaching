data = ([11,333],[22,55],[33,66,77])

#0 => [11,333]==>[1,2,3]

#data[0] = [1,2,3]
print(data)


# 22 => 78
data[1][0] = 78
print(data)

#0 => [11,333]==>[1,2,3]
l = list(data)
print(l)
l[0] = [1,2,3]
print(l)
print(tuple(l))

print(data)




"""
*
**
***
****
*****

*****
****
***
**
*
"""

for i in range(6):
    print(i*'*')

for i in range(6,0,-1):
    print(i*'*')

for i in range(6):
    print('*' +i*' '+'*')

for i in range(6,0,-1):
    print('*' +i*' '+'*')


for i in range(6,0,-1):
    print(' '* (i-1) +'*')
















