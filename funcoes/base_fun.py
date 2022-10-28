import random
def gera_ajuda(dic):
    string = 'DICA:\nOpções certamente erradas:'
    um_ou_dois = random.randint(1,2)
    alternativas = dic["opcoes"]
    correta = dic["correta"]
    lista_alternativas = []
    i = 0
    lista_ajuda = []
    for respostas in alternativas:
        lista_alternativas.append(respostas)

    while i < um_ou_dois:
        sorteada = random.choice(lista_alternativas)
        if sorteada != correta:
            if sorteada not in lista_ajuda:
              lista_ajuda.append(sorteada)
              string += alternativas[sorteada]
              string += ' '
              i += 1
        
    return string
print(gera_ajuda({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}))

#------------------------------------------------------------------------------------------------------

def questao_para_texto(dic,ID):
    string = ''
    primeira_linha = ('\033[34mQUESTÃO {0}\033[m'.format(ID))
    titulo = dic["titulo"]
    respostas = dic["opcoes"]
    string_final = ''
    for letras, alternativas in respostas.items():
        string += letras
        string += ':'
        string += ' '
        string += alternativas 
        string += '\n'
    string_final += '----------------------------------------\n'
    string_final += primeira_linha
    string_final += '\n'
    string_final += '\n'
    string_final += titulo
    string_final += '\n'
    string_final += '\n'
    string_final += 'RESPOSTAS:'
    string_final += '\n'
    string_final += string

    return string_final

#-------------------------------------------------------------------------------------------------------

def sorteia_questao(dic,nivel):
    questoes = dic[nivel]
    sorteada = random.choice(questoes)
    return sorteada

#-------------------------------------------------------------------------------------------------------

def sorteia_questao_inedida(dic,nivel,lista):
    continuar = True
    questoes = dic[nivel]
    sorteada = sorteia_questao(dic,nivel)
    if sorteada in lista:
        while continuar == True:
            sorteada = random.choice(questoes)
            if sorteada not in lista:
                continuar = False
        lista.append(sorteada)
        return sorteada
    else: 
        lista.append(sorteada)
        return sorteada

#------------------------------------------------------------------------------------------------------

def sorteia_questao(dic,nivel):
    questoes = dic[nivel]
    sorteada = random.choice(questoes)
    return sorteada

#-------------------------------------------------------------------------------------------------------

def transforma_base(lista_questoes):
    dic_final = {}
    lista_facil = []
    lista_medio = []
    lista_dificil = []
    if lista_questoes == []:
        return dic_final
    for questao in lista_questoes:
        nivel = questao['nivel']
        if nivel == 'facil':
            lista_facil.append(questao)
        elif nivel == 'medio':
            lista_medio.append(questao)
        else:
            lista_dificil.append(questao)
    if len(lista_facil) != 0:
        dic_final['facil'] = lista_facil
    if len(lista_medio) != 0:
        dic_final['medio'] = lista_medio
    if len(lista_dificil) != 0:
        dic_final['dificil'] = lista_dificil
    return dic_final

#--------------------------------------------------------------------------------------------------------

def valida_questao(questao):
    novo_dic = {}
    lista_keys_principal = ['titulo','nivel','opcoes','correta']
    lista_keys = []
    letras_certas = ['A','B','C','D']
    dic_respostas_vazia = {}
    for chaves in questao:
        lista_keys.append(chaves)
    for chaves in lista_keys_principal:
        if chaves not in lista_keys:
            novo_dic[chaves] = 'nao_encontrado'
    if len(lista_keys) != 4:
        novo_dic['outro'] = 'numero_chaves_invalido'
    if 'titulo' in lista_keys:
        titulo = questao['titulo']
        if titulo.isspace() == True:
            novo_dic['titulo'] = 'vazio'
    if 'nivel' in lista_keys:
        nivel = questao['nivel']
        if nivel != 'facil' and nivel != 'medio' and nivel != 'dificil':
            novo_dic['nivel'] = 'valor_errado'
    if 'opcoes' in lista_keys:
        alternativas = questao['opcoes']
        tamanho = len(alternativas)
        if tamanho != 4:
            novo_dic['opcoes'] = 'tamanho_invalido'
        elif tamanho == 4:
            for letras in alternativas:
                resposta = alternativas[letras]
                if letras not in letras_certas:
                    novo_dic['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                else:
                    if resposta.isspace() == True:
                        dic_respostas_vazia[letras] = 'vazia'
            if len(dic_respostas_vazia) != 0:
                novo_dic['opcoes'] = dic_respostas_vazia
    if 'correta' in lista_keys:
        certa = questao['correta']
        if certa not in letras_certas:
            novo_dic['correta'] = 'valor_errado'
    return novo_dic

#-----------------------------------------------------------------------------------------------------

def valida_questoes(lista):
    lista_final = []
    for questao in lista:
        erros = valida_questao(questao)
        lista_final.append(erros)
    return lista_final
