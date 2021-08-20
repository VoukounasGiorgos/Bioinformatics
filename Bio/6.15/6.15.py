al = "AATCTTGGGGGGTAACCAAAATGATGTCCTTTGTCTCT"
lista = list(al)

while (len(lista) > 0 ):
    print "to mikos ths akolou8ias einai ", len(lista), "\n"
    while True :
        #diag = ari8mos stoixeiwn (1 h 2) pou 8a aferesei
        diag = input("o prwtos paixtis epilegei an 8a diagrapsei 1 h 2 noukleotidia  \n")
        if (diag == 1) :
            break
        elif ( (diag == 2) and (len(lista)==1) ):
            print "exei apominei mono 1 noukleotidio"
        elif ( (diag == 2) and (len(lista) >= 2) ):
            break
        else:
            print "prepei na dialekseis 1 h 2 "

    if (diag ==1):
        lista.pop(0)
    else:
        lista.pop(0)
        lista.pop(0)

    winner = 1

    if (len(lista) == 0):
        break

    print "to mikos ths akolou8ias einai ", len(lista), "\n"

    while True :
        #diag = ari8mos stoixeiwn (1 h 2) pou 8a aferesei
        diag = input("o deuteros paixtis epilegei an 8a diagrapsei 1 h 2 noukleotidia  \n")
        if (diag == 1) :
            break
        elif ( (diag == 2) and (len(lista)==1) ):
            print "exei apominei mono 1 noukleotidio"
        elif ( (diag == 2) and (len(lista) >= 2) ):
            break
        else:
            print "prepei na dialekseis 1 h 2 "

    if (diag ==1):
        lista.pop(0)
    else:
        lista.pop(0)
        lista.pop(0)

    winner = 2

if (winner == 1 ):
    print "nikitis einai o prwtos paixtis \n"
else :
    print "nikitis einai o deuteros paixtis \n"
