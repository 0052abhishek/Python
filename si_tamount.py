p = int(input('Enter the principal amount'))
r = int(input('Enter the rate of interest'))
t = int(input('Enter the time period'))
si = (p*r*t)/100
ta = si+p
print('SI and total amount are', si, ta)
