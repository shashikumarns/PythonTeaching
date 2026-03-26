#REGEX: Regular Exprerssion

# data extraction
# data maipulation
# extract using any patterns
# data search

# Module -> re

#syntax to import module:
#import module_name

import re

# out = re.search("what to search","where to search")
# op is bool - true or false

inp = "hello i am testing regex simply for test"
exp = "test"

out = re.search(exp,inp)
print(out)
#if found -> <re.Match object; span=(11, 15), match='test'>
#if not found -> None


if out:
    print('found')
    print(out.start()) # start index
    print(out.end()) # end index
    print(out.group()) #substr string
else:
    print('not found')
    
    
 
print("*************")


inp = "test hello test i am testing regex simply for test"
exp = "^test" #

out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 4), match='test'>


print("*************")



inp = "test hello test i am testing regex simply for test"
exp = "test$"

out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 4), match='test'>


print("*************")

inp = "cricket team is in india country, ajay is player, ramesh is a player"
exp = "ramesh|ajay|krishna"  # | - or symbol

out = re.search(exp,inp)
print(out)

print("*************")

inp = "test abc test"
exp = "test$"  # 

out = re.search(exp,inp)
print(out)

print("*************")

inp = "i am fan of rahul dravid"
inp1 = "rahul i am fan of rahul dravid"
exp = "^(rahul|dravid)"  # None

out = re.search(exp,inp1)
print(out)

print("*************")

exp = "A(0|1|2|3|4|5|6|7|8|9)B" # A1B , A0B,...
inp = "A1B"
out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 3), match='A1B'>
inp1 = "aA1Bcdfd"
out = re.search(exp,inp1)
print(out)
inp2 = "aA1dcdfd"
out = re.search(exp,inp2)
print(out)
inp3 = "aA123d"
out = re.search(exp,inp2)
print(out)

print("*************")

exp = "[ABC1234]" # 
inp = "A1B"
out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 1), match='A'>

exp = "[ABC1234]" # 
inp = "a5f"
out = re.search(exp,inp)
print(out) #none

print("*************")

exp = "A[0123456789][123]B" # A[0-9][1-3]B
inp = "B23434A72Bc"
out = re.search(exp,inp)
print(out) #<re.Match object; span=(0, 1), match='A'>

inp1 = "A 2B"
out = re.search(exp,inp1)
print(out) #None

print("*************")

exp = "A[ABJK:%#y1002009]B" #A[]B
inp1 = "AxB" #none
out = re.search(exp,inp1)
print(out) #None

inp1 = "asd   A0Bbxxx22343" #none
out = re.search(exp,inp1) #<re.Match object; span=(0, 3), match='A0B'>
print(out) #None

print("*************")

exp = "A[ABJK:%#y1002009] B" 
inp1 = "A% B" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(0, 4), match='A% B'>


print("*************")

#exp = "A[0-9]B" 
exp = "A\dB" 
inp1 = "adsfdsA4B    dfd" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(0, 4), match='A% B'>


print("*************")

#exp = "A[^0-9]B"  #A(non didgit from 0-9)B
exp = "A\DB" 
inp1 = "adsfdsAcB    dfd" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(0, 4), match='A% B'>


print("*************")


#exp = " " 
exp = "^\s"
inp1 = " i am ok" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(0, 1), match=' '>

print("*************")



exp = "a[0-7]B"
inp1 = "asdfda6Baa" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(5, 8), match='a6B'>

print("*************")

exp = "a(0|1|2|3|4|5|6|7)B"
inp1 = "asdfda6Baa" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(5, 8), match='a6B'>

print("*************")

exp = "A[0-246-9a-z]B" #A(0|2)4[6-9][a-z]
inp1 = "asdfdA6Baa" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(5, 8), match='A6B'>


print("*************")

exp = "A[120-246]B" #A(1|2)[0-2](4|6)B
inp1 = "asdfdA7Baa" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(5, 8), match='A6B'>

print("*************")

exp = "A[16-98]B" #A(1)[6-9](8)B
inp1 = "asdfdA1Baa" #none
out = re.search(exp,inp1)
print(out) #<re.Match object; span=(5, 8), match='A6B'>

print("*************")












