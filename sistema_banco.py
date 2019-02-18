def Criacao_conta(usuario):
	usuarios = []
	usuarios.append(usuario)
	return "Usuário cadastrado com sucesso"


def Deletar_conta(deletar):
    usuarios = [["1", "12312312325", "Lucas", "1234"]]
    for item in usuarios:
        if (item[1] == deletar[0] and item[3] == deletar[1]):
        	usuarios.remove(item)
            return "Conta deletada com sucesso"
    else:
        return "Conta nao encontrada"

 def Alterar_limite(alterar):

 	return "Limite alterado com sucesso"