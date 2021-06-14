def power(x, y):
    p1 = x**y
    p2 = y**x
    return p1, p2

a = eval(input('Enter the first number'))
b  = eval(input('Enter the second number'))
s = power(a, b)
print(s)
