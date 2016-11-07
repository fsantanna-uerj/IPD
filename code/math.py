import math

print(math.sin(0),  math.cos(0))
print(math.sin(math.radians(90)), round(math.cos(math.radians(90))))

x = input('x: ')
y = input('y: ')
soma = 0
for i in range(1,51):
    cima = x + math.sqrt(y+2)
    div = cima / 3
    linha = div + i**2 - y**5
    soma = soma + linha
print('somatorio', soma)
