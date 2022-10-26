import random
def sorteia_questao(dic,nivel):
    questoes = dic[nivel]
    sorteada = random.choice(questoes)
    return sorteada