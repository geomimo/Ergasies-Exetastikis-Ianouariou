import random
import sys

i, j = 10,10;
box = [[chr(random.randrange(65,91)) for x in range(i)] for y in range(j)] #dimiourgia koytiou meso ascii
#box[5][0]='G' #bgalte tis diaiseis kai trexte to me arxeio to opoio periexei tin lexi GIORGOS
#box[5][1]='I'
#box[5][2]='O'
#box[5][3]='R'
#box[5][4]='G'
#box[5][5]='O'
#box[5][6]='S'
lex = open(sys.argv[1])
for line in lex:
    word = list(line) #metatrepi tis lexis apo string se list gia dieykolinsi stin sygkrisi
    word.remove('\n') #afairesi pithanon \n
    i=0 #oi grammes toy pinaka
    f=False #flag gia tin eyresi tis lexis
    while i<10 and f==False:
        left=0 #h arxh tis lexis poy checkaro apo ton pinaka orizontia
        while left+len(line)-1<10:
            if box[i][left:len(line)-1]==word:
                print 'Brikate tin lexi\n',line
                f=True
                break
            else:
                left+=1
        i+=1
    j=0 #omoia me pano
    while j<10 and f==False:
        top=0 #h arxi tis lexis katheta
        while top+len(line)-1<10:
            katheto = [] #edo mpainoun ta grammata apo ton pinaka poy einai katheta giatt anikoun se diaforetikous pinakes
            for i in range(top,top+len(line)-1):
                katheto.append(box[i][j])
            if katheto==word: 
                print 'Brikate tin lexi\n',line
                f=True
                break
            else:
                top+=1
        j+=1
lex.close
