import os
import time


#                               FUNÇÕES
# ================================================================================
def limpatela():  # FUNÇÃO PARA LIMPAR A TELA
    os.system('cls' if os.name == 'nt' else 'clear')


def dic_list(dicnary):  # FUNCÇÃO PARA RECEBER O DICIONÁRIO E TRANSFORMA-LO EM UMA LISTA

    chave = dicnary.keys()
    valor = dicnary.values()
    key_list = list(chave)
    value_list = list(valor)
    value_list.sort()

    for i, item in enumerate(key_list):
        print(f'[{i}] {item}: R$ {value_list[i]}')
    return ''


def produto(produtos):  # FUNÇÃO PARA RESGATAR O NOME DO PRODUTO.
    valor = produtos.items()

    produto = []
    for item, value in valor:
        produto.append(item)
    return produto


def preco(valores):  # FUNÇÃO PARA RESGATAR O VALORES DO PRODUTO.
    valor = valores.items()
    preco = []
    for item, value in valor:
        preco.append(value)
    return preco


def padronizar_texto(texto):  # FUNÇÃO PARA PADRONIZAR TEXTO
    texto = texto.upper()
    texto = texto.replace(" ", "")

    return texto


def opcoes_inicio():  # OPÇÕES DE ESCOLHA
    print('OPÇÕES: ')
    print('')
    print('[1] Medicamentos')
    print('[2] Cuidado Infatil')
    print('[3] Cuidado Feminino')
    print('[0] CAIXA')


def opcoes_medicamento():  # MEDICAMENTO
    print('MEDICAMENTOS: ')
    print('')
    print('[1] Dor de Cabeça')
    print('[2] Ginecológicos')
    print('[3] Ancologicos (Tratamento para cancêr)')
    print('[4] Tratamento dermatológico')
    print('[0] Aperte 0 PARA VOLTAR.')

def opcoes_infatis(): #INFANTIS
        print('INFANTIL: ')
        print('')
        print('[1] Fraldas')
        print('[2] Pomadas')
        print('[3] Sabonetes')
        print('[4] Shampoos')

def caixa_eletronico(soma):
    print(f'R$ {soma:.2f}')
    valor_total = soma
    print(f'R$ {valor_total:.2f}')

    print('OPÇÕES: \n [0] CARTÃO DE DÉBITO (2% DE ACRESCIMO) \n [1] CARTÃO DE CRÉDITO (4% DE ACRESCIMO) \n [2] PAGAMENTO VIA PIX (3% DE DESCONTO): ')
    opcao_de_pagamento = int(input('Qual seria a forma de pagamento?(DE ACORDO COM OS NÚMERO) '))
    while True:
        if opcao_de_pagamento == 0:
                porcentagem2 = valor_total * 2
                porcentagem2_valor = porcentagem2 / 100
                total = soma + porcentagem2_valor
                print(f'Valor a ser pago: R${total:.2f}')
                 
                break
                  
        elif opcao_de_pagamento == 1:
                porcentagem2 = valor_total * 4
                porcentagem2_valor = porcentagem2 / 100
                total = soma + porcentagem2_valor

                print(f'Valor a ser pago: R${total:.2f}')
                break
        elif opcao_de_pagamento == 2:
                porcentagem2 = valor_total * 3
                porcentagem2_valor = porcentagem2 / 100
                total = soma - porcentagem2_valor

                print(f'Valor a ser pago: R${total:.2f}')
                break
        else:
            print('OPÇÃO INVÁLIDA. NADA FOI ADICIONADO.')
            back = input('APERTE ENTER: ')
            if back == '' or padronizar_texto(back):
                limpatela()
            return caixa_eletronico(valor_soma_clientes)
# ================================================================================


# =======================ESTOQUE==================================================
headache = {
    'Dorflex Sanofi 50cps (Dipirona)': 24.90,
    'Neosaldina Dip 1g 20cps (Dipirona)': 18.38,
    'Paracetamol + Cafeína (Genérico)': 19.89
}

diapers = {
    'Fralda D. Babysec Ultra-Sec-XG 60u': 60.95,
    'Fralda D. Huggies Supreme-Care-Hiper-G 66u': 112.90,
    'Fralda D. Ever-Care-Baby-XG 20u': 26.90
}
# =======================ESTOQUE==================================================


name = input('Olá, sou uma IA de vendedora de farmácia e me chamo Hana, qual o seu nome? ')
print('')
print(f'Olá {name}, Seja bem vindo ao FARMAUSE. ***Peço que daqui para frente use apenas NÚMEROS como resposta.***')

time.sleep(2)

cliente_list_produto = []
cliente_list_valores = []
valor_soma_clientes = sum(cliente_list_valores) #SERÁ USADO APENAS PARA O PAGAMENTO DO CAIXA. PODE SER VISTO NA LINHA 184 À 192

