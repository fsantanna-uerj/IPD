n1 = input("N1: ")
n2 = input("N2: ")

v = 0

cont1 = 1
while cont1 <= n1:
    cont2 = 1
    while cont2 <= n2:
        v = v + 1
        cont2 = cont2 + 1
    cont1 = cont1 + 1

print "v", v
