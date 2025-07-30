'''
ORDEN SUGERIDO POR CHAT GPT:
1. cargar_combinacion()

    Objetivo: leer la combinación secreta desde un archivo .txt.

    Contenido clave:

        Verificar existencia del archivo.

        Leer línea, separar caracteres, parsear a enteros.

        Validar que sean exactamente 4 dígitos entre 0 y 9.

        En caso de fallo, mostrar error y abortar (levantar excepción o devolver None).

2. crear_tablero()

    Objetivo: inicializar la estructura de datos que guardará los 10 intentos.

    Contenido clave:

        Crear lista de 10 elementos (uno por intento), cada uno con campos para:

        Combinación propuesta (inicialmente None o [])

        Aciertos exactos

        Coincidencias (números correctos en otra posición)

3. imprimir_tablero(tablero)

    Objetivo: mostrar al jugador el estado actual de sus intentos.

    Contenido clave:

        Recorrer cada fila del tablero con índice.

        Para cada fila: imprimir número de intento, combinación (si existe), aciertos y coincidencias.

        Formato uniforme y claro.

4. leer_intento(nombre_jugador)

    Objetivo: solicitar al jugador una cadena de 4 caracteres.

    Contenido clave:

        input(f"{nombre_jugador}, ingresa 4 dígitos: ")

        Bucle hasta que la cadena cumpla con longitud y caracteres (0–9).

        Retornar la cadena cruda.

5. validar_intento(intento_str, historial)

    Objetivo: asegurarse de que el intento es válido y no repetido.

    Contenido clave:

        Verificar longitud == 4 y todos los caracteres en '0'..'9'.

        Comprobar que no esté en el conjunto historial.

        En caso de error, imprimir motivo (“repetido”, “caracter no válido”, etc.) y devolver False.

        Si es válido, return True.

6. calculo_resultado(intento_list, combinacion_secreta)

    Objetivo: contar cuántos dígitos están en la posición correcta (aciertos) y cuántos aparecen en otra posición (coincidencias).

    Contenido clave:

        Recorrer índices para aciertos exactos.

        Para coincidencias, usar contadores de frecuencia o lógica de multiconjunto, restando los aciertos ya contados.

        Devolver (n_aciertos, n_coincidencias).

7. registro_intento(tablero, fila_idx, intento_list, resultado)

    Objetivo: volcar los datos del intento al tablero.

    Contenido clave:

        Asignar en tablero[fila_idx] los campos: combinación, aciertos, coincidencias.

8. actualizar_tablero(tablero)

    Objetivo: refrescar la vista tras cada registro.

    Contenido clave:

        Llamar a imprimir_tablero(tablero).

9. es_victoria(resultado, contador_intentos)

    Objetivo: detectar si el jugador adivinó la combinación.

    Contenido clave:

        Si resultado.aciertos == 4:

        Imprimir mensaje de victoria y número de intentos usados.

        Devolver True.

        Si no, return False.

10. fin_del_juego(combinacion_secreta, contador_intentos)

    Objetivo: manejar el caso de derrota (agotamiento de intentos).

    Contenido clave:

        Si contador_intentos >= 10 y no hubo victoria:

        Imprimir la combinación secreta.

        Mensaje de “Lo sentimos, ha perdido el juego.”

11. control_flujo(contador_intentos)

    Objetivo: incrementar y retornar el contador de intentos.

    Contenido clave:

        return contador_intentos + 1

12. iniciar_juego()

    Objetivo: coordinador principal de la partida.

    Contenido clave:

        Pedir nombre del jugador.

        Llamar a cargar_combinacion().

        Inicializar tablero = crear_tablero() y historial = set().

        contador_intentos = 0.

        Bucle principal while contador_intentos < 10:

            Incrementar e imprimir "Intento X de 10".

            Obtener str_intento = leer_intento(nombre).

            Si validar_intento(str_intento, historial):

                Convertir a lista de ints.

                Calcular resultado con calculo_resultado.

                Registrar con registro_intento.

                Añadir al historial.

                Llamar a actualizar_tablero.

                Si es_victoria(...): llamar a volver_a_jugar() y break.

                Si no, contador_intentos = control_flujo(contador_intentos).

        Fuera del bucle, si no ganó, llamar a fin_del_juego.

        Finalmente, volver_a_jugar().

13. volver_a_jugar()

    Objetivo: manejar la opción de reiniciar o salir.

    Contenido clave:

        Pedir input “¿Desea volver a jugar? (S/N)”.

        Si “S”: llamar a iniciar_juego().

        En cualquier otro caso: mensaje de despedida y exit().

14. menu_principal()

    Objetivo: punto de entrada del programa.

    Contenido clave:

        Bucle infinito de input("1) Jugar 2) Salir: ").

        Si opción = “1”: llamar a iniciar_juego().

        Si opción = “2”: imprimir despedida y break o exit().

        En otro caso: mensaje de error “Opción inválida”.
'''

def cargar_combinacion():


def crear_tablero():

























# MENÚ PRINCIPAL:

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
    
