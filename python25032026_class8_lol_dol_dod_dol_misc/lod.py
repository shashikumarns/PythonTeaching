#LOD ==> List of Dictonary

#        k  v   k   v     k   v   k   v
lod = [{'a':'b','c':'d'},{'x':'y','m':'j'}]
#      --------0-------   -------1-------

#lod_object[index][key]

print(lod)
print(lod[0])
print(lod[0]['c'])
print(type(lod))
print(type(lod[0]))
#print(lod.keys())
print(lod[0].keys())
print(lod[1].keys())

#remove 'a':'b'

lod[0].pop('a')
print(lod)

##important
#1:2
d = {2:3,4:5}
d[1]=2
print(d)

#1:2
lod[0][1] = 2
print(lod)
print("**********")
lod = [{'a':'b','c':'d'},{'x':'y','m':'j'}]

for i in lod:
    print(i, type(i)) #{'a':'b','c':'d'}
    for j in i:
        print(j)  #a, c

print("**********")
i = {'a':'b', 'c':'d'}
j='c'
print(i[j]) #d


print("**********")
lod = [{'a':'b','c':'d'},{'x':'y','m':'j'}]
""""
a b
c d
x y
m j
"""

for i in lod:
    print(i)
    for j in i:
        #print(j, j.values())
        print(j , i[j])

print("**********")

lod3 = [{'a':'b','c':'d','e':{1:2,3:4,5:[3,4,5]}},{'x':'y','m':'j'}]

print(lod3)
print(lod3[0]['e'])
print(lod3[0]['e'][3])
print(lod3[0]['e'][5])
print(lod3[0]['e'][5][1])