while True:

    print('')
    print(f'R$ {sum(cliente_list_valores):.2f}')

    opcoes_inicio()

    number = int(input('No que eu posso ajudar? '))
    limpatela()

    if number == 0:  # CAIXA ELETRÔNICO
        lista = []

        print('CARRINHO DE COMPRA')
        print('')
        for i, itens in enumerate(cliente_list_produto):
            print(f'{cliente_list_produto[i]}: R$ {cliente_list_valores[i]}')

        if cliente_list_produto == lista:
            print('Volte sempre.')

        else:
            print('')
            Back_take = input('RETIRAR ALGO OU PAGAR? [R/P]:  ')

            if padronizar_texto(Back_take) == 'R': #PAGAMENTO COM OPÇÃO DE ESCOLHA PARA RETIRAR.
                tamanho = 1 - 2
                tamanho2 = tamanho
                limpatela()
                for i, itens in enumerate(cliente_list_produto):
                    tamanho2 = tamanho2 + 1
                    print(f'[{tamanho2}] {cliente_list_produto[i]}: R$ {cliente_list_valores[i]}')
                print('')
                print('USE APENAS NÚMEROS')
                print('')
                remove = int(input('Qual deseja tirar? '))

                limpatela()

                cliente_list_produto.pop(remove)
                cliente_list_valores.pop(remove)

                print('ITEM RETIRADO COM SUCESSO.')
                print('')
                for i, itens in enumerate(cliente_list_produto):
                    tamanho2 = tamanho2 + 1
                    print(f'[{tamanho2}] {cliente_list_produto[i]}: R$ {cliente_list_valores[i]}')
                
                limpatela()
                valor_soma_clientes = sum(cliente_list_valores)
                
                caixa_eletronico(valor_soma_clientes) 

            elif padronizar_texto(Back_take) == 'P':#PAGAMENTO DIRETO

                limpatela()
                valor_soma_clientes = sum(cliente_list_valores)
                
                caixa_eletronico(valor_soma_clientes) 
        break

    elif number == 1:  # 1° ESCOLHA
        # opções
        opcoes_medicamento()
        numer0 = int(input('O que deseja? '))
        limpatela()

        if numer0 == 0:  # RETORNA PARA O INÍCIO
            limpatela()
            print('BEM VINDO DE VOLTA')
            continue

        if numer0 == 1:  # CONTINUA O CÓDIGO (1° OPÇÃO)
            limpatela()
            print(f'R$ {sum(cliente_list_valores):.2f}')
            print('')

            print(dic_list(headache))

            while True:

                Produto_name = produto(headache)
                Preco_produto = preco(headache)

                Qtd = int(input('Quantos produtos deseja? '))  # RODAR A QUANTIDADE DE VEZES Q EU QUERO.

                for i in range(Qtd):

                    index = int(input('Qual produto deseja (DE ACORDO COM O NÚMERO DA LISTA)? '))
                    if index in Preco_produto or Preco_produto:
                        try:
                            cliente_list_produto.append(Produto_name[index])
                            cliente_list_valores.append(Preco_produto[index])
                            cliente_list_valores.sort()
                        except:
                            print('OPÇÃO INVÁLIDA. NADA FOI ADICIONADO.')
                            back = input('APERTE ENTER: ')
                            if back == '' or padronizar_texto(back):
                                limpatela()
                            break

                print(f'*Valor atual: R$ {sum(cliente_list_valores):.2f}*')

                inicio_adicionar = input('Algo a mais? [S/N] ')
                if padronizar_texto(inicio_adicionar) == 'S':  # Volta para o início
                    print('')
                    print('VOLTANDO...')
                    time.sleep(2)
                    limpatela()

                    print(f'R$ {sum(cliente_list_valores):.2f}')
                    print('')
                    print(f'Bem vindo de volta! {name}')
                    print('')
                    print(dic_list(headache))
                    continue

                else:
                    limpatela()
                    break



    elif number == 2:  # 2° ESCOLHA.
        opcoes_infatis()
        numer0 = int(input('O que deseja? '))
        limpatela()

        if numer0 == 0:  # RETORNA PARA O INÍCIO
            limpatela()
            print('BEM VINDO DE VOLTA')
            continue

        if numer0 == 1:  # CONTINUA O CÓDIGO (1° OPÇÃO)
            limpatela()
            print(f'R$ {sum(cliente_list_valores):.2f}')
            print('')

            print(dic_list(diapers))

            while True:

                Produto_name = produto(diapers)
                Preco_produto = preco(diapers)

                Qtd = int(input('Quantos produtos deseja? '))  # RODAR A QUANTIDADE DE VEZES Q EU QUERO.

                for i in range(Qtd):

                    index = int(input('Qual produto deseja (DE ACORDO COM O NÚMERO DA LISTA)? '))
                    if index in Preco_produto or Preco_produto:
                        try:
                            cliente_list_produto.append(Produto_name[index])
                            cliente_list_valores.append(Preco_produto[index])
                            cliente_list_valores.sort()
                        except:
                            print('OPÇÃO INVÁLIDA. NADA FOI ADICIONADO.')
                            back = input('APERTE ENTER: ')
                            if back == '' or padronizar_texto(back):
                                limpatela()
                            break

                print(f'*Valor atual: R$ {sum(cliente_list_valores):.2f}*')

                inicio_adicionar = input('Algo a mais? [S/N] ')
                if padronizar_texto(inicio_adicionar) == 'S':  # Volta para o início
                    print('')
                    print('VOLTANDO...')
                    time.sleep(2)
                    limpatela()

                    print(f'R$ {sum(cliente_list_valores):.2f}')
                    print('')
                    print(f'Bem vindo de volta! {name}')
                    print('')
                    print(dic_list(diapers))
                    continue

                else:
                    limpatela()
                    break

