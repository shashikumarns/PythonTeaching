# Dict Methods

d = {1:'a',2:'b',3:'c'}
print(d)

# keys() and values()

print(d.keys()) #dict_keys([1, 2, 3])  # internal type
print(list(d.keys())) #[1, 2, 3]

print(d.values()) # dict_values(['a', 'b', 'c']) # intental type - dic values
print(list(d.values()))  #['a', 'b', 'c']

print(d.items()) #dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
print(list(d.items())) #[(1, 'a'), (2, 'b'), (3, 'c')]
print(list(d.items())[1]) #(2, 'b')
print(list(d.items())[1][1]) #b

d1={}
print(d1.keys()) #dict_keys([])
print(d1.values()) #dict_values([])
print(d1.items()) #dict_values([])

#important
#GET() and SETDEFAULT()
data = {'rn1':'ramesh','rn2':'kiran'}

print(data['rn1'])
#print(data['rn4']) # key error

print(data.get('rn1'))
print(data.get('rn4'))  # None

print(data.get('rn1','not_present'))
print(data.get('rn4','not_present'))  # not_present

print(data) #{'rn1':'ramesh','rn2':'kiran'}

data = {'rn1':'ramesh','rn2':'kiran'}
out = data.setdefault('rn1')
print(out)

out = data.setdefault('rn4')
print(out) # None

print(data) #{'rn1': 'ramesh', 'rn2': 'kiran', 'rn4': None}

out = data.setdefault('rn1','dummy')
print(out)

out = data.setdefault('rn5','dummy')
print(out) # None

print(data) #{'rn1': 'ramesh', 'rn2': 'kiran', 'rn4': None, 'rn5': 'dummy'}

data = {'rn1':'ramesh','rn2':'kiran'}
# pop

out = data.pop('rn1')
print(data) #{'rn2':'kiran'}


#out = data.pop('rn3')
print(data) #{'rn2':'kiran'} #key error



data1  = {'rn1':'ramesh','rn2':'kiran'}
data2 = {}

data2 = data1.copy()
print(data2)


data1 = {10:20,40:60,90:100}
data2 = {50:60, 70:80}

#out = {10:20,40:60,90:100, 50:60, 70:80}
data1.update(data2)
out =data1
print(out)

data1.pop(50)
data1.pop(70)
print(data1)



data1.clear()
print(data1) #{}




# keys(), values(), items()
# get() -> not presnt then we get none, setdefault() -> iunsert if not present
# pop()
# copy(), update(), clear()






