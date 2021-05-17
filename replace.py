lst = [(10,20,40), (40,50,60), (70,80,90)]
lst2 = []
for i in range(len(lst)):
    ls = list(lst[i])
    ls[2] = 100 #Putting 100 at 2nd index in every tuple in list.
    
    ls = tuple(ls)
    lst2.append(ls)
print(lst2)    
        
       
