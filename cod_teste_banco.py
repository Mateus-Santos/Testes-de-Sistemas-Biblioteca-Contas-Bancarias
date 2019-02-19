import unittest
import sistema_banco

#Grupo: Allanderson, Daniel, Felipe, Jefferson


class MyModuleTest(unittest.TestCase):
	def teste_calc1(self):
		self.assertEqual(sistema_banco.Criacao_conta(["1", "12312312325", "Lucas", "1234"]), "Usuário cadastrado com sucesso")
	def teste_calc12(self):
		self.assertEqual(sistema_banco.Deletar_conta(["12312312325", "1234"]), "Conta deletada com sucesso")
	def teste_calc13(self):
		self.assertEqual(sistema_banco.Alterar_limite(["12312312325", "1234"]), "Limite alterado com sucesso")
	def teste_calc14(self):
		self.assertEqual(sistema_banco.Receber_emprestimo(["12312312325", "1234"]), "Operação feita com sucesso")
	def teste_calc15(self):
		self.assertEqual(sistema_banco.Transferencia_bancaria(["12312312325", "1234"]), "Operação feita com sucesso")
	def teste_calc16(self):
		self.assertEqual(sistema_banco.Saque(["12312312325", "1234"]), "Operação feita com sucesso")
	def teste_calc17(self):
		self.assertEqual(sistema_banco.Solicitar_emprestimo(["12312312325", "1234"]), "Operação feita com sucesso")
	def teste_calc18(self):
		self.assertEqual(sistema_banco.Verificar_saldo(["12312312325", "1234"]), "Operação feita com sucesso")
	def teste_calc19(self):
		self.assertEqual(sistema_banco.Verificar_limite(["12312312325", "1234"]), "Operação feita com sucesso")
	def teste_calc110(self):
		self.assertEqual((["12312312325", "1234"]), "Operação feita com sucesso")


if __name__ == '__main__':
	unittest.main()