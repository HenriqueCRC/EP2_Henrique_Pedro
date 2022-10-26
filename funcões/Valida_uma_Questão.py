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