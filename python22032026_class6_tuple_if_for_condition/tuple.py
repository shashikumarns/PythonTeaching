# Tuple() methods

t1 = (1,2,3,4,5, 5,2)

#count()

print(t1.count(3)) #1
print(t1.count(5)) #2

t2 = (0,1,(2,3),(2,3),[3,4],'get',56.8)
print(t2.count((2,3))) #2
print(t2.count(2)) #0

#index()

print(t1.index(3)) #2
print(t1.index(2)) #1
print(t1.index(2,2)) #6

t3 = (22,33,44)
o = (22,33,44,55)
o = list(t3)
o.append(55)
print(o)
print(tuple(o))

t4 = (1,2,1,2,1,2,1,2)
op = (1,2)
print(tuple(set(t4)))










