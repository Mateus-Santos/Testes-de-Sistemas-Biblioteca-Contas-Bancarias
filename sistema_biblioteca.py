livros = []

def cad_livro(livro):
	livros.append(livro)
	return "Livro cadastrado com sucesso"


def excluir_livro(excluir):
	for livro in livros:
		if(livro[1] == excluir):
			livros.remove(livro)
			return "Livro removido com sucesso."
	return "Livro não encontrado"


def verificar(verifique):
	for v in livros:
		if (v[1] == verifique):
			return "Livro encontrado"
	return "Esse livro não existe." 


def listar_livros():
	for l in livros:
		print(l)

	return "Livros listados"


def listar_livros_emprestados():
	for l in livros:
		print(l)
	return "Livros emprestados foram listados"


def emprestimo(livro):
	for l in livros:
		if(l[1] == livro):
			livros.remove(livro)
			return "Livro emprestado com sucesso."
	return "Este livro já foi emprestado."

def devolucao(livro):
	for l in livros:
		if(l[1] == livro):
			return "Livro já foi devolvido"
	#precisa de mais informações do livro para devolver de verdade...
	return "Livro devolvido com sucesso."

