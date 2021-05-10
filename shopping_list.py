n = int(input('Enter the maximum number of items:'))
l = []

for i in range(n):
    item = input('Enter the item to be buyed:')
    if item == '':
        break
    else:
        l.append(item)
print(l)
