def ar_and_cir(rad, pi):
    area = 2*pi*rad**2
    circumference = 2*pi*rad
    return area , circumference

r = eval(input('Enter the radius of circle'))
pi = 3.14
s = ar_and_cir(r, pi)
print(s)
