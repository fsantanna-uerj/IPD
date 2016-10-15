A = input("A: ")
B = input("B: ")

if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

atual = menor
while atual > 0:
    if (maior%atual == 0) and (menor%atual == 0):
        mdc = atual
        break
    atual = atual - 1

print "MDC", mdc

mdc = 0

cont = 0
atual = 1
while atual <= menor:
    if (maior%atual == 0) and (menor%atual == 0):
        cont = cont + 1
        mdc = atual
    atual = atual + 1

print "MDC", mdc, cont
