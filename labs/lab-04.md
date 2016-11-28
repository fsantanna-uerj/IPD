<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 4: Strings e Arquivos
=============================

Ao final, enviar o *print screen* da tela de edição e da tela de execução.

Sugestões:

- Fazer todos os itens em um único arquivo, ex., `lab-04.py`.
- Enviar o arquivo para o seu e-mail.
  **Ao desligar, todos os arquivos são removidos do computador.**

Strings
-------

<https://github.com/fsantanna/IPD/blob/master/slides/ipd-07-strings.pdf>

1. .
    - ler do teclado um número `v1`
    - transformar `v1` em uma string `s1`
    - exibir `v1` e `s1` na tela
2. .
    - ler do teclado a string `s2`
    - exibir o tamanho da string
    - exibir o primeiro e último caracteres usando índices positivos
    - exibir o primeiro e último caracteres usando índices negativos
3. .
    - ler do teclado as strings `s31` e `s32`
    - concatenar as duas strings lidas em `s33` separadas por um espaço
    - exibir `s33`
4. .
    - ler do teclado a string `s4`
    - exibir todos os códigos numéricos correspondentes aos caracteres de `s4`
    - guardar em uma lista `l4` todos os códigos numéricos correspondentes
      aos caracteres de `s4`
    - usar a função `ord`
5. .
    - ler do teclado uma lista `l5` de números
    - converter `l5` para uma string `s5`
        - cada valor `l5[i]` corresponde ao código numérico de `s5[i]`
    - usar a função `chr`
6. .
    - ler uma sequência de nomes separados por vírgula
        - o usuário vai digitar algo como 'joao,maria,jose'
    - criar uma lista com cada nome em uma posição
        - e.g., ['joao','maria','jose']
    - verificar se os nomes possuem somente letras
        - e.g., 'joao1' é um nome inválido
    - usar `isalpha` e `split`

Arquivos
--------

<https://github.com/fsantanna/IPD/blob/master/slides/ipd-08-arquivos.pdf>

1. .
    - abrir o arquivo *notas.txt* em modo de escrita
    - escrever no arquivo 3 linhas seguindo o formato *nome nota1 nota2*
    - fechar o arquivo
    - verificar se o arquivo *notas.txt* foi escrito corretamente
2. .
    - abrir o arquivo *notas.txt* em modo de escrita
    - ler do teclado, um por vez, o *nome*, *nota1* e *nota2* de um aluno
    - repetir a leitura até o nome ser a string vazia
    - escrever no arquivos todos nomes e notas seguindo o mesmo formato do
      exercício anterior
    - fechar o arquivo
    - verificar se o arquivo *notas.txt* foi escrito corretamente
3. .
    - abrir o arquivo *notas.txt* em modo de leitura
    - ler as linhas do arquivo, uma a uma, e exibi-las na tela
4. .
    - abrir o arquivo *notas.txt* em modo de leitura
    - ler as linhas do arquivo, uma a uma, e guardá-las em uma lista
        - cada elemento da lista é uma outra lista com o formato
          `[nome, nota1, nota2]`
            - `nome` deve ser uma string
            - `nota1` e `nota2` devem ser números
    - usar a função `split` para separar o nome e as notas
    - usar a função `int` para converter uma string para um número
5. .
    - a partir da lista do exercício anterior, exibir o nome dos alunos com
      média acima de 5.
