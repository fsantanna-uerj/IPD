<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 6: Listas [1/2]
=======================

<!--
- Fazer todos os itens em um único arquivo, ex., `lab-06.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-06, João da Silva
    - *Anexos*:
        - `lab-06.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 8
Não: 9 ao 10
Seguem arquivos em anexo...
```
-->

Listas
------

<https://github.com/fsantanna-uerj/IPD/blob/master/oficial/Python/4-Python%20-%20Vetores-expanded.pdf>

1. .
    - criar uma lista `L1` com os valores *1,2,3,4*
    - exibir a lista
    - exibir o tamanho da lista
    - exibir o 3o elemento da lista (deve exibir o valor *3*)
2. .
    - criar uma lista `L2` com 100 zeros
    - exibir a lista
    - exibir o tamanho da lista
    - alterar o 8o elemento para `50`
    - exibir a lista
3. .
    - criar uma lista `L3` vazia
    - exibir a lista
    - inserir o valor `100` na lista com o seguinte comando:
        - `L3.append(100)`
    - inserir o valor `50` na lista com o seguinte comando:
        - `L3.append(50)`
    - exibir a lista
    - ler do teclado dois valores com `input` e inseri-los na lista usando `L3.append`
    - exibir novamente a lista
4. .
    - criar uma lista `L4` vazia
    - ler do teclado e inserir 10 elementos novos na lista usando um `while`
    - exibir a lista
5. .
    - manter o exercício `4` do jeito que está (não fazer nenhuma alteração nele)
    - percorrer a lista `L4` com um `while`
        - o `i` deve variar de `0` até o tamanho da lista
        - exibir os valores da lista `L4[i]` maiores que 5
6. .
    - manter o exercício `4` do jeito que está
    - criar uma lista `L6` vazia
    - percorrer a lista `L4` e guardar os valores maiores que 5 em `L6`
        - usar `L6.append`
    - exibir `L6`
7. .
    - manter o exercício `4` do jeito que está
    - criar uma lista `L7` vazia
    - percorrer a lista `L4` e guardar os **índices** dos valores maiores que 5
      em `L7`
    - exibir `L7`
8. .
    - manter o exercício `4` do jeito que está
    - criar uma lista `L8` vazia
    - percorrer a lista `L4` e guardar os índices e valores maiores que 5 em `L8`
    - exibir `L8`
9. .
    - criar uma lista `P1` com as notas da P1
    - criar uma lista `P2` com as notas da P2
    - exibir o número de chamada (índice na lista) dos alunos aprovados com média `>= 7`
10. .
    - criar duas listas `LA` e `LB`
    - exibir os valores que aparecem tanto em `LA` quanto em `LB`, ou seja, a
        sua interseção
        - essa questão necessita de um `while` dentro de um `while`
