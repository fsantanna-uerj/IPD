velho = int(raw_input("valor: "))
atual = int(raw_input("valor: "))
soma  = velho + atual
total = 2
while atual >= velho:
    novo  = int(raw_input("valor: "))
    total = total + 1
    soma  = soma + novo
    velho = atual
    atual = novo
print "MEDIA: ", soma/total
