'''
    Esta función lo que hará, sera abrir, leer, 
limpiar la cadena de strings de los espacios que tiene en el archivo, 
y convertirlo en una lista.
    Además, controlará y manejará errores que puedan darse en la lista,
utilizando try y except, para que así el programa no se detenga.
    Primero manejará un error muy común que podría darse,
al relacionar un archivo de texto con un script en Pyrthon,
el cual es, que el archivo no exista 
o no se encuentreen el mismo directorio que el script de Python.
    Y el segundo error, también común, es que los elementos dentro de la lista,
no sean del tipo integer o números enteros,
sino floats o strings.
    En esta función también se establecen ciertos condicionales que la lista debe cumplir,
tanto de extensión, como el rango en el cual debe encontrarse los integers en la lista.
'''
def cargar_combinacion(combinacion_secreta):
    '''
    Se utilizarán las excepciones try y except para manejar errores al abrir el archivo, 
    como se solicitó en las instrucciones del proyecto para esta función específica, 
    estas permiten capturar y manejar las excepciones o "errores" sin detener la ejecución del código.
    '''
    try: # Va a contener el código que se intenta ejecutar, si todo funciona bien, entonces el programa continuará con normalidad.

        archivo_combinacion_secreta = open(combinacion_secreta, 'r').read().strip().split()
# La función open() utilizando como argumento el nombre del archivo que queremos abrir, permite hacerlo.
# El método read() imprime todo el contenido del archivo.
# El método split() divide una cadena en subcadenas y las devuelve almacenadas en una lista.
# El método strip() elimina a la izquierda y derecha el carácter que se le introduce. Si se llama sin parámetros elimina los espacios, como en este caso. De esa forma se limpió la cadena.
# Se agruparon estos 3 métodos en una sola línea para que se lean mejor, que el código sea más conciso, lo cual se considera una buena práctica.
    
    except FileNotFoundError:
# Solamente va a ejecutarse, si dentro del bloque try se da un "error", una excepción, en este caso, si el archivo no se encuenta en el mismo directorio que el script de Python.
        
        print(f"Lo sentimos, no se encontró el archivo '{combinacion_secreta}'.")
# Imprime el mensaje de error programado, si llegase a ocurrir el "error"/excepción indicado.
        
        exit(1)
# La función exit() termina la ejecución del programa, en este caso, si no se encuentra el archivo.
# El número 1 dentro de exit() indica que el programa terminó con un error, es una convención en Python para indicar que hubo un problema.
    
    if len(archivo_combinacion_secreta) != 4:
# Aquí se está usando la función len() para verificar que la cantidad de elementos en la lista sea exactamente 4, como parámetro dentro del condicional if.

        print("Lo sentimos, el archivo debe contener exactamente 4 números.")
# Si no se cumple la condición de longitud establecida, entonces se imprimirá un mensaje indicando el error al usuario, como se solicitó en las instrucciones.

        exit(1)
# La función exit() termina la ejecución del programa, en este caso, si no se encuentra el archivo.
# El número 1 dentro de exit() indica que el programa terminó con un error, es una convención en Python para indicar que hubo un problema.
    
    '''
    Se utilizarán nuevamente las excepciones try y except 
    para manejar otros errores/excepciones en el archivo,
    en este caso, asegurar que los datos ingresados en la lista, 
    creada con el método split(),
    sean exclusivamente integers o números enteros, 
    estas permiten capturar y manejar las excepciones o "errores" sin detener la ejecución del código.
    '''

    try: # Va a contener el código que se intenta ejecutar, si todo funciona bien, entonces el programa continuará con normalidad.

# Vamos a utilizar una funcionalidad de Python llamada list comprehension (comprensión de listas).

        combinacion = [int(numero) for numero in archivo_combinacion_secreta]
# Las list comprehension permiten crear listas de elementos, en una sola línea de código, haciendo que el código sea más conciso y legible.
# Aquí, la list comprehension va a estar iterando sobre cada elementos de la lista que se creó con el método split() y a la cual llamamos archivo_combinacion_secreta.
# El ciclo for, lo que va a hacer es recorrer cada elemento de la lista archivo_combinacion_secreta, y va a guardar cada elemento de esta lista en la variable numero de forma temporal.
# El int() convierte cada elemento de la lista archivo_combinacion_secreta, que son strings, a integers o números enteros.
# Se utilizan los [] porque se está creando una nueva lista de integers o números enteros, llamada combinacion.
    
    except ValueError:
# Solamente va a ejecutarse, si dentro del bloque try se da un "error", una excepción.
# En este caso, si los elementos en la lista no son números enteros.
        
        print("Lo sentimos, el archivo debe contener solo números enteros.")
# Imprime el mensaje de error programado, si llegase a ocurrir el "error
        
        exit(1)
# La función exit() termina la ejecución del programa, en este caso, si no se encuentra el archivo.
# El número 1 dentro de exit() indica que el programa terminó con un error, es una convención en Python para indicar que hubo un problema.

    if any(numero < 0 or numero > 9 for numero in combinacion):
# Se está utilizando la función any() para verificar si algún elemento de la lista combinacion es menor que 0 o mayor que 9.
# El condicional if verifica si alguno de los números en la lista combinacion cumple con la condición de ser menor que 0 o mayor que 9.
# El or se utiliza para indicar que si alguno de los números es menor que 0 o mayor que 9, entonces se cumple la condición. Da igual si es uno u otro, o ambos.
# El ciclo for, lo que va a hacer es recorrer cada elemento de la lista combinacion, y va a guardar cada elemento de esta lista en la variable numero de forma temporal.
# Los operadores relacionales < y > se utilizan para comparar los números en la lista combinacion con los valores 0 y 9, respectivamente.
        
        print("Lo sentimos, cada número debe estar entre 0 y 9.")
# Imprime el mensaje de error programado si se cumple la condición de que el número sea menor a 0 o mayor a 9
    
    return combinacion
# La función return, en este caso, lo que va a hacer es finalizar la función.
# Va a devolver los valores al lugar donde se llamó a la función combinacion.
# Al ser combinacion una lista, lo que va a hacer es devolver/entregar el contenido de la misma como el resultado de la función cargar_combinación

print(cargar_combinacion("combinacion_secreta.txt"))
# Se llama a la función cargar_combinacion.
# Se le da un argumento a dicha función, el nombre del archivo de texto.
# Imprime el resultado de la función en la terminal.

'''
def crear_tablero():


def imprimir_tablero(tablero):


def leer_intento(nombre_jugador):


def validar_intento(intento_str, historial):


def calculo_resultado(intento_list, combinacion_secreta):


def registro_intento(tablero, fila_idx, intento_list, resultado):


def actualizar_tablero(tablero):


def es_victoria(resultado, contador_intentos):


def fin_del_juego(combinacion_secreta, contador_intentos):


def control_flujo(contador_intentos):


def iniciar_juego():


def volver_a_jugar():


def menu_principal():
'''























# MENÚ PRINCIPAL:

'''
print("Bienvenido a 'Los 4 Monazos'.\n")

while True:
    print("Por favor seleccione alguna de las siguientes opciones:\n1. Jugar\n2. Salir\n")
    
    opcion = input("Ingrese la opción deseada (1 o 2): ")
    
    if opcion == "1":
        print("\nIniciando el juego.\n")
        # Aquí se llamaría a la función que inicia el juego.
        break
    elif opcion == "2":
        print("\nGracias por jugar. Nos vemos pronto. ¡Hasta luego!")
        exit()
    else:
        print("\nOpción inválida. Por favor, ingrese 1 para jugar o 2 para salir.\n")
'''