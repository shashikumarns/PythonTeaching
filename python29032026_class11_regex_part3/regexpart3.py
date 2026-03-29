#Modifiers:

# re.S => which will make . to march \n as well
import re
exp = "A.B"
inp = "A\nB"

out = re.search(exp,inp)
out = re.search(exp,inp, flags =  re.S)
#mod = re.search(exp,inp, flags=re.S)
if out:
    print(out)
    print(out.group()) #98
else:
    print("NF")
    
print("*******")

#re.I => ignorance case flag
exp ="a b"
inp = "A B"

out = re.search(exp,inp)
out = re.search(exp,inp, flags =  re.I)
#mod = re.search(exp,inp, flags=re.S)
if out:
    print(out)
    print(out.group()) #98
else:
    print("NF")
    

print("*******")   

inp = '56' #found
inp = '56abc' #nf
exp = '^5\d$'
out = re.search(exp,inp)
print(out)

print("*******")  

inp = "400.556565465"
exp = '^\d+\.\d+$'
out = re.search(exp,inp)
print(out)


print("*******")  

inp = "A+B"
exp = '^\w\+\w$'
out = re.search(exp,inp)
print(out)

print("*******") 


inp = "abcd_123@gmail.com"
exp = '^\w+\@\w+\.\w+$'
out = re.search(exp,inp)
print(out)

print("*******")

inp = "12"  #0,01,02...10,11,12
exp = "^([0-9])|(10|11|12)$"
#exp = "^[0-9]|1[0-2]$"
out = re.search(exp,inp)
print(out.group())
print(out)
 
print("*******")
#01-31

dt = "31"
exp = '^(0[1-9])|(1\d|2\d)|(3[01])$'
out = re.search(exp,dt)
print(out.group())
print(out.group(1))
print(out.group(2))
print(out.groups)
print(out)

print("*******")
inp= "4/04"
exp = "^\d\/\d+$"
out = re.search(exp,inp)
print(out.group())

print("*******")
#t = "05:30"
t = "19:30"

#hr - 00 to 24
#min - 00 to 60

exp = "[0-1][0-9]|2[0-4]\:[0-5][0-9]|60"

out = re.search(exp,t)
print(out)
#print(out.group())


print("*******")
#needs re-work
dt = "24/12/2019"
#years 1900 to 2099
exp = "^(0?[1-9]|[21][0-9]|3[01])/(0?[1-9]|1[0-2])/((19|20)\d{2})"

out = re.search(exp,t)
print(out)
#print(out.group(1))
#print(out.group(2))
#print(out.groups())
#print(out.group())


print("*******")
"""
192.168.0.102
192.168,0.255
127.0.0.1
 0-255

"""

inp = "192.00.0.102"
exp = "(\d{1,3})\.(\d{1,3}).(\d{1,3}).(\d{1,3})"

out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 13), match='192.168.0.102'>
print(out.group) #<built-in method group of re.Match object at 0x00000293A0B17880>
print(out.group(1)) #192
print(out.group(2)) # 168
print(out.group(3)) # 0
print(out.group(4)) #102
print(out.groups()) #('192', '168', '0', '102')

print("*******")
print('check less than 255')
inp = "192.00.0.255"
exp = "(\d{1,3})\.(\d{1,3}).(\d{1,3}).(\d{1,3})"

out = re.search(exp,inp)
print(out)
print(out.groups()) #('192', '168', '0', '102')
if int(out.group(1)) <=255 and int(out.group(2)) <=255 and int(out.group(3)) <=255 and int(out.group(4)) <=255:
    print('correct input')
else:
    print('incorrect input')

print("*******")
# needs a work in exp:
inp = "24/12/2019"
exp = r"(\d{1,2})//(\d{1,2})//(/d{4})"
out = re.search(exp,inp)
print(out)
#print(out.groups()) 


#if (g1 >0 or g1 <32) and (g2 <13) and (g3>=1900 or g3 <=2099)

print("*******")

inp = "test 4544 abc 343234 hello 3434 33423 1231"
exp = "\d+"
out = re.search(exp,inp)
print(out)

#re.search => first single occurence check
#re.findall => multile occurence
out = re.findall(exp,inp)
print(out) #['4544', '343234', '3434', '33423', '1231']


print("*******")

inp = "test 4544 abc 343234 HELlo 3434 33423 1231"
exp = "hello"
out = re.search(exp,inp,flags=re.I)
print(out) #<re.Match object; span=(21, 26), match='HELlo'>

#re.search => first single occurence check
#re.findall => multile occurence
out = re.findall(exp,inp,flags=re.I)
print(out) #['HELlo']

print("*******")


#inp = "000100101010101"
inp = ""
#exp = "^(0|1)+$"
#exp = "^[01]+$"
#exp = "^[01]?$" <re.Match object; span=(0, 0), match=''>
exp = "^[01]*$" 
out = re.search(exp,inp)
print(out) 

print("*******")

inp = "0001 1000 1100"

#out = [0001,1000,1100]
out = inp.split(" ")
print(out)


out = re.findall("[01]{4}",inp)
print(out)

print("*******")

inp = "ajay9ramesh9kiran9ram"
#out = [above names]

out = inp.split("9")
print(out)

out = re.findall("[a-z]+",inp)
print(out)

print("*******")

inp = "a::b::::c:::::::::::::d"
#out = [a,b,c,d]
out = inp.split(":")
print(out)
out = re.findall(":+",inp)
print(out)
out = re.findall("[a-z]+",inp)
print(out)


print("*******")

inp = "ajay,ramesh,vijay,kiran"
#out = [a,b,c,d]
out = inp.split(",")
print(out)
out = re.findall("[a-z]+",inp)
print(out)

print("*******")

inp = "ajay     ,ramesh   ,vijay  ,kiran"
#out = [a,b,c,d]
out = inp.split(",")
print(out)
out = re.findall("[a-z]+",inp)
print(out)

out = re.findall("\s*,\s*",inp)
print(out)


print("*******")

inp = "456abc12"
exp ="\d"

out = re.subn(exp,"x",inp)
print(out) #('xxxabcxx', 5) ==> replaced string and no of times replaced char


out = re.sub(exp,"x",inp)
print(out) #xxxabcxx

print("*******")

inp = "456abc12"
exp ="\d+"

out = re.subn(exp,"x",inp)
print(out) #('xabcx', 2)

out = re.sub(exp,"x",inp)
print(out) #'xabcx'


print("*******")

inp = "4545"
#inp = "5664"

exp = "^(\d{2})(\d{2})$"

out = re.search(exp,inp)
print(out)
print(out.groups)
print(out.group(1))
print(out.group(2))

print("*******")

inp = "4545"
exp = "^(\d{2})\1$"
# search first 2 digit and check next 2 digit is same or not by using back reference \1, \2, \3
out = re.search(exp,inp)
print(out)







































