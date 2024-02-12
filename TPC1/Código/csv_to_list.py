import sys

# Função que transforma um ficheiro numa lista de dicionários
def to_list():
    
    # Lista que irá conter todos as rows
    dados = []
    
    # Lista que contém os campos do ficheiro CSV
    keys = sys.stdin.readline().strip().split(',')
    
    for line in sys.stdin:
        row = line.rstrip().split(',')
        
        # Inicialização do dicionário
        dic = {}
        
        for i in range(len(row)):
            dic[keys[i]] = row[i]

        dados.append(dic)
        
    return dados
