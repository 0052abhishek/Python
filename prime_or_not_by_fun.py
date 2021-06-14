def prime(num):
    c = 0
    if num>1:
        for i in range(2, num):
            if num % i == 0:
                c += 1
    else:
        return False
    
    if c > 0:
        return False
    else:
        return True


n = int(input('Enter the number to be checked'))
s = prime(n)
print('Prime number') if s else print('Not a prime number')
