al1 = "AAACTTTCGTGCGCGTTGAA"
lista1 = list(al1)
al2 = "CTGCTGGCGCGGCGGGGCGGACTCCACCCCTGCCC"
lista2 = list(al2)

while ( len(lista1) and len(lista2) != 0):
    print "To mikos twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2)

    print "O prwtos paixtis dialegei pia akolou8ia 8a diagrapsei"

    while True:
        diag = input("diegrapse akolou8ia 1 h akolou8ia 2 \n")
        if ((diag == 1) or (diag == 2)):
            break
        else:
            print "prepei na epilekseis 1 h 2"

    if (diag == 1 ):
        emeine = lista2
    else:
        emeine = lista1

    while True:
        n = input ("dwse ari8mo xaraktirwn gia na xwriseis tin akolou8ia pou emeine \n")
        if (n < len(emeine)):
            break
        else:
            print "dwse mikrotero ari8mo"

    nlista1 = []
    for i in range (0,n):
        nlista1.append(emeine[i])

    nlista2 = []
    for j in range (n,len(emeine)):
        nlista2.append(emeine[j])

    lista1 = nlista1
    lista2 = nlista2

    winner = 1

    while ( len(lista1) and len(lista2) != 0):
        print "To mikos twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2)

        print "O deuteros paixtis dialegei pia akolou8ia 8a diagrapsei"

        while True:
            diag = input("diegrapse akolou8ia 1 h akolou8ia 2 \n")
            if ((diag == 1) or (diag == 2)):
                break
            else:
                print "prepei na epilekseis 1 h 2"

        if (diag == 1 ):
            emeine = lista2
        else:
            emeine = lista1

        while True:
            n = input ("dwse ari8mo xaraktirwn gia na xwriseis tin akolou8ia pou emeine \n")
            if (n < len(emeine)):
                break
            else:
                print "dwse mikrotero ari8mo"

        nlista1 = []
        for i in range (0,n):
            nlista1.append(emeine[i])

        nlista2 = []
        for j in range (n,len(emeine)):
            nlista2.append(emeine[j])

        lista1 = nlista1
        lista2 = nlista2

        winner = 2

if (winner == 1 ):
    print "nikitis einai o prwtos paixtis"
else :
    print "nikitis einai o deuteros paixtis"
