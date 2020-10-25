'''
In this project, the user gives a text input and the caesar cypher is printed back.
'''
txt=raw_input("Dwste keimeno: \n")
newtxt =""
for i in range(len(txt)):   
    if txt[i]!=" ":
        asc = ord(txt[i])  
        if asc <=90:   
            #  Keeping capital
            if asc + 13<=90: 
                asc+=13
            else:
                asc = (asc+13)-90+65-1
        else:
            # Keeping lower
            if asc + 13<=122:
                asc+=13
            else:
                asc = (asc+13)-122+97-1
        newtxt+=chr(asc)   
    else:
        newtxt+=" "
print newtxt
