buraco = input("volume do b: ")
pa1 = input("pa1: ")
pa2 = input("pa2: ")
pa3 = input("pa3: ")

#print(buraco, pa1, pa2, pa3)

movs = 0

while buraco > 0:
    buraco = buraco - pa1
    movs = movs + 1

    buraco = buraco - pa2
    movs = movs + 1

    buraco = buraco - pa3
    movs = movs + 1

print(buraco, movs)
