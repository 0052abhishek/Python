st = input('Enter the string:')
st1 = ''
for i in st:
    if ((i >='a' and i <= 'z') or
        (i >= 'A' and i <= 'Z')):
        st1 += i
print(st1)    
    
