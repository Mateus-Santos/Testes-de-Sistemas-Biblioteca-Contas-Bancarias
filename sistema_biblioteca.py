livros = []
livros_emprestados = []

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
	for livro in livros:
		if (livro[1] == verifique):
			return "Livro encontrado"
	return "Esse livro não existe." 


def listar_livros():
	for livro in livros:
		print(livro)
	return "Livros listados"


def listar_livros_emprestados():
	for livro in livros_emprestados:
		print(livro)
	return "Livros emprestados foram listados"


def emprestimo(livro_id):
	for l in livros:
		if(l[1] == livro_id):
			livros_emprestados.append(l)
			livros.remove(l)
			return "Livro emprestado com sucesso."
	return "Este livro já foi emprestado."

def devolucao(livro_id):
	for l in livros_emprestados:
		if(l[1] == livro_id):
			livros.append(l)
			livros_emprestados.remove(l)
			return "Livro devolvido com sucesso."
	return "Empréstimo não encontrado."
