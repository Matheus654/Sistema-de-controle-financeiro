import sqlite3

BD = "projetinho.db"


def mostrar_ultima_conta():
    '''Mostra a última conta cadastrada'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "select * from contas order by  cod_conta desc limit 1;"
    cursor.execute(sql)
    conta = cursor.fetchone()
    print('Sua última conta cadastrada:')
    print('Codigo da conta:', conta[0], ' - Data:', conta[1], ' - Descricao:', conta[2], ' - Valor:', conta[3],
          ' - Pagar:',
          conta[4], ' - Receber:', conta[5], ' - Cartao:', conta[6], ' - Dinheiro:', conta[7], ' - Cheque:', conta[8])
    cursor.close()
    conexao.close()
    return conta


def mostrar_contas():
    '''Mostra todas as contas cadastradas no banco de dados'''
    conexao = sqlite3.connect(BD)  # sempre preciso criar conexao com o banco
    sql = "SELECT * FROM contas"
    cursor = conexao.cursor()  # pego os codigos roda no bd
    cursor.execute(sql)
    contas = cursor.fetchall()  # seleciona tudo ta tabela
    if contas.__len__() > 0:
        print('Todas as suas contas:')
        for conta in contas:
            print('Codigo da conta:', conta[0], ' - Data:', conta[1], ' - Descricao:', conta[2], ' - Valor:', conta[3],
                  ' - Pagar:'
                  , conta[4], ' - Receber:', conta[5], ' - Cartao:', conta[6], ' - Dinheiro:', conta[7], ' - Cheque:',
                  conta[8])
    else:
        print("Nenhuma conta cadastrado!")
    cursor.close()
    conexao.close()


def contas_pagar(data, descricao, valor, pagar, receber, cartao, dinheiro, cheque):
    '''Pagar uma conta'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO contas(data,descricao,valor,pagar,receber,cartao,dinheiro,cheque)"
           " VALUES('%s','%s','%d','%s','%s','%s','%s','%s')"
           % (data, descricao, valor, pagar, receber, cartao, dinheiro, cheque))
    cursor.execute(sql)
    cod_conta = cursor.lastrowid
    saldo = mostrar_saldo()
    if saldo >= valor:
        conexao.commit()
        saldo -= valor
        cadastrar_saldo(cod_conta, saldo)
    else:
        print("Tu tá sem money")
        conexao.rollback()
    cursor.close()
    conexao.close()


def contas_receber(data, descricao, valor, pagar, receber, cartao, dinheiro, cheque):
    '''Receber uma conta'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    saldo = mostrar_saldo()
    sql = ("INSERT INTO contas(data,descricao,valor,pagar,receber,cartao,dinheiro,cheque) "
           "VALUES('%s','%s','%d','%s','%s','%s','%s','%s')"
           % (data, descricao, valor, pagar, receber, cartao, dinheiro, cheque))
    cursor.execute(sql)
    cod_conta = cursor.lastrowid
    conexao.commit()
    saldo += valor
    cadastrar_saldo(cod_conta, saldo)
    cursor.close()
    conexao.close()


def mostrar_saldo():
    '''Ver o saldo atual'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "select saldo from saldos order by  id_saldo desc limit  1;"
    cursor.execute(sql)
    saldo = cursor.fetchone()
    if not saldo:
        return 0
    else:
        return saldo[0]
    cursor.close()
    conexao.close()


def ver_saldo():
    '''Verifica o valor do saldo'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "select saldo from saldos order by  id_saldo desc limit  1;"
    cursor.execute(sql)
    saldo = cursor.fetchone()
    if not saldo:
        print('Seu saldo esta zerado')
    else:
        if saldo[0] < 100:
            print('Seu saldo atual é menor que R$ 100,00')
        print('Seu saldo é: R$', saldo[0])
    cursor.close()
    conexao.close()


def cadastrar_saldo(cod_conta, saldo):
    '''Salva o saldo'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO Saldos(cod_conta,saldo) VALUES('%s', '%d')" % (cod_conta, saldo)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print("Saldo Atualizado")
    else:
        conexao.rollback()
        print("Nao foi possivel cadastrar o saldo")
    sal = saldo
    if sal < 100:
        print('Seu saldo atual é menor que R$ 100,00')
    cursor.close()
    conexao.close()


def buscar_por_descricao(descricao):
    '''Encontrar uma conta pela descrição'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    descricao = descricao + '%'
    sql = "SELECT * FROM contas WHERE descricao LIKE '%s'" % descricao
    cursor.execute(sql)
    contas = cursor.fetchall()
    if contas:
        for conta in contas:
            print('Codigo da conta:', conta[0], ' - Data:', conta[1], ' - Descricao:', conta[2], ' - Valor:', conta[3],
                  ' - Pagar:', conta[4], ' - Receber:', conta[5],
                  ' - Cartao:', conta[6], ' - Dinheiro:', conta[7], ' - Cheque:', conta[8])
        return True
    else:
        print("Nenhum produto cadastrado!")
        return False
    cursor.close()
    conexao.close()


def excluir_conta(cod_conta):
    '''Excluir uma conta'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    saldo = mostrar_saldo()
    resposta = input("Deseja realmente excluir esse produto?").lower()
    if resposta == 'sim':
        sql = "DELETE FROM contas WHERE cod_conta='%d'" % cod_conta
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Conta deletada!')
        else:
            conexao.rollback()
            print("Nao foi possivel deletar a conta")
    cursor.close()
    conexao.close()
