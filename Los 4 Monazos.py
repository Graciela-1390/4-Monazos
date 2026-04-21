# ===============================
# Proyecto Final - Los 4 Monazos
# Curso: Introducción a la Programación
# Estudiantes:
# - Anny Graciela Castro Cordero
# - Cristhofer Alexander Martínez Arias
# Profesora: Lincy González Rojas
# Fecha de entrega: 22 de agosto de 2025
# ===============================

# -------------------------------------------------
# Función: generar_codigo_secreto
# Parámetro: ruta (str) -> ruta del archivo donde se guardará el código secreto
# Proceso: solicita al usuario ingresar los 10 dígitos del 0 al 9 en un orden aleatorio y sin repetir,
#          realiza un cálculo matemático para generar el código secreto, y lo guarda en un archivo .txt.
# Devuelve: lista de enteros con la combinación secreta.
# -------------------------------------------------
def generar_codigo_secreto(nombre_archivo):
    print("\nIngrese los 10 dígitos del 0 al 9 en un orden aleatorio, sin repetir: ")
    print("Ejemplo: 5920874316")

    while True:
        secuencia = input("\nDigite la secuencia: ").strip() # Quita espacios al inicio y al final.
        lista_secuencia = list(secuencia) # Convierte la cadena en una lista de caracteres.

        if len(lista_secuencia) != 10: # Valida que haya exactamente 10 elementos.
            print("\nError: Debe ingresar exactamente 10 números.")
            continue 

        todos_validos = True # Valida que todos sean dígitos y estén entre 0 y 9.
        lista_digitos = [] # Lista para almacenar los dígitos únicos.
        for valor in lista_secuencia: 
            if valor.isdigit():  # Valida que sean dígitos numéricos.
                num = int(valor) # Convierte a entero.
                if num >= 0 and num <= 9:  # Valida el rango.
                    if num not in lista_digitos:  # Valida que no se repitan.
                        lista_digitos.append(num) # Agrega el número a la lista si es único.
                    else: # Si se repite.
                        print("\nError: No debe repetir ningún número.")
                        todos_validos = False
                        break
                else: # Si no está en el rango 0-9.
                    print("\nError: Los números deben estar entre 0 y 9.")
                    todos_validos = False
                    break
            else: # Si no es un dígito.
                print("\nError: Solo se permiten números.")
                todos_validos = False
                break

        if not todos_validos:
            continue  # Vuelve a pedir.

        # Bloque de código para mezclar la lista de dígitos sin librerías. 
        for indice in range(len(lista_digitos)):
            i_aleatorio = (indice * 7 + 3) % len(lista_digitos) # Cálculo matemático para mezclar los dígitos.
                                                                # Utilizamos una fórmula simple para generar un índice aleatorio basado en el índice actual.
            lista_digitos[indice], lista_digitos[i_aleatorio] = lista_digitos[i_aleatorio], lista_digitos[indice] # Intercambia los valores en las posiciones 'indice' e 'i_aleatorio'.

        combinacion = lista_digitos[:4] # Tomamos los primeros 4 números de la lista mezclada.

        # Guardamos los números en un archivo, separados por espacios.
        archivo = open(nombre_archivo, "w")
        archivo.write(" ".join(str(num) for num in combinacion)) # Convierte cada número a cadena y los une con espacios.
        archivo.close() 

        print("\nCódigo secreto generado y guardado correctamente.")
        return combinacion # Devuelve la combinación secreta.

# -------------------------------------------------
# Función: cargar_combinacion
# Parámetro: ruta (str) -> ruta del archivo donde se encuentra la combinación secreta.
# Proceso: lee el archivo, verifica que tenga exactamente 4 números entre 0 y 9.
# Devuelve: lista de enteros con la combinación secreta.
# -------------------------------------------------
def cargar_combinacion(ruta):
    try:
        archivo = open(ruta, "r")  # Intenta abrir el archivo en modo lectura.
        pin = archivo.readline().strip()  # Lee la primera línea y quita los espacios.
        archivo.close()

        digitos = pin.split()  # Separa por espacios y crea la lista.
        if len(digitos) != 4:  # Valida que sean exactamente 4 números.
            print("\nError: el archivo no contiene exactamente 4 números.")
            return None 

        combinacion = [] # Lista para almacenar la combinación secreta.
        for valor in digitos: 
            if valor.isdigit():  # Valida que sea un número.
                numero = int(valor)
                if 0 <= numero <= 9:  # Valida que estén entre 0 y 9.
                    combinacion.append(numero) # Agrega el número a la combinación.
                else: # Si no está en el rango 0-9.
                    print("\nError: todos los números deben estar entre 0 y 9.")
                    return None
            else: # Si no es un número.
                print("\nError: el archivo contiene valores no numéricos.")
                return None

        return combinacion

    except FileNotFoundError: # Si el archivo no existe.
        print("\nError: el archivo no existe.")
        return None

