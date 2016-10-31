<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 1
=========

Ao final, enviar o *print screen* da tela de edição e da tela de execução.

Listas
------

<https://github.com/fsantanna/IPD/blob/master/oficial/Python/4-Python%20-%20Vetores-expanded.pdf>

1. .
    - criar uma lista `l1` com os valores *1,2,3,4*
    - exibir a lista
    - exibir o tamanho da lista
    - exibir o 3o elemento da lista (deve exibir o valor *3*)
2. .
    - criar uma lista `l2` com 100 zeros
    - exibir a lista
    - exibir o tamanho da lista
3. .
    - criar uma lista `l3` vazia
    - exibir a lista
    - ler e inserir 2 elementos novos na lista
    - exibir novamente a lista
4. .
    - criar uma lista `l4` vazia
    - ler e inserir 10 elementos novos na lista usando
      `for` ou `while` (*loop*)
    - exibir a lista
5.   .
    - percorrer a lista `l4` com um *loop*
    - exibir os valores da lista maiores que 5
6. .
    - criar uma lista `l6` vazia
    - percorrer a lista `l4` e guardar os valores maiores que 5 em `l6`
    - exibir `l6`
7. .
    - criar uma lista `l7` vazia
    - percorrer a lista `l4` e guardar os **índices** dos valores maiores que 5
      em `l7`
    - exibir `l7`
8. .
    - criar uma lista `l8` vazia
    - percorrer a lista `l4` e guardar os índices e valores maiores que 5 em `l8`
    - exibir `l8`

Funções
-------

<https://github.com/fsantanna/IPD/blob/master/slides/ipd-06-funs.pdf>

O código a seguir define a função `soma` que recebe dois valores como
parâmetros e retorna a soma entre eles:

```
def soma (v1, v2):
    return v1 + v2
```

Para usar a função, basta usar o nome e passar os argumentos desejados:

```
r1 = soma(10,20)
print(r1)

a = 100
b = 200
r2 = soma(a,b)
print(r2)
```

9. .
    - definir a função `celsius_para_fahrenheit` que recebe uma temperatura
      em *celsius* e a converte para *fahrenheit* (`°C  x  9/5 + 32 = °F`)
    - usar a função e exibir os resultados para 3 exemplos

10. .
    - definir uma função `maiores_que_5` que recebe uma lista e retorna uma
      nova lista com os valores maiores que 5
    - usar a função e exibir os resultados para 3 exemplos

