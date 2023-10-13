# Se importan las clases Cilindro y Radio desde los archivos "claseCilindro" y "ClaseRadio", respectivamente. 
from claseCilindro import Cilindro
from claseRadio import Radio

# Esta clase al igual que la clase Radio, representa una caracteristica comun presente en las figuras geometricas.
# Sus metodos son heredados de la clase Cilindro y se utiliza polimorfismo
class Volumen(Cilindro): #Se define una nueva clase llamada Volumen
    def __init__(self, diametro, altura):
        super().__init__(diametro, altura) #Hereda de la clase Cilindro. Esto significa que la clase Volumen heredará los atributos y métodos de la clase Cilindro.

    #Polimorfismo
    """
    la clase "Volumen" se utiliza para calcular y mostrar el volumen de un cilindro, aprovechando la herencia de la clase "Cilindro" y utilizando una instancia de la clase "Radio" para calcular el radio del cilindro. 
   El código utiliza el polimorfismo al proporcionar su propia implementación de los métodos formula y mostrar manteniendo la misma firma que los métodos en la clase base Cilindro.
    """
    # funcion la cual recibe un parametro ingresado para poder calcular el radio del cilindro
    def formula(self):
        radio = Radio(self.getDiametro())
        volumen = self.getPi() * (radio.formula() ** 2) * self.getAltura()
        super(Volumen, self).formula() #No es necesario
        return volumen

    # funcion que imprime en pantalla el resultado
    def mostrar(self):
        return f'El volumen del cilindro es de {round(self.formula(),2)} metros cúbicos'
