st = input('Enter a string;')
st2 = ''

for i in st:
    if i.isalpha():
        st2 += i

print('String with alphabet only is:--> ',st2)        
