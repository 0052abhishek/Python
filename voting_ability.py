def ability(age):
    if age >= 18:
        return True
    else:
        return False
    
a = int(input('Enter the age:'))
s = ability(a)
print('Eligible') if s else print('Not eligible')
