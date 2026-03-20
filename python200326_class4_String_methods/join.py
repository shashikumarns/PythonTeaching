#Join => Joion a iterable in to a string
# output of join will be in string

# out = "Joining_char".join(iterable_String)

data = ['ajay','ramesh','vijay','rahul']
out = "#".join(data)
print(out) #    ajay#ramesh#vijay#rahul

out = " ".join(data)
print(out) #    ajay ramesh vijay rahul

out = ",".join(data)
print(out) #    ajay,ramesh,vijay,rahul

data = "aeroplane"
out = "#".join(data)
print(out) # a#e#r#o#p#l#a#n#e

data = {'rn1':"ajay", "rn2":'kumar'}
out = "#".join(data)
print(out) # rn1#rn2

