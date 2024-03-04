# TPC 3
**PL 2024**

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

## Resumo

Este TPC teve como objetivo criar um programa que devolvesse a **soma de números** presentes num texto tendo em conta se o modo soma estava ***on*** ou ***off***

## Implementação

De forma a chegar ao objetivo, foram implementados os seguintes ficheiros:

### - somador.py

Neste ficheiro encontram-se as seguintes duas funções:

- **split_text** - recebe um texto e cria uma lista onde são armazenados todos os **on**, **off**, **'='** e **números** presentes no texto, pela ordem que aparecem no mesmo;

- **soma** - recebe a lista criada na função acima e percorre-a, caso o elemento atual seja um **on** irá atualizar a variável ***estado_soma*** para *true* (soma on), se o elemento for **off** atualiza para *false* (soma off), se o elemento for um **número** adiciona esse número à soma atual e se dor **=** dá print no terminal do valor atual da soma.


### - main.py

Na função ***main*** fazemos a leitura do ficheiro que queremos analisar, de seguida aplicámos-lhe a função ***split_text*** e por fim a função **soma** para obtermos os resultados esperados.