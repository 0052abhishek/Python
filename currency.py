a = int(input('Input the amount'))
a = a-100
o = 1
t = a//2000
print('No. of 2000 notes',t)
a = a-t*2000
f = a//500
print('No. of 500 notes',f)
a = a-f*500
o = o + a//100
print('No. of 100 notes',o)



