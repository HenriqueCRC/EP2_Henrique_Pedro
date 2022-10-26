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