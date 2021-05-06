st = input('Enter the string:')
frequency = {}
for char in st:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)        
