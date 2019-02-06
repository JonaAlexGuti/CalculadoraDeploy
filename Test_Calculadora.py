import unittest
from unittest import TestCase
from Calculadora import Calculadora
class TestCalculadora(unittest.TestCase):
	
	def test_suma_2_mas_2(self):
		cal=Calculadora()
		self.assertEquals(4,cal.suma(2,2))

if __name__ == '__main__':
	unittest.main()
