M1 = [ [0]*4 ] * 3
print(M1)

M2 = [ [0]*2, [0]*2 ]
print(M2)
for i in range(2):
    for j in range(2):
        M2[i][j] = input('n['+str(i)+']['+str(j)+']: ')
print(M2)

M3 = []
for i in range(0,2):
    M3.append([])
    for j in range(0,2):
        v = input('n['+str(i)+']['+str(j)+']: ')
        M3[i].append(v)
print(M3)

soma = 0
for i in range(0,2):
    for j in range(0,2):
        v = M3[i][j]
        if v%2 == 0:
            soma = soma + v
print('pares', soma)

soma = 0
for i in range(0,2):
    for j in range(0,2):
        v = M3[i][j]
        if i==j:
            soma = soma + v
print('diag-1', soma)

soma = 0
for i in range(0,2):
    v = M3[i][i]
    soma = soma + v
print('diag-2', soma)
