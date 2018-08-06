<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 10: Simulado P2
=======================

<!--
- Fazer todos os itens em um único arquivo, ex., `lab-10.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-10, João da Silva
    - *Anexos*:
        - `lab-10.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```
-->

## 1.

A operação `random.randrange(0,2)` retorna `0` ou `1` aleatoriamente, toda vez
que é executada.
Para usá-la, é preciso importar o módulo `random`:

```
import random
print(random.randrange(0,2))        # exibe 0 ou 1
print(random.randrange(0,2))        # exibe 0 ou 1
print(random.randrange(0,2))        # exibe 0 ou 1
```

Crie um programa que, a partir de uma lista `L` qualquer, crie uma nova lista
`M` onde cada elemento da lista `L` tem 50% de chance de aparecer.

Exemplo:

```
L = [1,2,3,4,5]
...         # sua solucao
print(M)    # M possível [1,3,4]
```

## 2.

Crie um programa que leia do teclado uma frase `F` e guarde em uma lista `L`
quantas vezes cada letra do alfabeto aparece.
Em seguida, o programa deve exibir o resultado na tela conforme o formato a
seguir:

```
a 13
b 0
...
z 1
```

Assuma que só aparecem letras minúsculas na frase.

## 3.

Crie um programa que, a partir de matrizes `M` e `N` quaisquer, calcule a
matriz produto `P` entre elas.

Assuma que as matrizes `M` e `N` são multiplicáveis, i.e., que o número de
colunas de `M` é igual ao número de linhas de `N`.
