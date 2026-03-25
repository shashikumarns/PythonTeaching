#DOD => Dict of Dict

#              k    v    k      v
dod = {
    'HDFC' : {'AN':123,'Name':'Ajay'},
    'CITI' : {'AN':124,'Name':'RAM'},
    'ICICI' : {'AN':125,'Name':'KIRAN'},
}

#    --k----   -----------v------------

#dod_object['key']['key']

print(dod)
print(dod['ICICI'])
print(dod['ICICI']['Name'])
print(dod['CITI'].values())
print(dod['CITI'].keys())
print(dod['CITI'].items())

dod['CITI']['AN']=126
print(dod)

#branch:bangalore

dod['HDFC']['branch'] = 'bangalore'
print(dod)

print("***************")

dod1 = {
    'HDFC' : {'AN':123,'Name':'Ajay'},
    'CITI' : {'AN':124,'Name':'RAM'},
    'ICICI' : {'AN':125,'Name':'KIRAN'},
}

for i in dod1:
    print(i)
    #print(i, dod1[i])
    for j in dod1[i]:
        print('   ', j, dod1[i][j])


"""
HDFC
    AN 123
    Name Ajay
CITI
....
"""


print("***************")


# skip HDFC and CITI Banks

dod2 = {
    'HDFC' : {'AN':123,'Name':'Ajay'},
    'CITI' : {'AN':124,'Name':'RAM'},
    'ICICI' : {'AN':125,'Name':'KIRAN'},
}


for i in dod2:
    print(i, dod2[i])
    if i != 'HDFC':
        continue
        print('a')
    if i != 'CITI':
        print('b')


print("*******++++*****")

for i in dod2:
    print(i, dod2[i])
    if i != 'HDFC' or i != 'CITI':
        continue
        print('a')
        print('b')
print('c')
print("***************")






