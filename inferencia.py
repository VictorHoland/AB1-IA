
# Probabilidades de cada  diagnóticos de forma individual(sem receber as entradas)
p_covid = 1/3
p_resfriado = 1/3
p_gripe = 1/3

class Doencas:
    def __init__(self, covid, resfriado, gripe):
        self.covid = covid
        self.resfriado = resfriado
        self.gripe = gripe

# Função para verificar se uma string pode ser traduzida de forma direta para número inteiro
def is_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Função para perguntar ao usuário quais sintomas o mesmo apresenta
def apresentou(sintoma):
    print("Você aprensenta " + sintoma + "?")
    print("{1} Sim     |     {2} Não")
    while 1:
        entrada = input()
        if entrada == '1':
            return True
        elif entrada == '2':
            return False
        else:
            print("Entre um valor válido: {1} ou {2}")

# Função para saber quão intenso é um sintoma
def intensidade(sintoma):
    print("Qual a intensidade " + sintoma + "? Digite o número correspondente a opção")
    print("{1} Leve     |     {2} Moderado     |     {3} Intenso")
    while 1:
        intensidade_sintoma = input()
        if is_int(intensidade_sintoma):
            if 0 < int(intensidade_sintoma) < 4:
                return int(intensidade_sintoma)
            else:
                print("Digite um valor dentro das opções disponíveis")
        else:
            print("Tente novamente, apenas números inteiros são aceitos")

def tipo_de_tosse(sintoma):
    print("Qual o tipo da " + sintoma + "? Digite o número correspondente a opção")
    print("{1} Seca     |     {2} Com secreção")
    while 1:
        intensidade_sintoma = input()
        if is_int(intensidade_sintoma):
            if 0 < int(intensidade_sintoma) < 3:
                return int(intensidade_sintoma)
            else:
                print("Digite um valor dentro das opções disponíveis")
        else:
            print("Tente novamente, apenas números inteiros são aceitos")

def intensidade2(sintoma):
    print("Qual a duração da " + sintoma + "? Digite o número correspondente a opção")
    print("3 dias  |  3 dias - 7 dias  |     mais de 7 dias")
    while 1:
        intensidade_sintoma = input()
        if is_int(intensidade_sintoma):
            if 0 < int(intensidade_sintoma) < 4:
                return int(intensidade_sintoma)
            else:
                print("Digite um valor dentro das opções disponíveis")
        else:
            print("Tente novamente, apenas números inteiros são aceitos")

# Função que entregará um resultando partindo das informações recebidas como entrada
def sistema_especialista(febre, grau_febre, tempo_febre,
                         dor_corpo, intensidade_corpo,
                         dor_cabeca, intensidade_cabeca, fadiga, intensidade_fadiga,
                         tosse, intensidade_tosse,tipo_tosse, falta_ar,
                         congestao_nasal):

    eventos_covid = []
    eventos_resfriado = []
    eventos_gripe = []
    doente = True

    if not febre and not dor_corpo and not dor_cabeca and not fadiga and not tosse and not falta_ar and not congestao_nasal:
        doente = False
        print('\nProvavelmente, você não está com covid, resfriado ou gripe\n')

    if not febre and doente:
        febre_chance = febre_prob()
        eventos_covid.append(febre_chance.covid)
        eventos_resfriado.append(febre_chance.resfriado)
        eventos_gripe.append(febre_chance.gripe)

    if febre:
        temperatura = febre_temperatura(grau_febre)
        duracao_febre = febre_duracao(tempo_febre)
        eventos_covid.append(temperatura.covid)
        eventos_resfriado.append(temperatura.resfriado)
        eventos_gripe.append(temperatura.gripe)
        eventos_covid.append(duracao_febre.covid)
        eventos_resfriado.append(duracao_febre.resfriado)
        eventos_gripe.append(duracao_febre.gripe)

    if dor_corpo:
        corpo_chance = corpo_prob()
        corpo_intensidade = corpo_dor(intensidade_corpo)
        eventos_covid.append(corpo_chance.covid)
        eventos_resfriado.append(corpo_chance.resfriado)
        eventos_gripe.append(corpo_chance.gripe)
        eventos_covid.append(corpo_intensidade.covid)
        eventos_resfriado.append(corpo_intensidade.resfriado)
        eventos_gripe.append(corpo_intensidade.gripe)

    if dor_cabeca:
        cabeca_chance = cabeca_prob()
        cabeca_intensidade = cabeca_dor(intensidade_cabeca)
        eventos_covid.append(cabeca_chance.covid)
        eventos_resfriado.append(cabeca_chance.resfriado)
        eventos_gripe.append(cabeca_chance.gripe)
        eventos_covid.append(cabeca_intensidade.covid)
        eventos_resfriado.append(cabeca_intensidade.resfriado)
        eventos_gripe.append(cabeca_intensidade.gripe)

    if fadiga:
        fadiga_intensidade = fadiga_dor(intensidade_fadiga)
        eventos_covid.append(fadiga_intensidade.covid)
        eventos_resfriado.append(fadiga_intensidade.resfriado)
        eventos_gripe.append(fadiga_intensidade.gripe)

    if tosse:
        tosse_tipo = tosse_dif(tipo_tosse)
        tosse_intensidade = tosse_dor(intensidade_tosse)
        eventos_covid.append(tosse_tipo.covid)
        eventos_resfriado.append(tosse_tipo.resfriado)
        eventos_gripe.append(tosse_tipo.gripe)
        eventos_covid.append(tosse_intensidade.covid)
        eventos_resfriado.append(tosse_intensidade.resfriado)
        eventos_gripe.append(tosse_intensidade.gripe)

    if falta_ar:
        chance_falta_ar = falta_ar_chance()
        eventos_covid.append(chance_falta_ar.covid)
        eventos_resfriado.append(chance_falta_ar.resfriado)
        eventos_gripe.append(chance_falta_ar.gripe)

    if congestao_nasal:
        congestao_chance = congestao_prob()
        eventos_covid.append(congestao_chance.covid)
        eventos_resfriado.append(congestao_chance.resfriado)
        eventos_gripe.append(congestao_chance.gripe)

    if len(eventos_covid) > 0 and len(eventos_resfriado) > 0 and len(eventos_gripe) > 0:
        probabilidades = bayesiano(eventos_covid, eventos_resfriado, eventos_gripe)

        if probabilidades.covid > probabilidades.resfriado and probabilidades.covid > probabilidades.gripe:
            print('\n<<==============================================================>>')
            print('Doença com maior probabilidade: covid')
            print('<<==============================================================>>\n')

        if probabilidades.resfriado > probabilidades.covid and probabilidades.resfriado > probabilidades.gripe:
            print('\n<<==============================================================>>')
            print('Doença com maior probabilidade: resfriado')
            print('<<==============================================================>>\n')

        if probabilidades.gripe > probabilidades.resfriado and probabilidades.gripe > probabilidades.covid:
            print('\n<<==============================================================>>')
            print('Doença com maior probabilidade: gripe')
            print('<<==============================================================>>\n')


