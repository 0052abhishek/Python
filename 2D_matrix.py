lst = list(map(int, input().split()))
r, c = map(int, input().split())
m = []
n = []
count = 0

if r*c == len(lst):
    for i in lst:
        n.append(i)
        count += 1
        if count == c:
            m.append(n)
            n = []
            count = 0
    for j in m:
        for k in j:
            print(k, end = ' ')
        print()

else:
    print('Matrix validation not matched')
