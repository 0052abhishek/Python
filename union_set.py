s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
u = s1|s2
# alternate method: u = s1.union(s2)
print(u)
