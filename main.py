from inferencia import *

def main():
    print('Seja bem vindo à central de diagnósticos!\n')

    # Loop para recever as principais informações
    print('Deseja realizar uma consulta?\n{1} Sim\n{2} Não')
    entrada = input()
    while 1:
        if entrada == '2':
            break
        elif entrada == '1':

            # Febre
            febre = False
            grau_febre = 0
            tempo_febre = 0
            if apresentou('febre'):
                febre = True
                # Loop para receber a entrada referente a temperatura
                print('Quantos graus celcius de febre você aprensenta? Apresente um valor arredondado e inteiro entre 36 e 41 \n')
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 35 < int(entrada) < 42:
                            grau_febre = int(entrada)
                            break
                        else:
                            print("Temperatura fora do intervalo aceitável, escreva novamente")
                    else:
                        print("Tente novamente, apenas números inteiros são ceitos")

                # Loop para receber a entrada referente ao tempo em que a febre vem persistindo
                print("Por quantos dias a febre vem persistindo? - Digite um valor entre 1 e 7")
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 0 < int(entrada) < 8:
                            tempo_febre = int(entrada)
                            break
                        else:
                            print("Números de dias incompatível com a entrada esperada, escreva novamente (1 a 7 dias)")
                    else:
                        print("Tente novamente, apenas números inteiros são aceitos")

            # Dores no corpo
            dor_corpo = False
            intensidade_corpo = 0
            if apresentou('Dores no corpo'):
                dor_corpo = True
                intensidade_corpo = intensidade('das dores no corpo')

            # Dor de cabeça
            dor_cabeca = False
            intensidade_cabeca = 0
            if apresentou('dor de cabeça'):
                dor_cabeca = True
                intensidade_cabeca = intensidade('da dor de cabeça')

            # fadiga
            fadiga = False
            intensidade_fadiga = 0
            if apresentou('fadiga'):
                fadiga = True
                intensidade_fadiga = intensidade2('da fadiga')

            # tosse
            tosse = False
            intensidade_tosse = 0
            tipo_tosse = 0
            if apresentou('tosse'):
                tosse = True
                intensidade_tosse = intensidade('da tosse')
                tipo_tosse = tipo_de_tosse('da tosse')

            # falta de ar
            falta_ar = False
            if apresentou('falta de ar'):
                falta_ar = True

            # congestao nasal
            congestao_nasal = False
            if apresentou('congestao nasal'):
                congestao_nasal = True

            # Resultado
            sistema_especialista(febre, grau_febre, tempo_febre,
                                 dor_corpo, intensidade_corpo,
                                 dor_cabeca, intensidade_cabeca, fadiga, intensidade_fadiga,
                                 tosse, intensidade_tosse,tipo_tosse, falta_ar,
                                 congestao_nasal)

            print('Deseja realizar um novo atendimento?\n{1} Sim     |     {2} Não')
            while 1:
                entrada = input()
                if entrada == '1' or entrada == '2':
                    break
                else:
                    print("Entre um valor válido: {1} ou {2}")
            if entrada == '2':
                break
            else:
                print('\n\nResponda novamente o questionário\n')

        # Não faz diagnóstico e nem sai do programa
        else:
            print("Comando não reconhecido")

    print("\nAtendimento encerrado")


if __name__ == '__main__':
    main()
