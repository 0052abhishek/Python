o = int(input('Enter the number of overs in cricket match'))


'''as to score maximum runs player requires to play maximum balls of each and every over
so he playes hits 5 sixes each over
and took 3 on last ball except last over(6 sixes)
It can be easily undrestood by below LOGIC

'''
max_runs = (o-1)*5*6 + (o-1)*3 + 6*6
print(max_runs)
