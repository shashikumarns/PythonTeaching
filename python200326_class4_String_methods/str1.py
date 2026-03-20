#String Methods

city = "BanGalorE iS iN INDIA"

# upper => convert all chars in the object to the upper case

print(city.upper()) #BANGALORE IS IN INDIA

#print(upper(city)) => error

print(city.lower()) #bangalore is in india

#title() ==> which converts all words first char to capital

print(city.title()) #Bangalore Is In India

#capitalize() ==> it converts only the first word first char to the capital

print(city.capitalize()) #Bangalore is in india

#swapcase() ==> it swaps cap to small or small to cap in the string

print(city.swapcase())  #bANgALORe Is In india


inp = "AJAY KUMAR"
out = inp.islower()
print(out) #False


inp = "AJAY KUMAR"
out = inp.isupper()
print(out) #true

inp = "AJAY KUMAR"
inpt = "Ajay Kumar"
out = inp.istitle()
print(out) #False

out = inpt.istitle()
print(out) #True

inp = "5a"
out = inp.isdigit()
print(out) #False

inp = "53"
out = inp.isdigit()
print(out) #True

inp = "ajay kumar"
out = inp.startswith("a")
print(out) #True

inp = "ajay kumar"
out = inp.startswith("AJAY")
print(out) #False


inp = "ajay kumar"
out = inp.upper().startswith("AJAY")
print(out) #True

inp = "ajay kumar"
out = inp.endswith("kumar")
print(out) #True

inp = "ajay kumar"
out = inp.count("a")
print(out) #3

inp = "ajay kumar"
out = inp.count('1')
print(out) #0

inp = "ajar kumar"
out = inp.index('r')
print(out) #3

inp = "ajar kurar"
out = inp.index('r',5) # second arg is starting index for the search of the char
print(out) #3


inp = "ajay kumar"
##out = inp.index('0')
##print(out) #value error: substring not found


inp = "ajay kumar"
print(inp.find("a")) #0 ==> found

inp = "ajay kumar"
print(inp.find("0"))  # -1 ==> not found

inp = "ajay kumar"
#out = "AY KU"
print(inp[2:7].upper())






















