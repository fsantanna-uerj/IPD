i = 0
while i < 5:
    i = i + 1
    print "Pessoa ", i
    idade = input("Qual a sua idade? ")
    if (idade >= 18) and (idade <= 67):
        print "Voce pode doar sangue"
    else:
        print "Voce nao pode doar sangue"
