# Esta super clase sera nuestra base, de la cual se posteriormente heredaremos sus atributos
# Su proposito es crear atributos privados a los cuales aplicaremos absorcion

#La clase Figura es una clase base genérica que puede utilizarse como punto de partida para representar figuras geométricas más específicas. 
#Los atributos privados:  __diametro y __altura son características fundamentales que pueden estar presentes en muchas figuras geométricas.

class Figura:
    def __init__(self, diametro, altura): #Este es el constructor de la clase, que inicializa los atributos
        # Atributos privados
        self.__diametro = diametro
        self.__altura = altura

#El propósito común de los métodos en esta clase es proporcionar un mecanismo controlado para acceder y modificar los atributos privados __diametro y __altura.
 
    # GETS permite obtener el valor del atributo privado 
    def getDiametro(self):
        return self.__diametro

    def getAltura(self):
        return self.__altura

    # SETS permite establecer el valor del atributo privado Inicializarlo o cambiarlo
    def setDiametro(self, pDiametro):
        self.__diametro = pDiametro

    def setAltura(self, pAltura):
        self.__altura = pAltura
