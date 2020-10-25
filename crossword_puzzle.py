import random
import sys
'''
In this project, a 10x10 crossword puzzel is created. The user gives a file with 1 word per line
and the project checks if the words exist horizontally or vertically
'''

i, j = 10,10;
box = [[chr(random.randrange(65,91)) for x in range(i)] for y in range(j)] # Creating a 10x10 crossword puzzle with random letters in ascii
# Remove comment below to insert the name GIORGOS in the puzzle
#box[5][0]='G' 
#box[5][1]='I'
#box[5][2]='O'
#box[5][3]='R'
#box[5][4]='G'
#box[5][5]='O'
#box[5][6]='S'
# Reading a file with words to search
lex = open(sys.argv[1])
for line in lex:
    word = list(line)
    word.remove('\n')
    i=0 
    f=False # Flag for a word finding
    # Search horizontally
    while i<10 and f==False:
        left=0 
        while left+len(line)-1<10:
            if box[i][left:len(line)-1]==word:
                print 'Brikate tin lexi\n',line
                f=True
                break
            else:
                left+=1
        i+=1
    # Search vertically
    j=0
    while j<10 and f==False:
        top=0 
        while top+len(line)-1<10:
            katheto = [] 
            for i in range(top,top+len(line)-1):
                katheto.append(box[i][j])
            if katheto==word: 
                print 'Brikate tin lexi\n',line
                f=True
                break
            else:
                top+=1
        j+=1
lex.close()
