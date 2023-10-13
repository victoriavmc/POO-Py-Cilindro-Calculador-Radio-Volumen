# Del archivo "claseFigura" importamos la clase "Figura"
from claseFigura import Figura
#La clase "Cilindro" hereda de la clase "Figura", lo que significa que "Cilindro" tiene acceso a los atributos y métodos definidos en la clase base "Figura"

# Esta clase representa a la forma geometrica en especifico que se nos solicita en la consigna y de la cual deberemos realizar los calculos.

# Los metodos de "Cilindro" seran utilizados en subclases "Radio" y "Volumen" haciendo uso del polimorfismo
class Cilindro(Figura):
    def __init__(self, diametro, altura): # El constructor de la clase, que inicializa los atributos que obtendremos de la clase padre"Figura"
        # Usamos la funcion super para llamar al constructor de la clase padre "Figura"
        super().__init__(diametro, altura) # Inicializan los atributos heredados
        # Establecemos el valor del atributo privado "pi"
        self.__pi = 3.141593

# Permite obtener el valor de __pi.
    def getPi(self):
        return self.__pi

#POLIMORFISMO 
    # Los siguientes dos métodos se mencionan solamente, pero ambos métodos tienen implementaciones vacías (pass). Esto significa que la clase "Cilindro" espera que las clases derivadas "Radio" y "Volumen" proporcionar sus propias implementaciones.
    def formula(self):
        pass

    def mostrar(self):
        pass
