import lib
from unittest import TestCase

class Test_hmw(TestCase):
	def teste_recebe_Lucas_retorna_1(self):
		frase = "Lucas"
		resultado_esperado = 1

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_Lucas_Souza_retorna_2(self):
		frase = "Lucas Souza"
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_Lucas_Souza_espaco_retorna_2(self):
		frase = "Lucas Souza "
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_espaco_Lucas_Souza_retorna_2(self):
		frase = " Lucas Souza"
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_espaco_Lucas_Souza_espaco_retorna_2(self):
		frase = " Lucas Souza "
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_espaco_Lucas_espacos_Souza_espaco_retorna_2(self):
		frase = " Lucas  Souza "
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_espacos_Lucas_espacos_Souza_espaco_retorna_2(self):
		frase = "  Lucas  Souza "
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_espacos_Lucas_espacos_Souza_espacos_retorna_2(self):
		frase = "  Lucas  Souza  "
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_del_Lucas_del_Souza_del_retorna_2(self):
		frase = "**Lucas**Souza**"
		resultado_esperado = 2

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_crazy(self):
		frase = "**(&#121481**  --.+@hshduhs.;/w7 37=  -&&Lucas*())_+*Souza**- *++-**"
		resultado_esperado = 6

		resultado_obitido = lib.how_many_words(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

class Test_rp(TestCase):
	def teste_recebe_Lucas_retorna_Lucas(self):
		frase = "Lucas"
		resultado_esperado = "Lucas"

		resultado_obitido = lib.reverse_phrase(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)

	def teste_recebe_menosLucasast_retorna_astLucasmenos(self):
		frase = "-Lucas*"
		resultado_esperado = "*Lucas-"

		resultado_obitido = lib.reverse_phrase(frase)

		self.assertEqual(resultado_esperado, resultado_obitido)
