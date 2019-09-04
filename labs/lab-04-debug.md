<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 4: Repetição (2)
========================

## 1.

Considere o programa a seguir:

```
n1 = int(input())
n2 = int(input())
q = 0
while n1 >= n2:
    q = q + 1
    n1 = n1 - n2
r = n1
print("Resposta", q, r)
```

- Teste o programa com várias entradas diferentes.
- Usando a funcionalidade de *Debug -> Debugger*, acompanhe os valores que `q`
  e `v` assumem durante a execução do programa.
- O que o programa está calculando?
  Em outras palavras, qual é o significado de `q` e `r`?

## 2.

Considere o programa a seguir:

```
n1 = int(input())
n2 = int(input())
n3 = int(input())
while n1 > 0:
    print("n2", n2)
    v = n3
    while v > 0:
        n2 = n2 + 1
        v = v - 1
    n1 = n1 - 1
```

Considere que o usuário digitou os seguintes valores para o programa acima:

```
# Entrada de Dados
3
10
5
```

Usando a funcionalidade de *Debug -> Debugger*, transcreva o estado da memória
(conteúdo das variáveis) e saída na tela (efeito dos `print`).

A simulação para a primeira linha já está transcrita a seguir:

```
# Estado da Memória
# Variável valor1 valor2 valor3 ...
# -------- ------ ------ ------
  n1            3



```

```
# Tela do Computador
# ------------------



```

O que o programa está fazendo? Descreva "em bom português" o significado do
programa.                          
Em outras palavras, explique o que o programa está calculando.
