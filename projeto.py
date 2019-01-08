from menu import menu
from funcoes import *

while True:
    menu()
    opcao = int(input('Digite aqui sua opção: '))
    if opcao == 1:
        data = input('Digite aqui a data(Formato Norte-Americano(ANO-MES-DIA)): ').lower()
        valor = float(input('Digite aqui o valor: '))
        descricao = input('Digite aqui a descrição: ').lower()
        pagar = True
        receber = False
        escolha = input('dinheiro,cheque ou cartao: ').lower()
        if escolha == 'dinheiro':
            dinheiro = True
            cheque, cartao = False, False
        elif escolha == 'cheque':
            cheque = True
            dinheiro, cartao = False, False
        elif escolha == 'cartao':
            cartao = True
            dinheiro, cheque = False, False

        else:
            print('Opção inválida')
        contas_pagar(data, descricao, valor, pagar, receber, cartao, dinheiro, cheque)
    elif opcao == 2:
        data = input('Digite aqui a data(Formato Norte-Americano(ANO-MES-DIA)): ').lower()
        valor = float(input('Digite aqui o valor: '))
        descricao = input('Digite aqui a descrição: ').lower()
        pagar = False
        receber = True
        escolha = input('dinheiro,cheque ou cartao:').lower()
        if escolha == 'dinheiro':
            dinheiro = True
            cheque, cartao = False, False
        elif escolha == 'cheque':
            cheque = True
            dinheiro, cartao = False, False
        elif escolha == 'cartao':
            cartao = True
            dinheiro, cheque = False, False
        else:
            print('Opção inválida')
        contas_receber(data, descricao, valor, pagar, receber, cartao, dinheiro, cheque)
    elif opcao == 3:
        ver_saldo()
    elif opcao == 4:
        mostrar_ultima_conta()
    elif opcao == 5:
        descricao = input('Digite a descrição da conta: ')
        buscar_por_descricao(descricao)
    elif opcao == 6:
        cod_conta = int(input('Qual o id da conta que deseja apagar: '))
        excluir_conta(cod_conta)
    elif opcao == 7:
        mostrar_contas()
    elif opcao == 8:
        print('Adeus e obrigado por usar nosso programa.')
        break
    else:
        print('Opção inválida')
