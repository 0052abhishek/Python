n = int(input('Enter the number of elements'))
lst = []
for j in range(1,n+1):
    k = int(input('Enter the element at position: %d'%j))
    lst.append(k)
print('List given by the user:',lst)    
lst2 = []
for i in lst:
    if i%2==0:
        lst2.append(i)
        
print('Even numbers in form of list',lst2)