# -------------------------------------------------
# Función: crear_tablero
# Proceso: crea una lista vacía con capacidad para 10 intentos.
# Cada intento se guardará como [combinación, aciertos, coincidencias].
# Devuelve: lista vacía que representará el tablero de juego.
# -------------------------------------------------
def crear_tablero():
    tablero = [] # Lista vacía para el tablero.
    for i in range(10): # Prepara 10 filas vacías (van a llenarse conforme avanza el juego).
        tablero.append([None, None, None])  # [combinación, aciertos, coincidencias]
    return tablero # Devuelve el tablero vacío.

# -------------------------------------------------
# Función: imprimir_tablero
# Parámetro: tablero (list) -> lista que contiene intentos previos
# Proceso: recorre el tablero e imprime en el formato:
#          #  Intento | ✓ | ~
#          1  2511    | 1 | 0
# Devuelve: nada (solo imprime en pantalla).
# -------------------------------------------------
def imprimir_tablero(tablero):
    print("\n#  Intento  | ✓ | ~")
    numero_intento = 1 # Contador de intentos.
    for fila in tablero: # Recorre cada fila del tablero.
        if fila[0] is not None: # Solo muestra los intentos ya jugados.
            combinacion_cadena = "".join(str(digito) for digito in fila[0]) # Convierte la combinación a cadena (str), sin comas. 
            print(f"{numero_intento}  {combinacion_cadena}     | {fila[1]} | {fila[2]}") # Imprime el intento, aciertos y coincidencias, formateado.
            numero_intento += 1 # Incrementa el contador de intentos.

# -------------------------------------------------
# Función: es_intento_valido
# Parámetros:
# - cadena (str) -> es el intento ingresado por el jugador.
# - historial (set) -> es el conjunto con los intentos ya jugados.
# Proceso: verifica que la cadena tenga 4 caracteres, que todos sean dígitos entre 0-9,
#          y que no se haya jugado antes.
# Devuelve: True si es válido, False si no.
# -------------------------------------------------
def es_intento_valido(cadena, historial):
    if len(cadena) != 4:
        print("\nError: la combinación debe tener exactamente 4 dígitos.")
        return False
    if not cadena.isdigit():
        print("\nError: la combinación solo puede contener dígitos (0-9).")
        return False
    if cadena in historial:
        print("\nError: esta combinación ya fue jugada antes.")
        return False
    return True

# -------------------------------------------------
# Función: leer_intento
# Parámetros:
# - historial (set) -> conjunto con los intentos ya jugados.
# - nombre_jugador (str).
# Proceso: solicita al jugador que ingrese su intento, valida que sea correcto,
#          y lo agrega al historial.
# Llama a la función es_intento_valido para verificar el intento.
# Devuelve: lista de enteros con el intento válido.
# -------------------------------------------------
def leer_intento(historial, nombre_jugador):
    while True:
        intento_cadena = input(f"{nombre_jugador}, ingrese su intento (4 dígitos): ").strip()
        if es_intento_valido(intento_cadena, historial): 
            historial.add(intento_cadena) # Agrega el intento al historial.
            return [int(digito) for digito in intento_cadena] # Convierte la cadena a lista de enteros.

