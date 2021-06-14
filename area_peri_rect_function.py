def ar_and_peri(le, bre):
    area = le*bre
    perimeter = 2*(le + bre)
    return (area, perimeter)



l = int(input('Enter the length of rectangle'))
b = int(input('Enter the breadth of rectangle'))
s = ar_and_peri(l, b)
print(s)
