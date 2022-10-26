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