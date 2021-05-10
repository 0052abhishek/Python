m = eval(input('Enter the matrix'))

ln = len(m[0])
for i in m:
  if ln != len(i):
    print('Matrix is not valid')
    break
else:
  print('Valid matrix')
