s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
i = s1&s2
# alternate method: i = s1.intersection(s2)
print(i)
