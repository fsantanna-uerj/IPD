<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 9: Funções
==================

<!--
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
-->

<https://github.com/fsantanna-uerj/IPD/blob/master/slides/ipd-06-funs.pdf>

<https://github.com/fsantanna-uerj/IPD/blob/master/oficial/Python/6-Python%20-%20Modularizacao-expanded.pdf>

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
    - em seguida, escrever um programa que leia uma temperatura em celsius e a
      exiba em fahrenheit
        - o programa deve usar a função definida acima (sem alterá-la)

2. .
    - definir uma função `eh_par` que recebe um número inteiro e retorna `True`
      caso ele seja par ou `False` caso ele seja ímpar
    - em seguida, escrever um programa que leia 10 números em um `while` e
      para cada um deles exiba `EH PAR` ou `EH IMPAR`
        - o programa deve usar a função definida acima (sem alterá-la)

3. .
    - definir uma função `triangulo` que recebe três números, cada um
      correspondendo a um dos lados de um triângulo e retorne uma das três
      opções:
        - `"equilatero"`
        - `"isoceles"`
        - `"escaleno"`
        - `"invalido"`
    - testar a função com alguns exemplos

4. .
    - definir uma função `eh_maiuscula` que recebe um caractere e retorna
      `True` caso ele seja uma letra maiúscula ou `False` caso contrário
    - testar a função com alguns exemplos
5. .
    - definir uma função `eh_alfa_num` que recebe um caracetere e retorna
      `True` caso ele seja uma letra do alfabeto ou um algarismo (ou `False`
      caso contrário)
    - testar a função com alguns exemplos

6. .
    - definir uma função `maiores_que_5` que recebe uma lista e retorna uma
      nova lista com os valores maiores que 5
    - testar a função com alguns exemplos
7. .
    - definir uma função `possui` que recebe uma lista e um valor e retorna
      `True` caso a lista possua o valor passado ou `False` caso contrário

8. .
    - definir uma função `criptografa` que recebe uma string e uma chave, e
      retorna uma nova string criptografada
    - usar o código numérico dos caracteres
        - para cada caractere
            - pegue o seu código numérico
            - some ao código o valor da chave
            - transforme o resultado de volta para um (novo) caractere
9. .
    - definir uma função `descriptografa` que receve uma string criptografada
      e uma chave, e retorna a string original
    - usar o mesmo mecanismo da questão anterior
