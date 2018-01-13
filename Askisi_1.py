import random

s=0    #sum
for i in range(1000):
    paiktes = []    #dimiourgia 100 5-adon
    for i in range(100):
        ada=random.sample(range(1,81),5)
        if not (ada in paiktes): #elegxos gia na einai monadiki pentada
            paiktes.append(ada)
            paiktes.sort() #dieykolinsi ston elegxo monadikotitas
    numbers = range(1,81)   #lista me tous 80 arithmous
    random.shuffle(numbers)
    bingo = numbers[:5]     #arxiki 5-ada
    win=False   #flag gia bingo
    steps=0     #arithmos vimaton
    while win==False:
        steps+=1
        for pentada in paiktes:
            check=0     #check an oi 5 airtmoi vriskontai stous arithmous bingo
            for num in pentada:
                if num in bingo:
                    check+=1
            if check==5:
                win=True
        bingo.append(numbers.pop())     #"anaggeleia" neo arithmou
    s+=steps

print s/1000     #meso oros
