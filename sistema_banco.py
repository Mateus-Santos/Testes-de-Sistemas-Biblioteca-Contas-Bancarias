usuarios = []

def Criacao_conta(usuario):
    usuarios.append(usuario)
    return "Usuário cadastrado com sucesso"


def Deletar_conta(deletar):
    for item in usuarios:
        if (item[1] == deletar[0] and item[3] == deletar[1]):
            usuarios.remove(item)
            return "Conta deletada com sucesso"
    return "Conta nao encontrada"

def Alterar_limite(alterar):
    for item in usuarios:
        if(item[1] == alterar[0] and item[3] == alterar[1]):
            #está faltando o valor que deve ser alterar...
            return "Limite alterado com sucesso"
    return "Nao foi possivel alterar o limite"

def Receber_emprestimo(emprestimo):
    for item in usuarios:
        if(item[1] == emprestimo[0] and item[3] == emprestimo[1]):
            #deveria ter o valor do emprestimo como parametro...
            return "Operação feita com sucesso"
    return "Nao foi possivel fazer a operacao"

def Transferencia_bancaria(transferencia):
    for item in usuarios:
        if(item[1] == transferencia[0] and item[3] == transferencia[1]):
            return "Operação feita com sucesso"
    return "Nao foi possivel fazer a operacao"

def Saque(sacar):
    for item in usuarios:
        if(item[1] == sacar[0] and item[3] == sacar[1]):
            return "Operação feita com sucesso"

    return "Nao foi possivel fazer a operacao"

def Solicitar_emprestimo(solicitar):
    for item in usuarios:
        if(item[1] == solicitar[0] and item[3] == solicitar[1]):
            return "Operação feita com sucesso"
    return "Nao foi possivel fazer a operacao"

def Verificar_saldo(verificar):
    for item in usuarios:
        if(item[1] == verificar[0] and item[3] == verificar[1]):
            return "Operação feita com sucesso"
    return "Nao foi possivel fazer a operacao"

def Verificar_limite(limite):
    for item in usuarios:
        if(item[1] == limite[0] and item[3] == limite[1]):
            return "Operação feita com sucesso"
    return "Nao foi possivel fazer a operacao"

    #O ultimo teste não foi possivel ser realizado pois falta o nome da função :(
