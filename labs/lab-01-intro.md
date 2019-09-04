<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 1: Introdução
=====================

1. Traduza o programa a seguir de Português para Python:

```
escreva("Qual a sua idade?")
idade <- leia()
exiba("Voce tem " + idade + " anos")
```

2. Considere os dois comandos a seguir:

```
print("1" + "1")
print(1 + 1)
```

Por quê os comandos exibem valores diferentes?

3. Considere os três comandos a seguir:

```
print("1" == 1)
print(int("1") == 1)
print("1" == str(1))
```

- Por quê os comandos exibem valores diferentes?
- Para que servem os comandos `int` e `str`?

-------------------------------------------------------------------------------

4. Crie um programa que leia um salário de uma pessoa e exiba o total a ser
   recebido em um ano.

5. Crie um programa que leia a idade de um pessoa e diga quantos anos faltam
   para ela se aposentar.

6. Crie um programa que leia a altura e peso de uma pessoa e exiba o seu índice
   de massa corporal (IMC).
    - O IMC é o peso em kg dividido pelo quadrado da altura em metros.

7. Crie um programa que leia uma temperatura em Fahrenheit e a exiba em
   Celsius.

-------------------------------------------------------------------------------

8. Traduza o programa a seguir de Português para Python:

```
escreva("Qual a sua idade?")
idade <- leia()
se idade >= 18:
    escreva("Voce pode dirigr!")
senao:
    escreva("Voce ainda nao pode dirigr...")
```

9. Crie um programa que leia a altura e peso de uma pessoa, calcule o seu IMC e
   exiba a sua situação de saúde de acordo com a tabela a seguir:

```
IMC                 SITUAÇÃO
-------------------------------------------
Abaixo de 17 	    Muito abaixo do peso
Entre 17 e 18,49 	Abaixo do peso
Entre 18,5 e 24,99 	Peso normal
Entre 25 e 29,99 	Acima do peso
Entre 30 e 34,99 	Obesidade I
Entre 35 e 39,99 	Obesidade II (severa)
Acima de 40 	    Obesidade III (mórbida)
```

<!--

10. Considere o programa a seguir em Português:

```
n <- leia()
v <- 1
enquanto n > 0:
    v <- v * n
    n <- n - 1
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
-->
