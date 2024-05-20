import math
import unittest
from src.logica.calculoraiz import matematicas


class RaizCuadrada(unittest.TestCase):
    
    def setUp(self):
        self.calcularraiz = matematicas()
    
    def tearDown(self):
        self.calcularraiz = None
    
    def test_calcularraiz(self):
        numero=9
        iteraciones=4
        resultado_esperado = math.sqrt(9)
        resultado_actual = self.calcularraiz.raizCuadrada(numero, iteraciones)
        
        self.assertAlmostEqual(resultado_esperado, resultado_actual, 0)    #el cero indica la cantidad de decimales que se van a comparar
        #self.assertEqual(resultado_esperado, resultado_actual)
    
    def test_raizCuadrada_numeroNegativo(self):
        numero = -4
        iteraciones = 10
        #resultado_esperado = -2
        
        with self.assertRaises(ValueError) as context:
            self.calcularraiz.raizCuadradaNegativo(numero, iteraciones)
        
        self.assertEqual(str(context.exception), "No se puede calcular la raiz cuadrada de numeros negativos")

if __name__=='__main__':
    unittest.main()
    