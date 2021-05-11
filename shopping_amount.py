a = int(input('Enter the shopping amount'))
if a >25000:
    d = (a*20)/100
    a = a-d
    print('GOLD and amount to be paid is:', a)
elif 10000 <= a <= 25000:
    d = (a*10)/100
    a = a-d
    print('SILVER and amount to be paid is:', a)
elif a < 10000:
    d = (a*5)/100
    a = a-d
    print('BRONZE and amount to be paid is:', a)
