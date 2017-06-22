<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 9: Funções
==================

- Fazer todos os itens em um único arquivo, ex., `lab-09.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-09, João da Silva
    - *Anexos*:
        - `lab-09.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```

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
    - definir uma função `criptografa` que recebe uma string e uma chave, e
      retorna uma nova string criptografada
    - usar o código numérico dos caracteres
        - para cada caractere
            - pegue o seu código numérico
            - some ao código o valor da chave
            - transforme o resultado de volta para um (novo) caractere
4. .
    - definir uma função `descriptografa` que receve uma string criptografada
      e uma chave, e retorna a string original
    - usar o mesmo mecanismo da questão anterior
