import itertools

arr = set(map(int, input().split()))
n = int(input('Enter the length of subset'))
d = itertools.combinations(arr, n)
subsets = set(d)
print(subsets)
