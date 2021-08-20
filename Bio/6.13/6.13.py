import random
al1 = "AAACTTTCGTGCGCGTTGAA"
lista1 = list(al1)
al2 = "CTGCTGGCGCGGCGGGGCGGACTCCACCCCTGCCC"
lista2 = list(al2)
print "Ta mhkh twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2) , "\n"

while ( len(lista1) or len(lista2) != 0):


    print "O prwtos paixtis dialegei an 8a diagrapsei mono apo ti mia h kai apo tis duo akolou8ies \n"

    while True:
        diag = input("8a diagrapseis apo 1 h kai apo tis 2 akolou8ies? \n")
        if ((diag == 1) or (diag == 2)):
            break
        else:
            print "prepei na epilekseis 1 h 2 \n"

    if ((diag == 1)):

        while True:
            diag = input("8a diagrapseis apo tin 1h h apo thn 2h akolou8ia? \n")
            if ((diag == 1) or (diag == 2)):
                break
            else:
                print "prepei na epilekseis 1 h 2 \n"
        if (diag == 1) :
            x = len(lista1)
            r = random.randint(0,x)
            lista1 = lista1[r:]
            print lista1
        else :
            y  = len(lista2)
            r = random.randint(0,y)
            lista2 = lista2[r:]
            print lista2

    else:
        x = len(lista1)
        y = len(lista2)
        if (x == 0) :
            r = random.randint(0,y)
        elif (y == 0) :
            r = random.randint(0,x)
        elif (x > y) :
            r = random.randint(0,x)
        elif (x < y) :
            r = random.randint(0,y)
        lista1 = lista1[r:]
        lista2 = lista2[r:]

    print "Ta mhkh twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2), "\n"

    winner = 1

    if ( len(lista1) and len(lista2) == 0):
        break



    print "O deuteros paixtis dialegei an 8a diagrapsei mono apo ti mia h kai apo tis duo akolou8ies \n"

    while True:
        diag = input("8a diagrapseis apo 1 h kai apo tis 2 akolou8ies? \n")
        if ((diag == 1) or (diag == 2)):
            break
        else:
            print "prepei na epilekseis 1 h 2 \n"

    if ((diag == 1)):

        while True:
            diag = input("8a diagrapseis apo tin 1h h apo thn 2h akolou8ia? \n")
            if ((diag == 1) or (diag == 2)):
                break
            else:
                print "prepei na epilekseis 1 h 2 \n"
        if (diag == 1) :
            x = len(lista1)
            r = random.randint(0,x)
            lista1 = lista1[r:]
            print lista1
        else :
            y  = len(lista2)
            r = random.randint(0,y)
            lista2 = lista2[r:]
            print lista2

    else:
        x = len(lista1)
        y = len(lista2)
        if (x == 0) :
            r = random.randint(0,y)
        elif (y == 0) :
            r = random.randint(0,x)
        elif (x > y) :
            r = random.randint(0,x)
        elif (x < y) :
            r = random.randint(0,y)
        lista1 = lista1[r:]
        lista2 = lista2[r:]

    print "Ta mhkh twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2), "\n"

    winner = 2

    if ( len(lista1) and len(lista2) == 0):
        break


if (winner == 1 ):
    print "nikitis einai o prwtos paixtis \n"
else :
    print "nikitis einai o deuteros paixtis \n"
