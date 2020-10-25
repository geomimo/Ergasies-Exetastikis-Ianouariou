import random
'''
In this project, a list of random 30 numbers in range [-29,29]/0 is created. The program finds any triplets of numbers that their sum is 0.
'''

# Checking if any combination of number i, j, k exist in the list.
def Check(i,j,k,tr): 
    if [i,j,k] in tr or [i,k,j] in tr or [k,i,j] in tr or [k,j,i] in tr or [j,i,k] in tr or [j,k,i] in tr:
        return False
    else:
        return True

while True:
    lst = random.sample(range(-30,30),30)
    if not (0 in lst):
        break

f=False 
triades=[] 
for i in lst:
    for j in lst:
        for k in lst:
            if i+j+k==0 and Check(i,j,k,triades):
                triades.append([i,j,k])
                f=True

if f==False:
    print "Den vrethike triada"
else:
    for tr in triades: 
        tr.sort()
        print tr