# Função para cálculo das probs Bayesianas
def bayesiano(eventos_covid, eventos_resfriado, eventos_gripe):
    numerador_covid = p_covid
    numerador_resfriado = p_resfriado
    numerador_gripe = p_gripe

    for i in range(0, len(eventos_covid)):
        numerador_covid = numerador_covid * eventos_covid[i]
        numerador_resfriado = numerador_resfriado * eventos_resfriado[i]
        numerador_gripe = numerador_gripe * eventos_gripe[i]

    denominador = numerador_covid + numerador_resfriado + numerador_gripe
    covid = numerador_covid/denominador
    resfriado = numerador_resfriado/denominador
    gripe = numerador_gripe/denominador

    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dada a presença ou não de febre
def febre_prob():
    covid = 0.5
    resfriado = 0.2
    gripe = 0.5
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dada a temperatura da febre
def febre_temperatura(grau_febre):
    if grau_febre < 38:
        covid = 1
        gripe = 0.5
        resfriado = 1
    else:
        covid = 1
        gripe = 1
        resfriado = 0.2

    return Doencas(covid, resfriado, gripe)

# Função que atualiza as probabilidades de cada doença dada a duração da febre
def febre_duracao(tempo_febre):
    if 0 < tempo_febre <= 2:
        covid = 0.5
        resfriado = 1
        gripe = 0.2
    elif 2 < tempo_febre <= 4:
        covid = 0.5
        resfriado = 0.5
        gripe = 1
    else:
        covid = 1
        resfriado = 0.2
        gripe = 0.5
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dado o surgimento de dor corpo
def corpo_prob():
    covid = 1 / 3
    resfriado = 2 / 3
    gripe = 1
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dada a intensidade da dor corpo
def corpo_dor(intensidade_corpo):
    if intensidade_corpo == 1:
        covid = 0.5
        resfriado = 1
        gripe = 0.2
    elif intensidade_corpo == 2:
        covid = 0.5
        resfriado = 0.2
        gripe = 0.5
    else:
        covid = 0.5
        resfriado = 0
        gripe = 1
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dado o surgimento de dor de cabeça
def cabeca_prob():
    covid = 0.5
    resfriado = 0.5
    gripe = 1
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dada a intensidade da dor de cabeça
def cabeca_dor(intensidade_cabeca):
    if intensidade_cabeca == 1:
        covid = 0.5
        resfriado = 1
        gripe = 0.2
    elif intensidade_cabeca == 2:
        covid = 0.5
        resfriado = 0.2
        gripe = 0.5
    else:
        covid = 0.5
        resfriado = 0
        gripe = 1
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dada a intensidade da fadiga
def fadiga_dor(intensidade_fadiga):
    if intensidade_fadiga == 1:
        covid = 0.5
        resfriado = 0.5
        gripe = 0.5
    else:
        covid = 1
        resfriado = 0
        gripe = 1

    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dada a intensidade da tosse
def tosse_dor(intensidade_tosse):
    if intensidade_tosse == 1:
        covid = 0.5
        resfriado = 1
        gripe = 0.5
    else:
        covid = 1
        resfriado = 0
        gripe = 1
    return Doencas(covid, resfriado, gripe)

def tosse_dif(tipo_tosse):
    if tipo_tosse == 1:
        covid = 1
        resfriado = 0.2
        gripe = 1
    else:
        covid = 0.2
        resfriado = 1
        gripe = 0.5
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dado o surgimento de falta de ar
def falta_ar_chance():
    covid = 1
    resfriado = 0.2
    gripe = 0.2
    return Doencas(covid, resfriado, gripe)

# Função que atualiza a probabilidade de cada doença dado o surgimento de congestao nasal
def congestao_prob():
    covid = 0.2
    resfriado = 1
    gripe = 0.5
    return Doencas(covid, resfriado, gripe)