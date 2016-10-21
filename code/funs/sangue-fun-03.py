def pode_doar_sangue (idade):
    if (idade >= 18) and (idade <= 67):
        return True
    else:
        return False

def pode_dirigir (idade):
    if idade >= 18:
        print "Voce pode dirigir"
    else:
        print "Voce nao pode dirigir"
    
i = 0
while i < 5:
    i = i + 1
    print "Pessoa ", i
    idade_fora = input("Qual a sua idade? ")
    if pode_doar_sangue(idade_fora):
        print "Voce pode doar sangue"
    else:
        print "Voce nao pode doar sangue"
