# Importa las clases Radio y Volumen desde los archivos "claseRadio" y "claseVolumen", respectivamente, para realizar cálculos relacionados con cilindros.
from claseRadio import Radio
from claseVolumen import Volumen
from claseValidacion import Validacion

if __name__ == '__main__':
    
    #El programa se encuentra dentro de un bucle while True, lo que significa que continuará ejecutándose hasta que el usuario elija salir.
    while True:
        
        """Muestra un menú principal con tres opciones:
        Calcular el radio de un cilindro.
        Calcular el volumen de un cilindro.
        Salir del programa."""
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('¡Bienvenida a la calculadora de Cilindros!')
        print("1-Calcular el radio de un cilindro")
        print("2-Calcular el volumen de un cilindro")
        print("9- Salir")
        
        """
        Utiliza la clase Validacion para solicitar al usuario que ingrese una opción (número) válida. Si el usuario ingresa una opción no válida, se le pedirá que lo haga nuevamente.
        """
        txt1= Validacion('el valor de una de las opciones')
        op= txt1.pedirNumeroEntero()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        if op == 1:
            
            """
            Si el usuario elige la opción 1, se solicitará el diámetro del cilindro mediante la clase Validacion y se calculará el radio utilizando la clase Radio. Luego, se muestra el resultado.
            """
            
            txt2=Validacion(' el diametro del cilindro')
            diametro= txt2.pedirNumeroFlotante()
            
            circulo1 = Radio(diametro)
            print(circulo1.mostrar())
                
        elif op==2:
            
            """
            Si el usuario elige la opción 2, se solicitarán el diámetro y la altura del cilindro mediante la clase Validacion, y se calculará el volumen utilizando la clase Volumen. Luego, se muestra el resultado.
            """
            
            txt3=Validacion(' el diametro del cilindro')
            diametroV = txt3.pedirNumeroFlotante()
            
            txt4=Validacion(' la altura del cilindro')
            altura = txt4.pedirNumeroFlotante()
            
            circulo1 = Volumen(diametroV, altura)
            print(circulo1.mostrar())
                
        elif op ==9:
            """
            Si el usuario elige la opción 9, se muestra información sobre el profesor y los estudiantes del programa y se sale del bucle principal, lo que termina la ejecución del programa.
            """
            
            print('''~ VictoriaVMC''')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            break #Salimos del bucle
        
        else:
            
            """
            Si el usuario ingresa una opción que no corresponde a ninguna de las opciones válidas del menú, se le informará que debe ingresar una opción válida y se le pedirá que lo haga nuevamente.
            """
            
            print('Ingrese una opcion valida.')