# -------------------------------------------------
# Función: calculo_resultado
# Parámetros:
# - enteros_combinacion (list) -> lista de enteros con el intento del jugador.
# - combinacion (list) -> lista de enteros con la combinación secreta.
# Proceso: compara el intento con la combinación secreta, cuenta los aciertos exactos
#          y las coincidencias.
# Devuelve: tupla con el número de aciertos exactos y coincidencias.
# -------------------------------------------------
def calculo_resultado(enteros_combinacion, combinacion):
    # Copias para trabajar sin mutar las listas originales.
    intento = enteros_combinacion.copy()
    secreto = combinacion.copy()

    # Cuenta los aciertos exactos y "anula" esas posiciones (los marca con None).
    n_aciertos_exactos = 0
    for i in range(len(intento)): # Aquí len(intento) será 4.
        if intento[i] == secreto[i]:
            n_aciertos_exactos += 1
            intento[i] = None # Evita volver a contar este dígito.
            secreto[i] = None # Evita volver a contar este dígito.

    # Cuenta las coincidencias (mismo dígito, distinta posición).
    # Para cada dígito restante del intento, buscamos si existe en secreto.
    n_coincidencias = 0
    for i in range(len(intento)):
        valor = intento[i]
        if valor is None:
            continue # Saltamos los que ya fueron aciertos exactos.
        try: # Buscamos la primera aparición de 'valor' en 'secreto' (si existe).
            posicion_en_secreto = secreto.index(valor)
            # Si lo encontramos, contamos la coincidencia y anulamos esa ocurrencia.
            n_coincidencias += 1
            secreto[posicion_en_secreto] = None # Elimina la primera ocurrencia para evitar contar doble.
        except ValueError:
            pass #  No está en 'secreto' (o ya fue consumido), no hacemos nada.

    return n_aciertos_exactos, n_coincidencias

# -------------------------------------------------
# Función: actualizar_tablero
# Parámetros:
# - tablero (list) -> lista que representa el tablero de juego.
# - numero_intento (int) -> número del intento actual (1 a 10).
# - intento (list) -> lista de enteros con el intento del jugador.
# - secreto (list) -> lista de enteros con la combinación secreta.
# Proceso: actualiza el tablero con el intento del jugador, calcula los aciertos y coincidencias,
#          e imprime el tablero actualizado.
# Devuelve: tupla con el número de aciertos y coincidencias.
# -------------------------------------------------
def actualizar_tablero(tablero, numero_intento, intento, secreto):
    aciertos, coincidencias = calculo_resultado(intento, secreto) # Calcula aciertos y coincidencias.
    tablero[numero_intento - 1] = [intento, aciertos, coincidencias] # Guarda en el tablero (ajustando el índice, porque la lista arranca en 0).
    imprimir_tablero(tablero) # Muestra tablero actualizado.
    return aciertos, coincidencias

# -------------------------------------------------
# Función:: es_victoria
# Parámetro: aciertos (int) -> número de aciertos del jugador.
# Proceso: verifica si el jugador ha acertado la combinación secreta.
# Devuelve: True si acertó los 4 dígitos, False en caso contrario.
# -------------------------------------------------
def es_victoria(aciertos):
    return aciertos == 4

# -------------------------------------------------
# Función: fin_del_juego
# Parámetros:
# - intentos (int) -> número de intentos realizados por el jugador.
# - aciertos (int) -> número de aciertos del jugador.
# Proceso: determina si el juego ha terminado, ya sea por victoria o por alcanzar el límite de intentos.
#          Llama a la función es_victoria para verificar si el jugador ha ganado.
# Devuelve: True si el juego ha terminado, False si aún hay intentos disponibles.
# -------------------------------------------------
def fin_del_juego(intentos, aciertos):
    if es_victoria(aciertos):
        return True
    if intentos >= 10:
        return True
    return False

