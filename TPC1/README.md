# TPC 1
PL 2024

## Aluno

**Nome:** Guilherme Oliveira

**ID:** a95021

### Resumo

Este TPC consistiu em criar um programa para análise de dados originários de um ficheiro **CSV**. Para isto teríamos que ler o dataset, processá-lo e criar os seguintes resultados:

- Lista ordenada alfabeticamente das modalidades desportivas;

- Percentagens de atletas aptos e inaptos para a prática desportiva;

- Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

### Implementação

Para a implementação do programa doram criados os seguintes ficheiros:

- **csv_to_list.py**

- **funcs.py**

- **main.py**

##### csv_to_list.py

Neste ficheiro encontrámos apenas a função **to_list** que transforma um ficheiro csv numa lista de dicionários com os dados do mesmo.

##### funcs.py

Em funcs.py encontrámos todas as funções que recebem a lista de dados criada em csv_to_list e retornam os diversos dados pedidos.

##### main.py

Ficheiro onde se encontra a função main onde está implementado o menu de interação com o utilizador e onde são chamadas as funções presentes nos pacotes referidos acima.