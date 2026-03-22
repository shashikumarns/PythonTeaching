#max(iterable) and min(iterable) and sum(iterable)
# max(iterable) - to get max object from the iterbale argument
# min(iterable) - to get min object from the iterbale argument
# sum(iterable) - to get sum of all object from the iterbale argument

inp = [2,5,8,10]
print(inp)
print(max(inp))
print(min(inp))
print(sum(inp))


# char = ascii values
#0=48
#A=65
#a=97

i1 = "aaa"
i2 = "AAA"
print(max(i1,i2))

i1 = "abcd"
i2 = "abbc"
print(max(i1,i2))

i1 = "aAz"
i2 = "z"
print(max(i1,i2)) #z Compare char by char


i1 = "aef"
i2 = "ai"
print(max(i1,i2)) #ai Compare char by char


i1 ="23"
i2 ="100"
print(max(i1,i2))

i1 ="100"
i2 ="9"
print(max(i1,i2)) #9

i1="100"
#i2 =100
print(max(i1,i2))   #error

inp = ['abb','ab','abd','aba','am']
print(max(inp)) #am

#inp = ['abb',12,12.5] # int and str not compared
print(max(inp)) #error

