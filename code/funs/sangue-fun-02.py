def pode_doar_sangue (idade):
    if (idade >= 18) and (idade <= 67):
        return True
    else:
        return False
    
for i in range(0,100):
    idade = input("Qual a sua idade? ")
    pode  = pode_doar_sangue(idade)
    if pode:
        print "Voce pode doar sangue"
    else:
        print "Voce nao pode doar sangue"
