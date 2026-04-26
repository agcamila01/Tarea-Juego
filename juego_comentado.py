palabras_correctas = ["PYTHON", "CODIGO", "LOGICA", "BUCLE", "LISTA", "VARIABLE", "CADENA", 
                      "ENTERO", "FUNCION", "CONSOLA", "OBJETO", "RECURSO", "PROCESO", "TECLADO", "PANTALLA"]
palabras_desordenadas = ["YPHTNO", "GIDOCO", "CIALGO", "ELUBC", "STILA", "BAVALRIE", "NEDACA", 
                         "REETNO", "COINFUN", "OLSACON", "TEJOBO", "SRUOCRE", "SCEOPRO", "DALOTEC", "TALLAPAN"]

print("Bienvenido al juego") # 
nombre_jugador = input("Ingrese su nombre: ")

while True:
    modo_de_juego = int(input("Elija su modo de juego:\n1: Modo Libre (Una palabra)\n2: Modo Clásico (Todas las palabras)\n3: Salir del juego\n"))
    if modo_de_juego == 1 or modo_de_juego == 2: # Si se ingresa un modo de juego válido, pregunta con que dificultad quiere jugar
        while True:
            opcion_dificultad = int(input("Dificultad: \n1: Fácil\n2: Medio\n3: Difícil\n4: Extremo\n"))
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
                print("Por favor ingrese una opción válida")
        # -------------- MODO LIBRE ---------------------------
        if modo_de_juego == 1:
            print("----------------------------------------")
            print("Modo de Juego: Modo Libre (Una palabra)")
            print("Instrucciones: ") # Añadir instrucciones
            print(f"Dificultad: {dificultad}")
            print(f"Vidas: {vidas}")
            print("----------------------------------------")
            print("Presione ENTER para comenzar")
            input()
            indice_palabra = int(input(f"Ingrese un numero del 1 al {len(palabras_desordenadas)}: ")) # Usuario "elige" una palabra
            palabra_seleccionada = palabras_desordenadas[indice_palabra-1] # Restamos 1 porque la lista comienza desde el 0
            palabra_correcta = palabras_correctas[indice_palabra-1]
            while vidas > 0:
                respuesta_usuario = input(f"Ordena la palabra {palabra_seleccionada}: ").upper() # upper para hacer comparaciones en mayuscula
                if respuesta_usuario == palabra_correcta:
                    print(f"¡Correcto! ¡Felicidades {nombre_jugador}!")
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
                print(f"No te quedan vidas, la respuesta era: {palabra_correcta}")
        # ----------------- MODO CLÁSICO ----------------------
        elif modo_de_juego == 2:
            print("----------------------------------------")
            print("Modo de Juego: Modo Clásico (Todas las palabras)")
            print("Instrucciones: ") ##
            print(f"Dificultad: {dificultad}")
            print(f"Vidas: {vidas}")
            print("----------------------------------------")
            print("Presione ENTER para comenzar")
            input()
            puntaje_total = 0 # acumulador de puntaje
            for indice_palabra in range(len(palabras_desordenadas)): # recorre toda la lista de palabras desordenadas en orden
                puntaje_ronda = 0 # reinicio de puntaje_ronda en cada ronda
                palabra = palabras_desordenadas[indice_palabra]
                palabra_correcta = palabras_correctas[indice_palabra]
                # las vidas en este modo corresponden a vidas por ronda
                # en cada ronda se vuelve a tener las vidas que se asignaron en el menu de dificultad
                vidas_ronda = vidas 
                print(f"Palabra {indice_palabra + 1} de {len(palabras_desordenadas)}")
                while vidas_ronda > 0:
                    respuesta_usuario = input(f"Ordena la palabra {palabra}: ").upper()
                    if respuesta_usuario == palabra_correcta:
                        print(f"¡Correcto!")
                        puntaje_ronda = 100 * vidas_ronda # si acierta, su puntaje sera de 100 puntos por las vidas que le queden
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
                    print(f"No te quedan vidas para esta ronda, la respuesta era: {palabra_correcta}")
                    puntaje_ronda = 0 # si no logra adivinar una palabra suma 0 puntos en esa ronda y pasa a la siguiente palabra 
                puntaje_total = puntaje_total + puntaje_ronda
            print(f"Puntaje final: {puntaje_total}")
        otra_partida = input("¿Quieres jugar otra partida? 1: Sí | 2: No: ") # cuando termina la partida pregunta si quiere salir o iniciar una nueva
        if otra_partida == "1":
            continue
        else:
            break
    elif modo_de_juego == 3:
        break
    else:
        print("Ingrese una opcion válida")
