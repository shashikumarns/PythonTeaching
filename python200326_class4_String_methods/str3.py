#STRIP

# method to remove unwanted leading or trailing white spaces \n, \t, empty spaces

inp = "\n\t     ajay kumar     \n\t"
print("**************")
print(inp)
print("**************")
out = inp.strip()
print(out)

# lstrip => remove leading spaces on left side of the string
inp = "\n\t      ajay kumar     \n\t"
print("**************")
print(inp)
print("**************")
out = inp.lstrip()
print(out)
# rstrip => remove trailing spaces on right side of the string

inp = "\n\t      ajay kumar     \n\t"
print("**************")
print(inp)
print("**************")
out = inp.rstrip()
print(out)
print("**************")
inp = "    ajay kumar"
out = inp.lstrip()
print(out)