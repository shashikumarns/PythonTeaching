# dol
# key is normal object (immutable objects)

#                0  1  2
dol = {        
       'RN1' : [10,11,12],
       'NAME': ['ajay','ram','sham'],
       'PAN' : ['p123','p124','p125']
}

#       k        v

# dol_object['key'][index]

print(dol)
print(dol['NAME'])
print(dol['NAME'][2])
dol.pop('PAN')
print(dol)

# adhar : ['A123','B123','C123']

dol['adhar'] =['A123','B123','C123']

print(dol)

"""
adhar
C123  ==> S123
"""

dol['adhar'][2] = 'S123'
print(dol)


dol = {        
       'RN1' : [10,11,12],
       'NAME': ['ajay','ram','sham'],
       'PAN' : ['p123','p124','p125']
}


dol['PAN'][2] = 'P128'
print(dol)

#remove P124
print(dol['PAN'][1])
print(dol['PAN'])
dol['PAN'].pop(1)
print(dol)

dol1= {
'RN' : [10,11,10,12,10,11,12,20],
'NAME': ['a','b','c','d'],
'PAN' : ['p123','p124','p125']
}


print(dol1)
print(dol1['RN'].count(11))
#dol1['RN'].remove(10)
print(dol1)


dol1['RN'].remove(10)
print(dol1)


print("**********")


dol1= {
'RN' : [10,11,10,12,10,11,12,20],
'NAME': ['a','b','c','d'],
'PAN' : ['p123','p124','p125']
}


for i in dol1:
    print(i,dol1[i])
    if i == 'RN':
        for j in range(0,len(dol1[i])-2):
            print(i,j, dol1[i])
            print('a')
            if dol1[i].count(10) > 0:
                dol1[i].remove(10)
                print(dol1[i])

print(dol1)
print("**********")

dol2= {
'RN' : [10,11,10],
'NAME': ['a','b','c'],
'PAN' : ['p123','p124','p125']
}

for i in dol2:
    #print(i, dol2[i])
    print(i)
    for j in dol2[i]:
        print('\t', j)

"""
RN
    10
    11
    10
NAME
    a
    b
    c
PAN
    p123
    p124
    p125
"""


































