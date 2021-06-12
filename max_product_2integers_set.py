s = set(map(int, input().split()))
m = max(s) # maximum number
s.remove(m)
m2 = max(s) # second maximum number
print(m*m2)
