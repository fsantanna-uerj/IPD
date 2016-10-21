def pode_doar_sangue (idade):
    if (idade >= 18) and (idade <= 67):
        return True
    else:
        return False

def pode_dirigir (idade):
    if (idade >= 18):
        return True
    else:
        return False
    
i = 0
while i < 5:
    idade = input("Qual a sua idade? ")
    print "Pessoa ", i

    if pode_doar_sangue(idade):
        print "Voce pode doar sangue"
    else:
        print "Voce nao pode doar sangue"

    if pode_dirigir(idade):
        print "Voce pode dirigir"
    else:
        print "Voce nao pode dirigir"

