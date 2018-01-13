txt=raw_input("Dwste keimeno: \n")
newtxt =[]
for i in range(len(txt)):
    if txt[i]!=" ":
        asc = ord(txt[i])
        if asc <=90:
            if asc + 13<=90:
                asc+=13
            else:
                asc = (asc+13)-90+65-1
        else:
            if asc + 13<=122:
                asc+=13
            else:
                asc = (asc+13)-122+97-1
        newtxt+=chr(asc)
    else:
        newtxt+=" "
newtxt = ''.join(newtxt)
print newtxt
