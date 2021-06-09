s = set(map(int, input().split()))
n = int(input('Enter the no. to be removed'))
s.discard(n)
print(s)
