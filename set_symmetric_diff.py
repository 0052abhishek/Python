s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s = s1^s2
t = s1.symmetric_difference(s2)
u = s2.symmetric_difference(s1)
print(s, t, u) # s=t=u
