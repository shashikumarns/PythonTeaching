# Slicing
#Syntax sting_object[start_range (x):end_range (y):step_range]
# incase if we need multiple char or substr then we usually go for slicing method
# if start range is not provided by default it is zero
# it cannot read from right to left
# whenever end range is not defined then value for end range is length of the string

 #           x  y             
inp = "Ajay Kumar"
#      0123456789  => +ve index
#     10987654321  => -ve index

print(inp[2:5]+":") #ay 
print("*******")

print(inp[1:8]) #jay Kum
print("*******")

print(inp[:8])
print("*******")

print(inp[-1:-4]) # empty not value
print("*******")

print(inp[-4:-1]) # uma
print("*******")

print(inp[-4:])  #umar
print("*******")

 #              y            x
inp = "Ajay Kumar"
#      0123456789  => +ve index
#     10987654321  => -ve index


print(inp[2:7]) #ay ku
print("*******")

print(inp[-8:-3])
print("*******")

print(inp[:-1])
print("*******")


print(inp[1:-1])
print("*******")


print(inp[:30]+":")
print("*******")


print(inp[30:-1])
print("*******")




















