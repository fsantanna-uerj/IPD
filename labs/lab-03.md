<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 3: Repetição
====================

- Fazer todos os itens em um único arquivo, ex., `lab-03.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-03, João da Silva
    - *Anexos*:
        - `lab-03.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```

## 1.

Faça um programa que leia números continuamente até que seja digitado `0`.
Ao final, o programa deve exibir a soma de todos os números lidos.

## 2.

Faça um programa que leia 10 números e, ao final, exiba o maior.

## 3.

O Campeonato Brasileiro está na reta final com 20 times na disputa.
Uma vitória vale 3 pontos, um empate vale 1 ponto e uma derrota vale 0 pontos.
Escreva um programa que, para cada time, leia o nome, número de vitórias,
número de empates e número de derrotas.
Ao final, o programa deve escrever o nome dos times com mais e menos pontos até
o momento.

## 4.

Considere o programa a seguir:

```
n1 = input()
n2 = input()
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

Considere o programa a seguir:

```
n1 = input()
n2 = input()
n3 = input()
while n1 > 0:
    print "n2", n2
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

O que o programa está fazendo? Descreva ``em bom português'' o significado do
programa.                          
Em outras palavras, explique o que o programa está calculando.
