print "Bem-vindo ao jogo..."
g = raw_input("Adivinhe o numero: ")
guess = int(g)
if guess == 5:
    print "Voce ganhou!"
else:
    if guess > 5:
        print "Muito alto..."
    else:
        print "Muito baixo..."
print "Fim"
