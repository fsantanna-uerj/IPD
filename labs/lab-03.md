<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 3: Matrizes
===================

Ao final, enviar o *print screen* da tela de edição e da tela de execução.

Sugestões:

- Fazer todos os itens em um único arquivo, ex., `lab-03.py`.
- Enviar o arquivo para o seu e-mail.
  **Ao desligar, todos os arquivos são removidos do computador.**

Listas
------

<https://github.com/fsantanna/IPD/blob/master/oficial/Python/5-Python%20-%20Matrizes-expanded.pdf>

1. .
    - criar uma matriz `m1` (exemplo abaixo)
    - exibir a matriz
    - exibir o número de linhas da matriz (assuma que `m1` pode ter diversos formatos).
    - exibir o número de colunas da matriz
    - exibir a 3a coluna da 2a linha da matriz (deve exibir o valor *6*)
```
| 1 2 3 |
| 4 5 6 |
| 7 8 9 |
```
2. .
    - criar uma matriz `m2` com `l` linhas e 2 colunas com todos os elementos zerados
    - ler do teclado o número de linhas `l`
    - exibir a matriz
3. .
    - criar uma matriz `m3` `l` x `c` com todos os elementos zerados
    - ler do teclado o número de linhas `l` e colunas `c`
    - exibir a matriz
    - (precisa de *loops* aninhados)
4. .
    - criar uma matriz `m4` vazia
    - ler do teclado o número de linhas `l` e colunas `c`
    - ler do teclado cada um dos `l` x `c` valores da matriz
    - exibir a matriz
    - (precisa de *loops* aninhados)
5. .
    - calcular a soma da diagonal principal de `m3`
6.   .
    - definir a função que calcula a soma da diagonal principal de uma matriz:
```
def soma_diagonal (m):
    <...>   # ???

matriz = [ [1,2], [3,4] ]
soma = soma_diagonal(matriz)
print(soma)
```
