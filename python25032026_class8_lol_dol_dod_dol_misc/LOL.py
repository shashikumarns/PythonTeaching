# LOL ==> List of List

#        0   1  2    0  1  2    0  1
data = [[10,20,30],[40,50,60],[30,80]]
#       ----0-----  ----1----   --2--
# LOL_OBJECT[index][index]


print(data)
print(data[1])
print(data[1][2])

#['a,'b','c']

data.append(['a','b','c'])
print(data)

# [1,2,3]
data[1] = [1,2,3]

print(data)

data[0][0] = 'a'
print(data)

c = data[2].count(80)
print(c)

print("********")
data = [[10,20,30],[40,50,60],[30,80]]
#out = [10,20,30,40,50,60,30,80]
out = []
for i in range(len(data)):
    print(data[i])
    for j in data[i]:
        print(j, data[i])
        out.append(j)

print(out)
print("********")

data = [[10,20,30],[40,50,60],[30,80]]
data[2].pop(1)
print(data)
data[1].remove(50)
print(data)
data[-1].append(['a'])
print(data)
#                                 0
#   0  1    2     0   1    0      1
#[[10, 20, 30], [40, 60], [30, ['a']]]
# ----0-----  ----1----      --2--
print(data[2][1][0])


data = [
["EN","NAME","SALARY"],
[123,"RAMESH",5000],
[124,"AJAY",10000],
[125,"KIRAN",3000],
[126,"SURESH",1000],
]

print(data)
print(data[1][1])
print(data[3][1])
print(data[3])
data[3][2] = 2500
print(data)

print("********")

for row in data: #["EN","NAME","SALARY"]
    print(row, type(row)) 
    for col in row: #EN NAME SALARY
        print(col)
 
print("********")

data = [
["EN","NAME","SALARY"],
[123,"RAMESH",5000],
[124,"AJAY",10000],
[125,"KIRAN",3000],
[126,"SURESH",1000],
]



# fetch salry less than 3000 print their names

for row in data[1:]: #["EN","NAME","SALARY"]
    print(row, type(row)) 
    if row[2] < 3000:
        print(row[1])





















