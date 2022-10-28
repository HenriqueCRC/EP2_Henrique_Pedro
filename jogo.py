import random
from dados import base_dados
from funcoes import base_fun

lista_dados_nova=[]

for questao in base_dados.quest:
    validada = base_fun.valida_questao(questao)
    if validada == {}:
        lista_dados_nova.append(questao)

# Transforma base de questões
dados_novo = base_fun.transforma_base(lista_dados_nova)

rodar_questao = True
lista_ja_sorteadas = []
ja = 0
dinheiro = 0
pulos = 3
ajuda = 2
n = 1
lista_ajuda = []
lista_dificuldade = ['facil','facil','facil','medio','medio','medio', 'dificil','dificil','dificil']
i = 0
lista_premio = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_quant_respostas = []
lista_alternativas = ['A','B','C','D','ajuda','pula','parar']
continuar = True

# Início do jogo

print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')

pergunta_nome = input('Digite seu nome:')

print(f'Ok {pergunta_nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ')
tecla_para_continuar = input('Aperte ENTER para continuar...')
print('O jogo já vai começar! Lá vem a primeira questão! ')
print('Vamos começar com questões do nível {0}!'.format(lista_dificuldade[i]))
tecla_para_continuar = input('Aperte ENTER para continuar...')

# Início Do Loop
while rodar_questao == True:
    # utilizei apenas o sorteia uma questao inedita, pois eu ja utilzo o valida questao no valida questao inedita
    ja_foi_sorteada = base_fun.sorteia_questao_inedida(dados_novo,lista_dificuldade[i],lista_ja_sorteadas)
    mostrar_questao = base_fun.questao_para_texto(lista_ja_sorteadas[ja],n)
    correta = lista_ja_sorteadas[ja]['correta']
    if len(lista_quant_respostas) == 3:
            print('Você passou para o nível MÉDIO!')
    if len(lista_quant_respostas) == 6:
            print('Você passou para o nível DIFÍCIL!')
    print(mostrar_questao)
    resposta = input('Qual sua resposta?').upper()
    while resposta not in lista_alternativas:
        print('Opção inválida!')
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
        while continuar == True:
            resposta = input('Qual sua resposta?').upper()
            if resposta in lista_alternativas:
                break
            else:
                print('Opção inválida!')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    if resposta == 'ajuda':
        dica = base_fun.gera_ajuda(lista_ja_sorteadas[ja])
        if ajuda == 0:
            print('Não deu! Você não tem mais direito a ajuda!')
            passar = input('Aperte ENTER para continuar...')
        if len(lista_ajuda) == 0:
            lista_ajuda.append(1)
            ajuda -= 1
            print('Ok, lá vem ajuda! Você ainda tem {0} ajudas!'.format(ajuda))
            (dica)
            passar = input('Aperte ENTER para continuar...')
        elif len(lista_ajuda) != 0:
            lista_ajuda.append(1)
            print('Não deu! Você já pediu ajuda nesta questão!')
            passar = input('Aperte ENTER para continuar...')
    elif resposta == 'pula':
        pulos -= 1
        if pulos == 0:
            print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
            ja += 1
        elif pulos > 0:
            print('Ok, pulando! Você ainda tem {0} pulos!'.format(pulos))
            ja += 1
        elif pulos <= 0:
            print('Não deu! Você não tem mais direito a pulos!')
    elif resposta == 'parar':
        sim_nao = input('Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {0}!'.format(dinheiro))
        if sim_nao == 'S':
            print('Ok! Você parou e seu prêmio é de R$ {0}'.format(dinheiro))
            rodar_questao = False
            break
    elif resposta == correta:
        dinheiro = lista_premio[i]
        if dinheiro == 1000000:
            ('PARABÉNS, agora você está rico!')
            break
        i += 1
        n += 1
        ja += 1
        lista_quant_respostas.append(1)
        lista_ajuda = []
        print(f'Você acertou! Seu prêmio atual é de R$ {dinheiro}')
        passar = input('Aperte ENTER para continuar...')
    elif resposta != correta:
        print('Que pena! Você errou e vai continuar pobre')
        break


