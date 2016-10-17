def pode_doar_sangue ():
    idade = input("Qual a sua idade? ")
    if (idade >= 18) and (idade <= 67):
        print "Voce pode doar sangue"
    else:
        print "Voce nao pode doar sangue"
    
for i in range(0,100):
    pode_doar_sangue()
