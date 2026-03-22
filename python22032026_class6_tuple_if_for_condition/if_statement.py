# Conditional Statement:
# if Statements

# 4 space => good practice
# 1 tab 
# 2 spaces

"""
if expression:
   statemnts
"""

# Exprression is a python statemnt/condition which should some value

"""
To check expression in editor mode
D:\python22032026_class6>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print('hello')
hello
>>> x=[1,2,3]
>>> x.pop()
3
>>> print(x)
[1, 2]
>>> 100>110
False
>>> exit()
"""

x = 1
if x:
   print('i am inside')

print('i am outside')
print("****")
if (x<50):
   print('i am inside')

print('i am outside')

print("****")
if (x>=50):
   print('i am inside')

print('i am outside')



# if condition/ expression output is true => then it enters inside the if clause
# if condition/ expression output is false => then it goes outside the if clause
print("****")
inp = []
if len(inp) == 0:
   print('i am inside')
print(inp)

print("****")
inp = [10] #10,20
if len(inp) != 0:
   print('i am inside')
   #inp.extend([10,20]) #[10,10,20]
   inp.append([10,20]) #[10,[10,20]]
print(inp)

print("****")
inp = "abbaca"
if inp[0] == inp[-1]:
    print('matching')
else:
    print('not matching')

print('i am out')


print("****")
#inp = "abbaca"
inp = input("enter the value:")
if inp[0] == inp[-1]:
    print('matching')
else:
    print('not matching')

print('i am out')

print("****")

inp = []

if len(inp) == 0:
   inp.append(10) #10
if len(inp) == 0:
   inp.append(30)
if len(inp) == 2:   
   inp.pop()
else:
   inp.append(5) #10,5
print(len(inp)) #2
print(inp) #[10,5]



print("****")


inp = []
if inp:
    print('i am true')
else:
    print('i am false')


#Elseif ==> elif
"""
if exp1:
    stat1
elif exp2:
    stat2
elif exp3:
    stat3
else:
    stat5
stat6
"""
print("****")

inp = []

if len(inp) == 0:
   inp.append(10) #10
elif len(inp) == 0:
   inp.append(30)
elif len(inp) == 2:   
   inp.pop()
else:
   inp.append(5) 
print(len(inp)) #1
print(inp) #[10]


# top to bottom first true condition it will execte which is true and will stop after that and will not execute further statemnts

print("****")

inp = []

if len(inp) == 0:
   inp.append(10) #10
   #exit()
elif len(inp) == 0:
   inp.append(30)
elif len(inp) == 2:   
   inp.pop()
else:
   inp.append(5) 
print(len(inp)) #1
print(inp) #[10]

# exit() -> fuction to exit from that point or line fromt he entier code

# if or elif or else ==> only exit() can be used and cannot use break() or skip() which will be used in the loops
 
print("***** if check *****")

inp = [10,20,30]
if isinstance(inp,str):
   print('it is a string')
if isinstance(inp,list):
   print('it is a list')
if isinstance(inp,tuple):
   print('it is a tuple')
if isinstance(inp,dict):
   print('it is a dict')
if isinstance(inp,bool):
   print('it is a bool')
else:
   print("don't know")
print("outside")
"""
it is a list
don't know
outside
"""
print("****")




print("***** elif *****")

inp = [10,20,30]
if isinstance(inp,str):
   print('it is a string')
elif isinstance(inp,list):
   print('it is a list')
elif isinstance(inp,tuple):
   print('it is a tuple')
elif isinstance(inp,dict):
   print('it is a dict')
elif isinstance(inp,bool):
   print('it is a bool')
else:
   print("don't know")
print("outside")
"""
it is a list
outside
"""
print("****")




































