
import re
exp = "a\dB"
inp = "A2B"


out = re.search(exp,inp)

if out:
    print(out)
    print(out.group())
else:
    print("NF")
    
print("**********")

#exp = "[a-z][0-9][a-z][0-9]"
exp = "\w\d\w\d"
inp1 = "anbifnini2d4dfkjodf"

out = re.search(exp,inp1)

print(out)
print("**********")
exp = "\W\d\w\D"
inp2 = "anbifnin%2fjodf"
out = re.search(exp,inp2)

print(out)
print("**********")

exp = "[A-Z]\d{3}K" #[A-Z][0-9][0-9][0-9]K
#inp3 = "MJ8939KKK" #none
inp3 = "MJ899KKK" #none
out = re.search(exp,inp3)

print(out)

print("**********")

inp4 = "good 456 morning hi"
exp = ".(0|1|2|3|4|5|6){3}."

out = re.search(exp,inp4)

print(out)
print("**********")

inp4 = "good 456 morning hi"
exp = ".(0-6){3}."

out = re.search(exp,inp4) #none due to braces in exp is ()

print(out)
print("**********")
inp4 = "good 456 morning hi"
exp = ".[0-6]{3}."

out = re.search(exp,inp4) #found due to braces in exp []

print(out)
print("**********")
exp = "[A-Z]\d{1,3}K" #[A-Z][0-9]K or  [A-Z][0-9][0-9]K or [A-Z][0-9][0-9][0-9]K
#inp3 = "MJ8939KKK" #none
inp3 = "MJ899KKK" #Matched
out = re.search(exp,inp3)


print(out)
print("**********")

exp = "[A-Z]\d{0,1}K" #[A-Z]K  or [A-Z][0-9]K 
#inp3 = "MJ8939KKK" #none
inp3 = "MJ899KKK" #Matched
out = re.search(exp,inp3)


print(out)
print("**********")

"""
? => {0,1} => 0 or 1 time
+ => {1,} => 1 or many time
* => {0,} => o or many time   
 
\d? => \d{0,1}
\w? => \w{0,1}
\d+ => \d{1,}
samples:
x? => x{0,1}
\d{10}
.d{10}
[A-Z]{5,10}
"""

print("*********")
exp = "^[A-Z]\d?K$" #[A-Z]K  or [A-Z][0-9]K 
#? => {0,1} => 0 or 1 time

#inp3 = "MJ8939KKK" #none
inp3 = "MK" #Matched
inp3 = "M1K" #Matched
inp3 = "M12K" #Not matched since digit is 2 chars
out = re.search(exp,inp3)


print(out)

print("*********")
exp = "[A-Z]\d+K$" #[A-Z]K  or [A-Z][0-9]K 
#+ => {1,} => 1 or many time

#inp3 = "MJ8939KKK" #none
inp3 = "asdfe34355aM567K" #Matched <re.Match object; span=(11, 16), match='M567K'>
inp3 = "asdfe34355aM5K" #Matched <re.Match object; span=(11, 14), match='M5K'>
inp3 = "asdfe34355aMK" #None
inp3 = "asdfe34355aM5Kddfd" #None
out = re.search(exp,inp3)


print(out)
print("**********")

print("*********")
exp = "^[A-Z]\d*K$" #[A-Z]K  or [A-Z][0-9]K 
#* => {0,} => o or many time   

#inp3 = "MJ8939KKK" #none
inp3 = "MK" #Matched
inp3 = "M1K" #Matched
inp3 = "M12K" #Matched
out = re.search(exp,inp3)


print(out)

print("*********")

exp = "^[A-Z]\d{1,}K"
exp = "^\w\d*K"
inp = "a98873483784K" #match for +
inp = "aK" #match for *
out = re.search(exp,inp)


print(out)
print("*********")

inp = "hello india '979465446ABCD' done"
#exp = "'\d*\w*'"
exp = "'.+'"

# '979465446ABCD'

out = re.search(exp,inp)

if out:
    print(out.group())
else:
    print("NF")


print("*********")

#inp = "hi \nhow are you\nwhat is your name\nmy name is ajay..."
inp1 = "what is your name"
inp2 = "hi \nhow are you\nwhat is your name\nwhat is your name..."
print(inp)
exp = "what.*"


out = re.search(exp,inp2)

if out:
    print(out)
    print(out.group())
else:
    print("NF")

print("*********")

#interview question: python expression are greedy or non-greedy
#greedy example:
exp = "9\d+8"
inp = "hello 565 indicate 889899256854545928454546 is good"


out = re.search(exp,inp)

if out:
    print(out)
    print(out.group()) #9899256854545928
else:
    print("NF")

print("*********")
# how to make it non-greedy

exp = "9\d+?8"
inp = "hello 565 indicate 889899256854545928454546 is good"


out = re.search(exp,inp)

if out:
    print(out)
    print(out.group()) #98992568
else:
    print("NF")

print("*********")

exp = "9\d*?8"
inp = "hello 565 indicate 889899256854545928454546 is good"


out = re.search(exp,inp)

if out:
    print(out)
    print(out.group()) #98
else:
    print("NF")

#Modifiers:

exp = "A.B"
#inp = "A\nB" #NF
#inp = "A B" #Found
#inp = "A B" #Found
#inp = "A\sB" #NF
inp = "A\nB" #NF
out = re.search(exp,inp)
mod = re.search(exp,inp, flags=re.S)
if out:
    print(out)
    print(out.group()) #98
else:
    print("NF")

if mod:
    print(mod)
    print(mod.group()) #98
else:
    print("NF")
print("*********")

exp = "a b"
inp = "A B"
mod = re.search(exp,inp, flags=re.I)
if mod:
    print(mod)
    print(mod.group()) #98
else:
    print("NF")






