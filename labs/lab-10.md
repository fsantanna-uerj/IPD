<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 10: Simulado P2
=======================

## 1.

A operação `random.randrange(0,2)` retorna `0` ou `1` aleatoriamente, toda vez
que é executada.
É uma espécie de "cara ou coroa" em Python.
Para usá-la, é preciso importar o módulo `random`:

```
import random                       # inclua essa linha no topo do arquivo

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

Crie uma função `inverte` que recebe uma string e retorne uma nova string com
as caixas invertidas (maiúscula vira minúscula e minúscula vira maiúscula).
Os caracteres que não forem letras devem ser mantidos.

Exemplo:

```
inverte("Ola, Tudo bem?")   # retorna "oLA, tUDO BEM?"
```

## 4.

Crie um programa que, a partir de matrizes `M` e `N` quaisquer, calcule a
matriz produto `P` entre elas.

Assuma que as matrizes `M` e `N` são multiplicáveis, i.e., que o número de
colunas de `M` é igual ao número de linhas de `N`.

- Dica: Tente primeiro multiplicar uma matriz `1xN` por uma `Nx1`.
