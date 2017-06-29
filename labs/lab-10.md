<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 10: Simulado P2
=======================

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

## 1.

A função `random.randrange(0,2)` retorna `0` ou `1` aleatoriamente.
Para usá-la, é preciso importar o módulo `random`:

```
import random
print(random.randrange(0,2))        # exibe 0 ou 1
print(random.randrange(0,2))        # exibe 0 ou 1
print(random.randrange(0,2))        # exibe 0 ou 1
```

Crie uma função que receba uma lista e retorne uma nova lista onde cada
elemento da lista original tem 50% de chance de aparecer.

## 2.

Crie um programa que leia do teclado uma frase e guarde em uma lista quantas
vezes cada letra do alfabeto aparece.
O programa deve escrever o resultado na tela conforme o formato a seguir:

```
a 13
b 0
...
z 1
```

Assuma que só aparecem letras minúsculas na frase.

## 3.

1. Crie uma função que receba um número e verifique se ele é primo.
2. Crie um programa que leia um número `N` e imprima os `N` primeiros números
   primos.

## 4.

Crie uma função que receba uma lista de listas e retorne uma nova lista com
todos os elementos de todas as listas.

Exemplo:

```
f([ [1,2], [-1,-1,-1], [100]) -> [1,2,-1,-1,-1,100]
```
