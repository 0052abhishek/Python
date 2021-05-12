ch = input()

if 'A' <= ch <= 'Z':
    print('Upper case alphabet')
elif 'a' <= ch <= 'z':
    print('Lower case alphabet')
elif '0' <= ch <= '9':
    print('Digit')
else:
    print('Special character')
