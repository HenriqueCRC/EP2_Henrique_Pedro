def questao_para_texto(dic,ID):
    string = ''
    primeira_linha = ('QUESTÃO {0}'.format(ID))
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