ingressos = []

while True:
    preco = input("Preco (0 para terminar): ")
    if preco == 0:
        break
    ingressos.append(preco)

total = 0

for preco in ingressos:
    total = total + preco

print "Total: ", total

media = total/len(ingressos)
print "Media: ", media
