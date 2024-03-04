# TPC 2
**PL 2024**

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

## Resumo
O objetivo deste TPC foi criar um programa que faz a converção de um ficheiro MarkDown para HTML

## Implementação

Para a implementação do programa foram criados os seguintes ficheiros:

- **converter.py**

- **main.py**

### converter.py

Neste ficheiro encontrámos as funções que recebem um texto markdown e o vão transformando num html, tendo cada uma a função de substiruir um tipo de texto.
Assim sendo temos as seguintes funções:

- **convert_title** - converte um título

- **convert_bold** - converte palavras a negrito

- **convert_italico** - converte palavras em itálico

- **convert_blockquote** - converte blocos de código

- **convert_oList** - converte listas ordenadas

- **convert_uList** - converte listas desordenadas

- **convert_link** - converte links

- **convert_img** - converte imagens

- **convert_paragraph** - converte parágrafos

- **converterAll** - junta todas as funções acima fazendo a conversão total do texto


### main.py

Ficheiro onde se encontra a função main onde está implementado o cabeçalho do ficheiro html e onde é invocada a função ***converterAll*** de forma a fazer a conversão do texto.