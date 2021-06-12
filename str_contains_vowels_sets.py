s = {'have','a', 'good', 'day','xyz', 'pqr'}
st = list(s)
st2 = []
for i in range(len(st)):
    if ('a' in st[i] or 'e' in st[i] or 'i' in st[i] or 'o' in st[i] or 'u' in st[i]):
        st2.append(st[i])
print(set(st2))        
