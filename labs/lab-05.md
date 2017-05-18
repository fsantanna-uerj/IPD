<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 5: Simulado P1
======================

- Fazer todos os itens em um único arquivo, ex., `lab-05.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-05, João da Silva
    - *Anexos*:
        - `lab-05.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```

## 1.

Um aluno de IPD está nos Estados Unidos durante o outono e precisa decidir se
vai sair na rua de blusa (a partir de 25C), casaco leve (a partir de 15C) ou
casaco pesado (caso esteja ainda mais frio).
Lá, as temperaturas são exibidas em Fahrenheit, que pode ser convertido para
graus Celcius através da seguinte fórmula:

    C = (F-32) * 5/9

Faça um programa que leia a temperatura em Fahreneheit e escreva na tela
*VÁ DE BLUSA* ou *VÁ DE CASACO LEVE* ou *VÁ DE CASACO PESADO*, dependendo do
valor lido.
Faça um programa que leia números continuamente até que seja digitado `0`.
Ao final, o programa deve exibir o maior valor e quantas vezes esse valor foi
digitado.

## 2.

A pizzaria da UERJ está com uma promoção em que a pizza de 8 pedaços está
saindo a 20 reais.
Considere que uma pessoa sempre come exatamente 2 pedaços de pizza.
Faça um programa que leia o número de pessoas em uma mesa e escreva

a) o total de pizzas a pedir,
b) o total em reais a pagar,
c) a quantidade de pedaços que serão desperdiçados.

## 3.

Uma cidade está fazendo uma eleição entre os seguintes candidatos:

1. Maria da Vendinha
2. Toninho Sorriso
3. Doutora Neide
4. Mãozinha

A eleição é eletrônica e o eleitor digita apenas o número do seu candidato.
A quantidade de eleitores deve ser digitada pelo operador imediatamente antes
da votação.
Não há segundo turno.

Crie um programa que
- leia a quantidade de eleitores;
- leia os votos de todos os eleitores, um de cada vez;
- exiba o nome e o total de votos de cada candidato;
- exiba o número de votos inválidos;
- exiba o nome do candidato eleito e o seu percentual de votos.

## 4.

Considere o programa a seguir:

```
print "Seja Bem-vindo..."
n1 = input()
n2 = input()
r1 = 0
while n1 >= 0:
    c1 = 1
    while c1 <= n2:
        n1 = n1 - 1
        c1 = c1 + 1
    r1 = r1 + 1
    print "n1", n1, "r1", r1
r1 = r1 - 1
r2 = n1 + n2
print "A resposta é ", r1, r2
```

Considere que, para o programa acima, o usuário digitou os números a seguir:

```
5
2
```

a) Simule a execução do programa considerando a entrada e transcreva o estado
   da memória (conteúdo das variáveis) e saída na tela (efeito dos `print`).

A simulação para as duas primeiras linhas já está transcrita a seguir:

```
# Estado da Memória
# Variável val1 val2 val3 ...
# -------- ---- ---- ----
  n1          5    ?    ?
  n2          ?    ?    ?



# Tela do Computador
# ------------------
Seja Bem-vindo...
```

b) O que o programa está fazendo? Descreva "em bom português" o significado
   do programa.                          
   Em outras palavras, explique o que o programa faz para alguém que não sabe
   programar.
