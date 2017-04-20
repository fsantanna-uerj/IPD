<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 1: Introdução
=====================

- Fazer todos os itens em um único arquivo, ex., `lab-01.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-01, João da Silva
    - *Anexos*:
        - `lab-XX.py`
        - *print screen* da tela de edição e da tela de execução para cada item
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```

Listas
------

<https://github.com/fsantanna/IPD/blob/master/oficial/Python/4-Python%20-%20Vetores-expanded.pdf>

1. Considere o programa a seguir em português:

```
escreva("Qual a sua idade?")
idade = leia()
se idade >= 18:
    escreva("Voce pode dirigr!")
senao:
    escreva("Voce ainda nao pode dirigr...")
```

Traduza o programa para a linguagem Python e teste a sua execução com diversos
valores.

2. Escreva um programa em Python que leia uma temperatura em Fahrenheit e a
   exiba em Celsius.

3. Considere o programa a seguir em português:

```
n = leia()
v = 1
enquanto n > 0:
    v = v * n
    n = n - 1
escreva("A resposta foi", v)
```

- Traduza o programa para Python e teste a sua execução com diversos valores.
- Usando a funcionalidade de *Debug -> Debugger*, enumere todos os valores que
  a variável `v` assume durante a execução do programa.
- O que o programa está calculando?

4. Escreva um programa em Python que leia um número `n` e exiba todos os
   quadrados de `1` até `n`. Exemplo:

```
> 5     # valor digitado
1
4
9
16
25
```
