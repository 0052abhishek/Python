str = input('Enter the string:')
v = 0
c = 0
d = 0
w = 0

for i in str:
    

    if ((i >= 'a' and i <='z')or
       (i >= 'A' and i <= 'Z')):

          str = str.lower()
          if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
              v += 1
          else:
              c += 1
    elif (i >= '0' and i <= '9'):
        d += 1
    else:
        w += 1
print('Vowels are:',v,'consonants are:',c,'Digits are:',d,'and whitespaces(or special characters) are:',w)        
