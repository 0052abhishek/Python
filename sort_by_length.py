lst = []
n = eval(input('Enter the number of elements:'))

for i in range(n):
    e = input('Enter the element')
    lst.append(e)

lst.sort(key = len)
print(lst)

