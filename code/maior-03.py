novo = 0
velho = 0
while novo >= velho:
    velho = novo
    novo = int(raw_input("novo: "))
print "maior:", velho
