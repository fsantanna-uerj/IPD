arq = open('notas.txt', 'w')
for i in range(0,3):
    nome = raw_input('nome: ')
    nota = input('nota: ')
    arq.write(nome + ' ' + str(nota) + '\n')
arq.close()
