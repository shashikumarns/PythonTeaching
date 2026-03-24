# Nested Loop: Loop inside a loop

x = [10,20,30]
y =['a','b','c']

for i in x:
    print(i)
    for j in y:
        print(j)
    print('dummy')
print('done')

print("**********")

x = [10,20,30]
y =['a','b','c']

for i in x:
    print(i)
    if i not in y:
        print(y)
    print('dummy')
print('done')

print("**********")
x = [10,20,30]
y =['a','b','c']
for i in x:
    for j in y:
        print(i,j)
        print('dummy1')
    break
    print('dummy2')
print('done')


print("**********")
print("**********")
x = [10,20,30]
y =['a','b','c']
for i in x:
    for j in y:
        print(i,j)
        print('dummy1')
    print('dummy2')
print('done')


print("**********")

for i in range(5):
    print(i)
    break # it comes out of loop and ends the loop
    print('dummy1')
    print('dummy2')
print('done')

print("**********")
"""
**********
0
done
**********

"""

print("**********")

for i in range(5):
    print(i)
    continue # it skips/ignores below code and continues to next iteration
    print('dummy1')
    print('dummy2')
print('done')

print("**********")

"""


**********
0
1
2
3
4
done
**********

"""

print("**********")

for i in range(5):
    print(i)
    pass # it ignoreance statement
    print('dummy1')
    print('dummy2')
print('done')

print("**********")

"""
**********
0
dummy1
dummy2
1
dummy1
dummy2
2
dummy1
dummy2
3
dummy1
dummy2
4
dummy1
dummy2
done
**********
"""


x = [1,2,3]
if 1 in x:
    print('found')
    pass

print("**********")

for i in range(5):
    print(i)
    if i%2 == 0:
        break # it ignoreance statement
        print('dummy1')
        print('dummy2')
print('done')

print("**********")

print("**********")

for i in range(5):
    print(i)
    if i%2 == 0:
        continue # it avoids next statement in this if condition body
        print('dummy1')
        print('dummy2')
print('done')

print("**********")

"""
**********
0
1
2
3
4
done
**********
"""

print("**********")

for i in range(5):
    print(i)
    if i%2 == 0:
        pass # it ignoreance statement
        print('dummy1')
        print('dummy2')
print('done')

print("**********")