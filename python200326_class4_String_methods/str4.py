# replace() => used to search and replace chars, 3rd arg is for occurence which can accept only postivie numbers

# out = str.replace("search_char",replace_Char)

inp = "ajay kumar"
out  = inp.replace("a","b") # all a's replaced with b's char
print(out) #bjby kumbr
#out  = inp.replace("a") error since 2nd positional arg is absent


out = inp.replace('a','b',1)
print(out) #bjay kumar

out = inp.replace('a','bxn',2)
print(out) #bxnjbxny kumar

out = inp.replace('a','bxn',-1)
print(out) #bxnjbxny kumbxnr

out = inp.replace('a','bxn',0)
print(out) #ajay kumar

inp = "ajay  is  a  good  boy"
print(inp.replace("  "," "))
print(inp.replace("  ",""))

inp = "ajay      is    a              good      boy"
print(inp.replace("  "," "))
print(inp.replace("  ",""))