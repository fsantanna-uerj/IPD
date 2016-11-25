arq = open('notas.txt', 'r')

n = 0
soma = 0

maior_nota = -1
maior_nome = ''

for linha in arq:
    nome_nota = linha.split(' ')
    nome = nome_nota[0]
    nota = int(nome_nota[1])

    n = n + 1
    soma = soma + nota

    if nota > maior_nota:
        maior_nome = nome

print(maior_nome)
print(soma/float(n))

arq.close()
