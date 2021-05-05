l = int(input('Enter the lower limit of range'))
u = int(input('Enter the upper limit of range'))
print('All the prime numbers between the given range are :')
for num in range(l, u+1):
    if num>1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
             print(num)
