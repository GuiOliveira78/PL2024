
# Função que recebe uma lista de dados e devolve
# uma lista de todas as modalidades ordenadas alfabeticamente
def modalidades(dados):
    
    modalidades = []
    
    for atleta in dados:
        if atleta["modalidade"] not in modalidades:
            modalidades.append(atleta["modalidade"])
    
    modalidades.sort()
    
    return modalidades

# Função que calcula a percentagem de atletas aptos
def aptos(dados):
    
    aptos = 0
    
    for atleta in dados:
        if atleta["resultado"] == 'true':
            aptos += 1
            
    percentagem = str(aptos/(len(dados))*100) + '%'
    return percentagem

# Função que calcula a percentagem de atletas inaptos
def inaptos(dados):
    
    inaptos = 0
    
    for atleta in dados:
        if not atleta["resultado"] == 'false':
            inaptos += 1
            
    percentagem = str(inaptos/(len(dados))*100) + '%'
    return percentagem

# Função que calcula a percentagem de aptos e inaptos apenas numa travessia
def aptos_e_inaptos(dados):
    aptos = 0
    inaptos = 0
    for atleta in dados:
        if atleta["resultado"] == 'true':
            aptos += 1
        else:
            inaptos += 1
            
    percentagens = []
    percentagens.append(str(aptos/(len(dados))*100) + '%')
    percentagens.append(str(inaptos/(len(dados))*100) + '%')
    return percentagens

# Função que cria uma lista de listas de intervalos etários de 5 anos
# Exemplo: [[0,1,2,3,4],[5,6,7,8,9],...]
def cria_intervalos(max):
    i = 0
    intervalos = []
    while i < max:
        lista = []
        j = i
        while j != i+5:
            lista.append(j)
            j += 1 
        i = j
        intervalos.append(lista)


    return intervalos

# Função que cria um dicionário para os escalões etários e associa cada atleta ao respetivo escalão
def intervalos(dados):
    dic = {}
    
    intervalos = cria_intervalos(45)
    
    for intervalo in intervalos:

        intervalo_str = f"({intervalo[0]}-{intervalo[-1]})"
        dic[intervalo_str] = []  
        
    for atleta in dados:
        idade = int(atleta['idade'])
        for intervalo in intervalos:
            if idade in intervalo:
                dic[f"({intervalo[0]}-{intervalo[-1]})"].append(atleta['nome/primeiro'] + ' ' + atleta['nome/último'])
                
    return dic
