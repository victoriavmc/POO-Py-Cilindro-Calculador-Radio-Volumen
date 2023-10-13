#Del archivo "claseCilindro"  importamos "Cilindro"
from claseCilindro import Cilindro

# La clase Radio representa una caracteristica comun en ciertas Figuras
# Hereda de Cilindro el atributo diamtero, y se aplica el polimorfismo en los metodos "formula" y "mostrar"
class Radio(Cilindro):
    def __init__(self, diametro,): #constructor toma un argumento diametro
        super().__init__(diametro, 0.0) #0.0 Es el atributo por defecto de altura, ya que solo se hereda de Cilindro el diametro
    
    #POLIMORFISMO HIJO

    # Se está aplicando el polimorfismo al definir métodos "formula" y "mostrar" en la clase "Radio", que hereda de la clase "Cilindro".
    
    # Con esta funcion calculamos el radio de un cilindro y devuelve el resultado
    def formula(self):
        radio = self.getDiametro() / 2
        return radio

    # Se mostrara el resultado calculado con la funcion anterior
    def mostrar(self):
        return f'El radio del cilindro es de {round(self.formula(),2)} metros cúbicos'
    
