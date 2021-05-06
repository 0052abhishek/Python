n = int(input('Enter the number:'))
fact = 1

while n:
    fact *= n
    n -= 1
    if n == 1:
        break
print(fact)    

