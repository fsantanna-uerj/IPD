<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 2: Condicionais
=======================

- Fazer todos os itens em um único arquivo, ex., `lab-02.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: IPD, lab-02, João da Silva
    - *Anexos*:
        - `lab-02.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```

## 1.

Faça um programa que leia dois valores e exiba o maior valor lido.

## 2.

Um aluno de IPD está indo aos Estados Unidos e quer comprar um celular novo.
Ele não quer gastar mais do que 1000 reais. Um dólar está custando 3.17 reais.
Faça um programa que leia o preço de um celular em dólares e, caso seja um bom
negócio, escreva `BOM NEGÓCIO`.

## 3.

Agora o aluno alugou um carro.
Ele está preocupado com o limite de velocidade, mas não entende muito bem
o sistema de milhas por hora (mph).
Ele pretende manter sempre uma velocidade entre 80 e 100 quilômetros por hora
(kph).
Sabe-se que que 1 milha tem aproximadamente 1.6 quilômetros.
Crie um programa que leia a velocidade atual do carro em mph e escreva na tela
`ACELERE`, `DESACELERE` ou `MANTENHA`.

## 4.

Considere o programa a seguir:

```
n1 = input()
n2 = input()
q = 0
while n1 >= n2:
    q = q + 1
    n1 = n1 - n2
r = n1
print("Resposta", q, r)
```

- Teste o programa com várias entradas diferentes.
- Usando a funcionalidade de *Debug -> Debugger*, acompanhe os valores que `q`
  e `v` assumem durante a execução do programa.
- O que o programa está calculando?
  Em outras palavras, qual é o significado de `q` e `r`?
