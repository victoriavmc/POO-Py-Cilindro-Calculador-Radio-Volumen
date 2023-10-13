# Esta clase se proporciona métodos para solicitar y validar la entrada del usuario, ya sea para números flotantes o enteros.

class Validacion:
    def __init__(self, texto=""):
        self.__texto = texto

     # GETS: permite obtener el valor del atributo privado
    def getTexto(self):
        return self.__texto

    # SETS: permiten establecer el valor del atributo privado, inicializarlo o cambiarlo
    def setTexto(self, pTexto):
        self.__texto = pTexto

    # Esta clase se utiliza para solicitar al usuario que ingrese un numero flotante. Para ello hace uso de un bucle para que el usuario pueda continuar ingresando un numero hasta que ingrese una valor valido.
    def pedirNumeroFlotante(self):
        while True:
            try:
                numero = float(input(f'  Ingrese {self.getTexto()}: '))
            except ValueError:
                print(
                    'Debe ingresar número flotantes. \n                          Intente nuevamente!')
            else:
                if numero >= 0.1:
                    return numero
                else:
                    return ('Debe ingresar número flotantes positivos. \n                            Intente nuevamente!')

# Su funcion es la misma que "pedirNumeroFlotante", solo que en vez de pedir valores flotantes pide enteros.
    def pedirNumeroEntero(self):
        while True:
            try:
                numero = int(input(f'  Ingrese {self.getTexto()}: '))
            except ValueError:
                print(
                    'Debe ingresar número enteros. \n                          Intente nuevamente!')
            else:
                if numero >= 1:
                    return numero
                else:
                    return ('Debe ingresar número enteros positivos. \n                            Intente nuevamente!')
