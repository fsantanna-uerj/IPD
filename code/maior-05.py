velho = raw_input("valor: ")
atual = raw_input("valor: ")
while atual >= velho:
    novo  = raw_input("valor: ")
    velho = atual
    atual = novo
print "MAIOR: ", velho
