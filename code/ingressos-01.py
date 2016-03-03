ingressos = [
    #60, 35, 130, 50, 15,
    60, 35, 130, 50, 15
]

total = 0

for preco in ingressos:
    total = total + preco

print "Total: ", total

media = total/len(ingressos)
print "Media: ", media
