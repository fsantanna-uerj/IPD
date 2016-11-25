arq = open('notas.txt', 'r')
n = 0
soma = 0
for linha in arq:
    nome_nota = linha.split(' ')
    nome = nome_nota[0]
    nota = int(nome_nota[1])
    n = n + 1
    soma = soma + nota
media = (soma / float(n))
arq.close()

arq_r = open('notas.txt', 'r')
arq_w = open('nomes.txt', 'w')
for linha in arq_r:
    nome_nota = linha.split(' ')
    nome = nome_nota[0]
    nota = int(nome_nota[1])
    if nota >= media:
        arq_w.write(nome + '\n')
arq_r.close()
arq_w.close()
