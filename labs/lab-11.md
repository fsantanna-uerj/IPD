<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 11: Matrizes
===================

<!--
- Fazer todos os itens em um único arquivo, ex., `lab-09.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-09, João da Silva
    - *Anexos*:
        - `lab-09.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4 ao 7
Seguem arquivos em anexo...
```
-->

<https://github.com/fsantanna-uerj/IPD/blob/master/slides/ipd-09-matrizes.pdf>

**Nunca use o operador `*` para construir matrizes (usar `append`).**

1. .
    - criar uma matriz `m1`, ex.:
    ```
    | 1 2 3 |
    | 4 5 6 |
    | 7 8 9 |
    ```
    - exibir a matriz
    - exibir a quantidade de linhas da matriz (assuma que `m1` pode ter diversos formatos).
    - exibir a quantidade de colunas da matriz
    - exibir a 3a coluna da 2a linha da matriz (deve exibir o valor *6*)
2. .
    - criar uma matriz `m2` com `L` linhas e 2 colunas com todos os elementos zerados
    - ler do teclado a quantidade de linhas `L`
    - exibir a matriz
3. .
    - criar uma matriz `m3` `L` x `C` com todos os elementos zerados
    - ler do teclado a quantidade de linhas `L` e colunas `C`
    - exibir a matriz
    - (precisa de *loops* aninhados)
4. .
    - criar uma matriz `m4` vazia
    - ler do teclado a quantidade de linhas `L` e colunas `C`
    - ler do teclado cada um dos `L` x `C` valores da matriz
    - exibir a matriz
    - (precisa de *loops* aninhados)
5. .
    - calcular a soma da diagonal principal de `m4`
6. .
    - exibir a matriz transposta de `m4`

<!--
6.   .
    - definir a função que calcula a soma da diagonal principal de uma matriz:
```
def soma_diagonal (m):
    <...>   # ???

matriz = [ [1,2], [3,4] ]
soma = soma_diagonal(matriz)
print(soma)
```
7. Definir uma função `transposta(M)` que recebe uma matriz e retorna uma nova
   matriz transposta.
-->
