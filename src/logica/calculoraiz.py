import math

class matematicas():
    
    def raizCuadrada(self, numero, iteraciones):
        x=1.0
        for i in range(1, iteraciones):
            x=(x+numero/x)/2
        return x

    def raizCuadradaNegativo(self, numero, iteraciones):
        
        if numero<0:
            raise ValueError("No se puede calcular la raiz Cuadrada de Numeros Negativos")
        
        return math.sqrt(numero)