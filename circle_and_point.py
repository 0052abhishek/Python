x1, y1 = map(int,input('Enter the cordinates of point on circumference ').split())
c1, c2 = map(int,input('Enter the centre point coordinates:').split())
x, y = map(int,input('Enter the point coordinates to be checked:').split())
r = ((x1-c1)**2 + (y1-c2)**2)**(1/2)
l = ((x-c1)**2 + (y-c2)**2)**(1/2)

if r > l:
    print('Point is inside the circle')
elif r < l:
    print('Point is outside the circle')
elif r == l:
    print('Point is on circle')
