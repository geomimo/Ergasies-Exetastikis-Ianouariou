txt=raw_input("Dwste keimeno: \n") #eisagogi keimenoy
newtxt ="" #to neo keimeno
for i in range(len(txt)):   #gia ka8e xaraktira
    if txt[i]!=" ":
        asc = ord(txt[i])   #eyresi ascii gia ton xaraktira
        if asc <=90:    #an einai kefalaio h pezo
            if asc + 13<=90: 
                asc+=13
            else:
                asc = (asc+13)-90+65-1
        else:
            if asc + 13<=122:
                asc+=13
            else:
                asc = (asc+13)-122+97-1
        newtxt+=chr(asc)    #prosthiki sto neo keimeno
    else:
        newtxt+=" "
print newtxt
