a = input("Enter the number")

ln = len(a)
s = 0
for i in a:
    s += int(i)**ln

if int(a) == s:
    print("Number is armstrong")
else:
    print("Not armstrong")
