n = int(input('Enter the number'))
sum = 0
for i in range(n):
    r = n%10
    sum = sum+r
    n = n//10
print('The sum of all digits of a number is:',sum)    
