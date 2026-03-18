# Slicing
#Syntax sting_object[start_range (x):end_range (y):step_range]
# incase if we need multiple char or substr then we usually go for slicing method
# if start range is not provided by default it is zero
# it cannot read from right to left
# whenever end range is not defined then value for end range is length of the string
# by default step is 1
 #     x       y             
inp = "Ajay Kumar"
#      0123456789  => +ve index
#     10987654321  => -ve index

print(inp[0:8])
print("******")

print(inp[0:8:2])  #0,2,4,6,8 #Aa u
print("******")

print(inp[2:8:1])  #2,3,4,5,6,7,8
print("******")

#print(inp[2:8:0]) # step index cannot be zero error
print("******")

print(inp[::2]) #0,2,4,6,8 #Aa ua
print("******")



print(inp[3:8:50]) #3,53, 106 #a 
print("******")



print(inp[8:2:1]) # empty string
print("******")

print(inp[5::-1])  #5,4,3,2,1,0
print("******")

a= "america"
#reverse string
print(a[::-1])
print(a[8::-1])


s = "Python"
reversed_s = "".join(reversed(s))
print(reversed_s)

"""
Step index: +ve
 * resutl will not be reverse
  * if start index not given
  assume start = LHS (0) index
  * if end index not given
  assume end = RHS(size of string)




Step index: -ve
 * resutl will  reverse
  * if start index not given
  assume start = RHS (size of string) index
  * if end index not given
  assume end = LHS(0)
"""

p = "Ajay Kumar"
print(p[::1]) #Ajay Kumar
print(p[:]) #Ajay Kumar
print(p[::]) #Ajay Kumar
print(p[::-1]) # reverse of string
print(p[:-1])  #Ajay Kuma








































































