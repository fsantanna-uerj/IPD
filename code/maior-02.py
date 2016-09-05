novo = raw_input("novo: ")
velho = novo
while novo >= velho:
    velho = novo
    novo = raw_input("novo: ")
print "maior:", velho
