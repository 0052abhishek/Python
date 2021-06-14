def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter the number to be checked"))
s = even(n)
print('Even number') if s else print('Not even number')
