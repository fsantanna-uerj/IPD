<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 8: Strings
==================

<https://github.com/fsantanna-uerj/IPD/blob/master/slides/ipd-07-strings.pdf>

1. .
    - ler do teclado a string `s`
    - exibir o tamanho da string
    - exibir o primeiro e último caracteres usando índices positivos
    - exibir o primeiro e último caracteres usando índices negativos
2. .
    - ler do teclado as strings `s1` e `s2`
    - concatenar (unir) as duas strings lidas em `s3` separadas por um espaço
    - exibir `s3`
3. .
    - ler do teclado uma string `s`
    - ler do teclado um caractere `c`
        - (um caractere nada mais é do que uma string de tamanho `1`)
    - exibir a quantidade de vezes que `c` aparece em `s`
4. .
    - ler do teclado a string `s`
    - exibir todos os códigos numéricos correspondentes aos caracteres de `s`
    - guardar em uma lista `l` todos os códigos numéricos correspondentes
      aos caracteres de `s`
    - usar a função `ord`
5. .
    - ler do teclado uma lista `l` de `5` números
    - converter `l` para uma string `s`
        - cada valor `l[i]` corresponde ao código numérico de `s[i]`
    - usar a função `chr`
6. .
    - ler do teclado uma string `s`
    - exibir na tela a string `s` com todos os seus caracteres convertidos para
      maiúsculas
    - ex., se `s` for `"olabomdia"`, o programa deve exibir `"OLABOMDIA"`
7. .
    - considerando o exercício anterior, converter *somente* os caracteres do
      nosso alfabeto para maiúsculas
    - ex., se `s` for `"ola, bom dia!"`, o program deve exibir `"OLA, BOM DIA!"`
8. .
    - ler do teclado uma string `s`
    - converter cada letra do alfabeto para a letra seguinte
        - o `a` deve ser convertido para `b`
        - o `b` deve ser convertido para `c`
        - ...
        - **o `z` deve ser convertido para `a`**
    - exibir o texto convertido
9. .
    - o caractere especial `'\n'` representa "quebra de linha" em uma string
    - exibir a string "ola\nmundo" e verificar a exibição na tela
    - ler do teclado uma string `s`
    - transformar e exibir a string `s` da seguinte forma:
        - toda vez que a string tiver um ponto final seguido de um espaço,
          trocar os dois por uma quebra de linha
    - ex., se `s` for `"Bom dia. Aqui sou eu. Tudo bem?"`, o programa deve exibir:

```
Bom dia
Aqui sou eu
Tudo bem?
```

10. .
    - ler do teclado uma string `texto`
    - ler do teclado uma outra string `sub`
    - exibir quantas vezes a string `sub` aparece dentro de `texto`
    - ex., a string `"na"` aparece 2 vezes dentro de `"banana"`
    - **Nessa questão é necessário usar um while dentro de outro while!**
