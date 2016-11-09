<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 2: Funções
==================

Ao final, enviar o *print screen* da tela de edição e da tela de execução.

Sugestões:

- Fazer todos os itens em um único arquivo, ex., `lab-02.py`.
- Enviar o arquivo para o seu e-mail.
  **Ao desligar a máquina, todos os arquivos são removidos do computador.**

Funções
-------

<https://github.com/fsantanna/IPD/blob/master/slides/ipd-06-funs.pdf>

<https://github.com/fsantanna/IPD/blob/master/oficial/Python/6-Python%20-%20Modularizacao-expanded.pdf>

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

1. .
    - definir a função `celsius_para_fahrenheit` que recebe uma temperatura
      em *celsius* e a converte para *fahrenheit* (`°C  x  9/5 + 32 = °F`)
    - usar a função e exibir os resultados para 3 exemplos
2. .
    - definir uma função `maiores_que_5` que recebe uma lista e retorna uma
      nova lista com os valores maiores que 5
    - usar a função e exibir os resultados para 3 exemplos
3. .
    - resolva um exercício qualquer da lista entre o 18 e 32 (exceto 23,26,30)
    - use pelo menos uma função no exercício
    - <https://github.com/fsantanna/IPD/blob/master/oficial/lista-02-algos.pdf>
    - (quanto mais alunos resolverem um exercício, menos ele vale)