# -------------------------------------------------
# Función: iniciar_juego
# Controla el flujo del juego.
# Parámetros: ninguno.
# Proceso:
# - Solicita el nombre del jugador.
# - Pregunta si desea generar una nueva combinación secreta o cargar una existente:
#   * Si genera una nueva combinación, solicita el nombre del archivo y guarda la combinación.
#   * Si carga una combinación, solicita la ruta del archivo y verifica que sea válida.
# - Crea el tablero y el historial de intentos.
# - Permite al jugador hacer hasta 10 intentos para adivinar la combinación.
# - Actualiza el tablero con cada intento y muestra los resultados.
# - Al finalizar, pregunta si el jugador desea jugar de nuevo.
# - Si el jugador decide jugar de nuevo, reinicia el juego; si no, finaliza el programa.
# -------------------------------------------------
def iniciar_juego():
    nombre_jugador = input("Ingrese su nombre: ").strip() # Pide el nombre del jugador.
    if nombre_jugador == "":
        nombre_jugador = "Jugador" # Si no ingresa nombre, usa "Jugador" por defecto.

    generar = input("¿Desea generar una nueva combinación secreta? (S/N): ").strip().lower() # Pregunta si quiere generar una nueva combinación.
    secreto = None
    ruta = None

    if generar == "s":
        nombre_archivo = input("Nombre del archivo (ej. combinacion.txt): ").strip() # Pide el nombre del archivo para guardar la combinación.
        # Si no se ingresa un nombre, usa "combinacion_secreta.txt
        if nombre_archivo == "":
            nombre_archivo = "combinacion_secreta.txt" # Genera un nombre por defecto.
        secreto = generar_codigo_secreto(nombre_archivo) # Asume que la función genera y guarda la combinación en el archivo.
        ruta = nombre_archivo
    else: # Si no quiere generar una nueva combinación, pide la ruta del archivo existente.
        ruta = input("Ruta del archivo con la combinación (ej. combinacion.txt): ").strip()
        if ruta == "":
            ruta = "combinacion_secreta.txt" # Usa un nombre por defecto si no se ingresa nada.
        # Carga la combinación desde el archivo.
        secreto = cargar_combinacion(ruta) # Llama a la función para cargar la combinación secreta.

    if secreto is None or len(secreto) != 4: # Valida que la combinación tenga 4 dígitos.
        print("\nError al cargar la combinación secreta. Se aborta la partida.")
        return True
    
    # Se definen las variables del juego.
    tablero = crear_tablero() # Crea el tablero de juego.
    historial = set() # Usamos un conjunto para almacenar los intentos ya jugados.
    intentos = 0 # Inicializa el contador de intentos.

    while intentos < 10: # Permite hasta 10 intentos.
        print(f"\nIntento {intentos + 1} de 10") # Imprime el número de intento actual.
        intento_lista = leer_intento(historial, nombre_jugador) # Llama a la función para leer el intento del jugador.
        aciertos, coincidencias = actualizar_tablero(tablero, intentos + 1, intento_lista, secreto) # Actualiza el tablero con el intento del jugador y muestra los resultados.
        intentos += 1 # Incrementa el contador de intentos.

        if es_victoria(aciertos): # Verifica si el jugador ha acertado la combinación.
            print(f"\n¡Felicidades, acertaste la combinación en {intentos} intentos!") # Imprime mensaje de victoria.
            break # Sale del bucle si el jugador ha ganado.

        if intentos >= 10: # Verifica si se han agotado los intentos.
            secreto_str = " ".join(str(d) for d in secreto) # Convierte la combinación secreta a cadena para mostrarla.
            print(f"\nNo lo lograste. La combinación correcta era {secreto_str}") # Informa al jugador de la combinación correcta.
            break # Sale del bucle si se han agotado los intentos.

    respuesta = input("\n¿Desea jugar de nuevo? (S/N): ").strip().lower() # Pregunta al jugador si desea jugar de nuevo.
    if respuesta == "s": # Si el jugador quiere jugar de nuevo, retorna True para reiniciar el juego.
        return True
    else: # Si el jugador no quiere jugar de nuevo, imprime mensaje de despedida y retorna False para finalizar el programa.
        print("\nGracias por jugar. ¡Hasta luego!")
        return False

# -------------------------------------------------
# Función: menu_principal
# Proceso: muestra el menú principal del programa, permite al usuario elegir entre jugar o salir.
#          Si elige jugar, llama a iniciar_juego(); si elige salir, finaliza el programa.
# Devuelve: nada (controla el flujo del programa).
# -------------------------------------------------
def menu_principal():
    while True: # Bucle principal del menú.
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Seleccione una opción (1 o 2): ").strip() # Pide al usuario que ingrese una opción.

        if opcion == "1": # Si elige jugar, llama a iniciar_juego().
            continuar = iniciar_juego() 
            if not continuar:
                break # Si no quiere jugar de nuevo, sale del bucle y finaliza el programa.
        elif opcion == "2": # Si elige salir, imprime mensaje de despedida y finaliza el programa.
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break # Sale del bucle y finaliza el programa.
        else: # Si la opción no es válida, informa al usuario.
            print("\nError: opción inválida. Debe ingresar 1 o 2.")

# -------------------------------------------------
# Punto de entrada del programa
# Si se ejecuta este archivo directamente, llama a menu_principal() para iniciar el programa.
#_name_ representa el nombre del módulo.
# El módulo es la unidad básica de código en Python. 
# Si _name_ es igual a "__main__", significa que este archivo se está ejecutando directamente,
# no como un módulo importado en otro archivo.
# Es decir, si se ejecuta este archivo directamente, se ejecutará menu_principal().
# Si se importa este archivo en otro, no se ejecutará menu_principal() automáticamente.
# -------------------------------------------------
if __name__ == "__main__":  
    menu_principal()