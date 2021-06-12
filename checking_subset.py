s = set(map(int, input().split()))
s2 = set(map(int, input().split()))
if s2.issubset(s):   #checking s2 is subset of s or not.
    print('YES')
else:
    print('NO')
