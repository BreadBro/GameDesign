#1
aTuple = ("a","b","c")
print(aTuple)
#2
bTuple = ("a", True, 1.5, 1)
print(bTuple)
#3
cTuple = (1,2,3)
print(cTuple[2])
#4
print(cTuple)
x, y, z = cTuple
print(x+y+z)
x, y, z = cTuple
#5
dTuple = ("x","y","z")
b="w"
eTuple = dTuple + (b,)
print(eTuple)
#6
eTuple = ("d","e","f")
print(''.join(eTuple))
#7
fTuple = ("5","6","7","8","9","10")
print(fTuple[3])
print(fTuple[-4])
#8
"g"
#9
hTuple = (1,1,1,1,2)
hcount = hTuple.count(1)
print(hcount)
#10
iTuple = ("a","b","c","d")
print("a" in iTuple)
print("1" in iTuple)
#11
jList = [1,2,3]
jTuple = tuple(jList)
print(jTuple)
