import unittest
import sistema_biblioteca

#Grupo: Allanderson, Daniel, Felipe e Jefferson

class MyModuleTest(unittest.TestCase):

	def teste_calc1(self):
		self.assertEqual(sistema_biblioteca.cad_livro(["Harry Potter", "2487536952148", "EU"]), "Livro cadastrado com sucesso")
	def teste_calc2(self):
		self.assertEqual(sistema_biblioteca.excluir_livro("2487536952148"), "Livro removido com sucesso.")
	def teste_calc3(self):
		self.assertEqual(sistema_biblioteca.verificar("2487536952148"), "Esse livro não existe.")
	def teste_calc4(self):
		self.assertEqual(sistema_biblioteca.verificar("1987536955487"), "Esse livro não existe.")
	def teste_calc5(self):
		self.assertEqual(sistema_biblioteca.listar_livros(), "Livros listados")
	def teste_calc6(self):
		self.assertEqual(sistema_biblioteca.listar_livros_emprestados(), "Livros emprestados foram listados")
	def teste_calc7(self):
		self.assertEqual(sistema_biblioteca.emprestimo("2487536952148"),"Este livro já foi emprestado.")
	def teste_calc8(self):
		self.assertEqual(sistema_biblioteca.emprestimo("2487536952148"),"Livro emprestado com sucesso.")
	def teste_calc9(self):
		self.assertEqual(sistema_biblioteca.devolucao("2487536952148"), "Livro devolvido com sucesso.")
	def teste_calc10(self):
		self.assertEqual(sistema_biblioteca.devolucao("2487536952148"), "Empréstimo não encontrado.")


if __name__ == '__main__':
	unittest.main()