import re

inp = "0101010101010"
#inp = "01010101010134230"
# inp is only binary or not

exp = "^[01]*$"

m = re.search(exp,inp)
print(m)
print("**************")
inp = "010101010101"
#out = [0101,0101,0101}
out = re.findall("[01]{4}",inp)
out = re.findall("[01]{2}",inp)
out = re.findall("[01]",inp)
print(out)
out1 =[]
for i in inp:
    out1.append(i)
    

print("**************")

inp = "ajay99ramesh89kiran9vijay"
#out = [ajay, ramesh, kiran, vijay]
out = inp.split('9')
print(out)



out = re.findall("[a-z]+",inp)
print(out)

out = re.split("\d+",inp)
print(out)

print("**************")

inp = "1234test5678"

#replace all digits to 0

out = re.subn("\d+",'0',inp)
print(out) #('0test0', 2)

#replace each digit to 0

out = re.subn("\d",'0',inp)
print(out) #('0000test0000', 8)

#replace all digits to 0

out = re.sub("\d+",'0',inp)
print(out) #'0test0'

#replace each digit to 0

out = re.sub("\d",'0',inp)
print(out) #'0000test0000'


#BACK REFERENCE
# grouping is done by using ()

inp = "4545"
exp = "(\d{2})(\d{2})"
out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 4), match='4545'>
print(out.group()) #4545
print(out.group(1)) #45
print(out.group(2)) #45



print("A\tB")
print("A\\tB")
print(r"A\tB")
print(r"\1\2\3\4")


inp1 = "4545"
#exp1 = r"(\d{2})\1"
exp1 = "(\d{2})\\1"
out1 = re.search(exp1,inp1)
print(out1) #<re.Match object; span=(0, 4), match='4545'>
#print(out1.group(1)) #45



inp2 = "9009"
inp2 = "9090"
inp2 = "9089"
exp2 = r"(\d)(\d)\2\1"
out2 = re.search(exp2,inp2)
print(out2) 


inp3 = "ab cd cd ab"

exp3 = r"([a-z]{2})\s([a-z]{2})\s\2\s\1"
exp3 = r"([a-z]{2})(\s+)([a-z]{2})\2\3\2\1"
out3 = re.search(exp3,inp3)
print(out3) 


inp4 = "abxytest"

#bayxetts

exp4 = r"([a-z])([a-z])"
#exp4 = r"(\w)(\w)"
rep4 = r"\2\1"
out4 = re.subn(exp4,rep4,inp4)
print(out4)


out4 = re.sub(exp4,rep4,inp4)
print(out4)

inp5 = "502"

#out5 = "550022"
exp5 = "(\d)(\d)(\d)"

out5 = re.subn(exp5,r"\1\1\2\2\3\3",inp5)
print(out5)

inp6 = "5.0.2"
#out6 = "5.*0.*2"
exp6 = "(\d)"
out6 = re.subn(exp6,r"\1.*",inp6) #('5.*.0.*.2.*', 3)
print(out6)







































