# Conversion Function: one data type to another data type
"""
out = list(iterable)
out = set(iterable)
out = tuple(iterable)
"""
#iterable: dict, list, set, tuple, string

data = [11,22,33,44,44,33,56]
out=set(data)
print(data)
print(out)

out = tuple(data)
print(out)

out = set(data)
print(out)

out = str(data)
print(out)
print(type(out))

inp="testt"
print(list(inp))
print(set(inp))
print(tuple(inp))
#print(dict(inp))

d = {1:2,3:4,5:6,5:68}
print(list(d))
print(set(d))
print(tuple(d))



inp ="56"
print(int(inp))
print(float(inp))

inp = "51a"
print(str(inp))
#print(int(inp))
#print(float(inp))

# int(Valid_object)

inp = 123.45
print(str(inp))
print(int(inp))

inp = set()
print(bool(inp))

inp = 5
print(bool(inp))

inp = 0.0000000000000000000000001
print(bool(inp))

inp =-1
print(bool(inp))

inp =0
print(bool(inp))


inp =-0
print(bool(inp))


data = [[10,20],[30,40],[50,60]]
out = dict(data)
print(out)

data1 = [[10,20],{30,40},(50,60)]
out1 = dict(data1)
print(out1)


#data2 = [[10,20,30],{30,40},(50,60)]  error
data2 = [[10,[20,30]],{30,40},(50,60)] 
out2 = dict(data2)
print(out2)


data3 = [{10,20},{30,40},{50,60}]
out3 = dict(data3)
print(out3)



data4 = [{10,20,20},{30,40},{50,60}]
out4 = dict(data4)
print(out4)

print("****")
#data5 = {[10,20],[30,50]} #unshable type list error
print(type(data5))
data5 = ([10,20],[30,50])
out5 = dict(data5)
print(out5)













