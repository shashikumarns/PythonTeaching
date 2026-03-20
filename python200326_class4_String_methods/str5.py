# Split : Breaks the string int to multiple word and stores the result in the form of list, the argument by default is space char to split
# out = str.split("char to split")
inp = "10.45"
print(inp.split()) #['10.45']
print(inp.split('.')) #['10', '45']

inp = "ajay  is  a  good  boy"
print(inp.split('  ')) #['ajay', 'is', 'a', 'good', 'boy']
print(inp.split()) #['ajay', 'is', 'a', 'good', 'boy']

inp = "ajay      is    a              good      boy"
print(inp.split()) #['ajay', 'is', 'a', 'good', 'boy']

print(inp.split('is'))

inp = "ajay,ramesh,vijay,rahul"
print(inp.split(',')) #['ajay', 'ramesh', 'vijay', 'rahul']
print(inp.split(',')[1].upper())

# always start from left to right while debugging multiple method/functions written in single line

inp = "ajay,ramesh,'vij,ay',rahul"
print(inp) #ajay,ramesh,'vij,ay',rahul
print(inp.split(',')) #['ajay', 'ramesh', "'vij", "ay'", 'rahul']