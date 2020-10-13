#1
import operator #I had to look up this problem since we haven't learned importing libraries yet.
a = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary:',a)
sorted_a = sorted(a.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value:',sorted_a)
sorted_a = dict( sorted(a.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value:',sorted_a)
#2
b = {0:10, 1:20}
print(b)
b.update({2:30})
print(b)
#3
c={1:10, 2:20}
d={3:30, 4:40}
e={5:50,6:60}
f={}
for x in (c, d, e): f.update(d)
print(f)
#4
g = {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}
def is_key_present(x):
    if x in g:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
#5
h = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in h.items():
    print(color_key, 'corresponds to', h[color_key])
#6
i=int(8)
iD=dict()
for x in range(1,i+1):
    iD[x]=x*x
print(iD)
#7
j=dict()
for x in range(1,16):
    j[x]=x**2
print(j)
#8
k1 = {'a': 1, 'b': 2}
k2 = {'c': 3, 'd': 4}
k = k1.copy()
k.update(k2)
print(k)
#9 = #5
#10
l = {'e':5,'f':6,'g':7}
print(sum(l.values()))
