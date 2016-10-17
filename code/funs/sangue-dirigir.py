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
    
for i in range(0,100):
    idade = input("Qual a sua idade? ")

    sangue  = pode_doar_sangue(idade)
    if sangue:
        print "Voce pode doar sangue"
    else:
        print "Voce nao pode doar sangue"

    dirigir  = pode_dirigir(idade)
    if dirigir:
        print "Voce pode dirigir"
    else:
        print "Voce nao pode dirigir"

