palabras_correctas = ["PYTHON", "CODIGO", "LOGICA", "BUCLE", "LISTA", "VARIABLE", "CADENA", 
                      "ENTERO", "FUNCION", "CONSOLA", "OBJETO", "RECURSO", "PROCESO", "TECLADO", "PANTALLA"]
palabras_desordenadas = ["YPHTNO", "GIDOCO", "CIALGO", "ELUBC", "STILA", "BAVALRIE", "NEDACA", 
                         "REETNO", "COINFUN", "OLSACON", "TEJOBO", "SRUOCRE", "SCEOPRO", "DALOTEC", "TALLAPAN"]

print("==========================================")
print("             JUEGO DE PALABRAS        ")
print("==========================================")
print("Pon a prueba tu lógica ordenando palabras\n")
nombre_jugador = input("Ingrese su nombre: ")

while True:
    print("\nModo de juego")
    print("1: Modo Libre (Una palabra)")
    print("2: Modo Clásico (Todas las palabras)")
    print("3: Salir del Juego")
    validacion_entrada_modo = input("Elija su modo de juego: ") # Para que no se termine la ejecucion con error si no se ingresa un numero
    if validacion_entrada_modo.isdigit():
        modo_de_juego = int(validacion_entrada_modo)
    else:
        print("*** Por favor ingrese solo números ***")
        continue
    if modo_de_juego == 1 or modo_de_juego == 2: # Si se ingresa un modo de juego válido, pregunta con que dificultad quiere jugar
        while True:
            print("\nDificultad:")
            print("1: Fácil   - 10 vidas + pista para cada palabra.")
            print("2: Medio   - 5 vidas  + pista cuando te queden 2 vidas.")
            print("3: Difícil - 3 vidas  + pista cuando te quede 1 vida.")
            print("4: Extremo - 1 vida SIN PISTAS.")
            validacion_entrada_dificultad = input("Elija su nivel de dificultad: ")
            if validacion_entrada_dificultad.isdigit():
                opcion_dificultad = int(validacion_entrada_dificultad)
            else:
                print("*** Por favor ingrese solo números ***")
                continue
            if opcion_dificultad == 1:
                dificultad = "Facil"
                vidas = 10
                break
            elif opcion_dificultad == 2:
                dificultad = "Medio"
                vidas = 5
                break
            elif opcion_dificultad == 3:
                dificultad = "Dificil"
                vidas = 3
                break
            elif opcion_dificultad == 4:
                dificultad = "Extremo"
                vidas = 1
                break
            else:
                print("*** Por favor ingrese una opción válida ***")
        # ------------------------ MODO LIBRE ---------------------------
        if modo_de_juego == 1:
            print("------------------------------------------------------------------------")
            print("Modo de Juego: Modo Libre (Una palabra)")
            print(f"Dificultad: {dificultad}")
            print(f"Vidas: {vidas}")
            print("Instrucciones:")
            print("- Se te mostrará una palabra desordenada.")
            print("- Deberás escribirla en el orden correcto.")
            print("- Cada vez que falles, perderás una vida.")
            print("- El juego termina cuando aciertes la palabra o cuando te quedes sin vidas.")
            print(f"¡Buena Suerte {nombre_jugador}!")
            print("------------------------------------------------------------------------")
            print("Presione ENTER para comenzar")
            input()
            validacion_entrada_indice = input(f"Ingrese un numero del 1 al {len(palabras_desordenadas)}: ") # Usuario "elige" una palabra
            if validacion_entrada_indice.isdigit():
                indice_palabra = int(validacion_entrada_indice)
                if indice_palabra < 1 or indice_palabra > len(palabras_desordenadas):
                    print("*** Número fuera de rango ***")
                    continue
            else:
                print("*** Por favor ingrese solo números ***")
                continue
            palabra_seleccionada = palabras_desordenadas[indice_palabra-1] # Restamos 1 porque la lista comienza desde el 0
            palabra_correcta = palabras_correctas[indice_palabra-1]
            while vidas > 0:
                respuesta_usuario = input(f"\nOrdena la palabra {palabra_seleccionada}: ").upper() # upper para hacer comparaciones en mayuscula
                if respuesta_usuario == palabra_correcta:
                    print(f"¡Correcto! ¡Felicidades {nombre_jugador}!\n")
                    break
                else:
                    vidas -= 1
                    print("¡Incorrecto!")
                    print(f"Vidas restantes: {vidas}")
                    # Hay dos tipos de pistas, una sencilla que solo muestra la primera letra de la palabra correcta 
                    # Y el otro tipo de pista que muestra las letras con indice par, ej: CASA -> C_S_
                    # Se inicializa la variable pista aquí para que quede vacía cada vez que se pierde una vida
                    # Sino se empieza a concatenar todo si se hace mas de un intento ej: C_S_->C_S_C_S_->C_S_C_S_C_S_
                    pista = ""
                    for letra in range(len(palabra_correcta)):
                        if letra % 2 == 0: # indice par -> se muestra la letra
                            pista = pista + palabra_correcta[letra]
                        else:
                            pista = pista + "_" #indice impar -> se muestra un '_' en vez de la letra
                    if dificultad == "Facil": # Si elige dificultad fácil, se ve la pista cada vez que el usuario se equivoque
                        print(f"Pista: {pista}")
                    elif dificultad == "Medio": # Se ve una pista sencilla cuando queden 2 vidas y mejor pista cuando quede 1 vida
                        if vidas == 2:
                            print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                        elif vidas == 1:
                            print(f"Pista: {pista}")
                    elif dificultad == "Dificil" and vidas == 1: # Solo se ve la pista sencilla cuando queda 1 vida
                        print(f"Pista: La palabra comienza con {palabra_correcta[0]}") 
                    # dificultad extremo nunca muestra pistas    
            if vidas == 0:
                print(f"\nNo te quedan vidas, la respuesta era: {palabra_correcta}")
        # ----------------- MODO CLÁSICO ----------------------
        elif modo_de_juego == 2:
            print("-------------------------------------------------------------------------------------------")
            print("Modo de Juego: Modo Clásico (Todas las palabras)")
            print(f"Dificultad: {dificultad}")
            print(f"Vidas: {vidas}")
            print("Instrucciones:")
            print("- Deberás escribir las palabras en el orden correcto, una por una.")
            print("- Cada palabra es una ronda independiente (las vidas se reinician en cada ronda).")
            print("- Cada vez que falles, perderás una vida en esa ronda.")
            print("- Si aciertas la palabra, sumas 100 puntos * vidas restantes en la ronda.")
            print("- Si te quedas sin vidas en una ronda no sumarás puntos y avanzarás a la siguiente palabra.")
            print("- Al finalizar el juego se mostrará tu puntaje total.")
            print("¡Buena Suerte!")
            print("-------------------------------------------------------------------------------------------")
            print("Presione ENTER para comenzar")
            input()
            puntaje_total = 0 # acumulador de puntaje
            contador_acertadas = 0 # contador de palabras acertadas
            for indice_palabra in range(len(palabras_desordenadas)): # recorre toda la lista de palabras desordenadas en orden
                puntaje_ronda = 0 # reinicio de puntaje_ronda en cada ronda
                palabra = palabras_desordenadas[indice_palabra]
                palabra_correcta = palabras_correctas[indice_palabra]
                # las vidas en este modo corresponden a vidas por ronda
                # en cada ronda se vuelve a tener las vidas que se asignaron en el menu de dificultad
                vidas_ronda = vidas 
                print(f"Palabra {indice_palabra + 1} de {len(palabras_desordenadas)}")
                while vidas_ronda > 0:
                    respuesta_usuario = input(f"\nOrdena la palabra {palabra}: ").upper()
                    if respuesta_usuario == palabra_correcta:
                        print(f"¡Correcto!")
                        puntaje_ronda = 100 * vidas_ronda # si acierta, su puntaje sera de 100 puntos por las vidas que le queden
                        contador_acertadas += 1
                        break # si acierta sale del while, aunque tenga mas de 0 vidas
                    else:
                        vidas_ronda -= 1
                        print("¡Incorrecto!")
                        print(f"Vidas restantes: {vidas_ronda}")
                        # Mismo sistema de pistas que el modo libre pero las vidas se reinician cuando se pasa de palabra
                        pista = ""
                        for letra in range(len(palabra_correcta)):
                            if letra % 2 == 0:
                                pista = pista + palabra_correcta[letra]
                            else:
                                pista = pista + "_"
                        if dificultad == "Facil":
                            print(f"Pista: {pista}")
                        elif dificultad == "Medio":
                            if vidas_ronda == 2:
                                print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                            elif vidas_ronda == 1:
                                print(f"Pista: {pista}")
                        elif dificultad == "Dificil" and vidas_ronda == 1:
                            print(f"Pista: La palabra comienza con {palabra_correcta[0]}")
                if vidas_ronda == 0:
                    print(f"\nNo te quedan vidas para esta ronda, la respuesta era: {palabra_correcta}\n")
                    puntaje_ronda = 0 # si no logra adivinar una palabra suma 0 puntos en esa ronda y pasa a la siguiente palabra 
                puntaje_total = puntaje_total + puntaje_ronda
            print("\n-----------------------------------------------------------")
            print("Fin de la partida")
            print(f"Has acertado {contador_acertadas} de {len(palabras_desordenadas)} palabras")
            print(f"Puntaje final {nombre_jugador}: {puntaje_total} puntos")
            print("-----------------------------------------------------------")
        otra_partida = input("\n¿Quieres jugar otra partida? 1: Sí | 2: No: ") # cuando termina la partida pregunta si quiere salir o iniciar una nueva
        if otra_partida == "1":
            continue
        else:
            print("¡Gracias por jugar!")
            break
    elif modo_de_juego == 3:
        break
    else:
        print("*** Ingrese una opcion válida ***")
