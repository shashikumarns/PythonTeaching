# indexing ==> only one index can be passed in the indexing
# nly one character as a output


inp = "Ajay Kumar"
#      0123456789  => +ve index
#     10987654321  => -ve index
print(inp[3])  #y
print("*********")
print(inp[-3])  #m
print("*********")
#print(inp[10])  # string index out of range
print("*********")
print(inp[-10])  #A
print("*********")
print(inp[10-7])  #y
print("*********")
print(inp[-10+5])  #K