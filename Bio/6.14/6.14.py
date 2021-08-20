al1 = "CCCAGGGCCCCGTGCTGCAGGCTAGCGGCCTCCCGC"
lista1 = list(al1)
al2 = "GCCTCTGCTAGTTGCACCTCTTCCGTCA"
lista2 = list(al2)

while ( (len(lista1) and len(lista2)) != 0 ) :
    print "Ta mhkh twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2) , "\n"
    winner = 1
    while True:
        diag = input("o prwtos paixtis dialegei an 8a diagrapsei 1 h 2 noukleotidia apo tin prwth akolou8ia \n")
        # lista 1 h lista 2
        if ((diag== 1) or (diag == 2)):
            break
        else:
            print "prepei na epilekseis 1 h 2 \n"
    #gia thn prwti akolou8ia
    if (diag == 1):
        lista1.pop(0)
        print "afou epelekses na diagrapseis 1 apo tin pwrti akolou8ia diagrafonte duo noukleotidia apo thn deuterh \n"
        lista2.pop(0)
        lista2.pop(0)
    else:
        lista1.pop(0)
        lista1.pop(0)
        print "afou epelekses na diagrapseis 2 apo tin pwrti akolou8ia diagrafete ena noukleotidio apo thn deuterh \n"
        lista2.pop(0)
    if ( (len(lista1) or len(lista2)) == 0 ):
        break
    winner =  2
    print "Ta mhkh twn akolou8iwn 1 kai 2 einai antistoixa ->" , len(lista1) ,"kai", len(lista2) , "\n"
    while True:
        diag = input("o deuteros paixtis dialegei an 8a diagrapsei 1 h 2 noukleotidia apo tin prwth akolou8ia \n")
        # lista 1 h lista 2
        if ((diag== 1) or (diag == 2)):
            break
        else:
            print "prepei na epilekseis 1 h 2 \n"
    #gia thn prwti akolou8ia
    if (diag == 1):
        lista1.pop(0)
        print "afou epelekses na diagrapseis 1 apo tin pwrti akolou8ia diagrafonte duo noukleotidia apo thn deuterh \n"
        lista2.pop(0)
        lista2.pop(0)
    else:
        lista1.pop(0)
        lista1.pop(0)
        print "afou epelekses na diagrapseis 2 apo tin pwrti akolou8ia diagrafete ena noukleotidio apo thn deuterh \n"
        lista2.pop(0)


if (winner == 2 ):
    print "nikitis einai o prwtos paixtis \n"
else :
    print "nikitis einai o deuteros paixtis \n"
