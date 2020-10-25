import random

'''
In this project, I create 1000 games of bingo with 100 players with 5 different fives.
I calculate the average number of number announcement until a bingo occurs.
'''

s=0    #sum
for i in range(1000):
    paiktes = []    # Creating 100 fives of numbers
    for i in range(100):
        ada=random.sample(range(1,81),5)
        if not (ada in paiktes): # Check for duplicates
            paiktes.append(ada)
            paiktes.sort() # Optimising checking (for linear search)
    numbers = range(1,81)
    random.shuffle(numbers)
    bingo = numbers[:5]    
    win=False   
    steps=0     
    while win==False:
        steps+=1
        for pentada in paiktes:
            check=0     # Check for bingo
            for num in pentada:
                if num in bingo:
                    check+=1
            if check==5:
                win=True
        bingo.append(numbers.pop()) # New numbers
    s+=steps

print s/1000  # Avg of steps for bingo
