import random       # Se importa el modulo random que genera numeros aleatorios que sera utilizado luego para la generacion de la baraja

# Funcion ilustrativa de menu con saludo del juego
def menu_salir():       # Definicion de la funcion menu_salir()
    print("==========================================================")
    print("||            ¡Muchas Gracias por Jugar!                ||")
    print("==========================================================")    

# Funcion del menu principal del juego
def menu_inicial():     # Definicion de la funcion menu_inicial()
    print("==========================================================")
    print("||   Menú BlackJack:                                    ||")
    print("||       1. Jugar                                       ||")
    print("||       2. Salir                                       ||")
    print("==========================================================")
    
    opcion = int(input("° Opción: "))       # El jugador ingresa la opcion deseada
    while opcion != 1 and opcion != 2:      # Si la opcion ingresada por el jugador no corresponde a ninguna de las mostradas en el menu:
        opcion = int(input("° Ingrese una opción válida: "))        # Se le solicita al jugador que vuelva a ingresar la opcion

    print("\n")     # Se imprime un espacio
    return opcion       # Se devuelve la opcion ingresada por el jugador
    
# Funcion del menu de cantidad de jugadores
def menu_jugadores():       # Definicion de la funcion menu_jugadores()
    print("==========================================================")
    print("||   Menú BlackJack:                                    ||")
    print("||       ¿Cuál es la cantidad de jugadores?             ||")
    print("==========================================================")
    
    numero_jugadores = int(input("° Jugadores: "))      # El jugador ingresa la cantidad de jugadores deseada
    while numero_jugadores < 1 or numero_jugadores > 4:     # Si el numero de jugadores ingresado por el jugador es menor a 1 o mayor a 4: (esto esta definido de esta forma para que no sea grande el numero de jugadores pero puede ser ampliado quitando el "> 4")
        numero_jugadores = int(input("° Ingrese un número de jugadores válido (1 a 4): "))      # Se le solicita al jugador que vuelva a ingresar el numero de jugadores
 
    print("\n")     # Se imprime un espacio
    return numero_jugadores     # Se devuelve la cantidad de jugadores ingreasados
    
# Funcion del menu de informacion de jugadores
def menu_info_jugadores(numero_jugadores):      # Definicion de la funcion menu_info_jugadores() la cual recibe el numero de jugadores
    jugadores = []      # Inicializacion de la lista de jugadores
    
    print("==========================================================")
    print("||   Menú BlackJack:                                    ||")
    print("||       Ingrese la información de los Jugadores:       ||")
    print("==========================================================")
    
    for numero in range(numero_jugadores):      # Se repetiran los siguientes casos segun el numero de jugadores que recibe la fnucion
        print("° Jugador:", numero)     # Se imprime el jugador y su numero
        nombre_jugador = input("° Nombre: ")        # Se solicita al jugador que ingrese su nombre 
        saldo_jugador = int(input("° Saldo: "))     # Se solicita al jugador que ingrese su saldo
        while saldo_jugador < 1:        # Mientras el saldo que ingreso el jugador sea menor que 1: (el saldo no puede ser negativo o 0 para jugar)
            saldo_jugador = int(input("° Ingrese un saldo válido (mayor a 0): "))       # Se le solicita al jugador que vuelva a ingresar el saldo
        jugando = 1     # Se setea la variable jugando en 1 (significa que el jugador esta jugando)
        
        jugadores.append([numero, nombre_jugador, saldo_jugador, jugando])      # Se guardan dentro de la lista jugadores una lista con: el numero, nombre, saldo y estado, del jugador
        print("\n")     # Se imprime un espacio
    
    return jugadores        # Se devuelve la lista jugadores con la lista de cada jugador y su informacion

# Funcion del menu de accion de ronda de cartas del jugador
def menu_accion_jugador():      # Definicion de la funcion menu_accion_jugador()
    print("==========================================================")
    print("||   Menú BlackJack:                                    ||")
    print("||       1. Pedir Carta                                 ||")
    print("||       2. Plantarte                                   ||")
    print("==========================================================")
    
    opcion = int(input("° Opción: "))       # El jugador ingresa la opcion deseada
    while opcion != 1 and opcion != 2:      # Si la opcion ingresada por el jugador no corresponde a ninguna de las mostradas en el menu:
        opcion = int(input("° Ingrese una opción válida: "))        # Se le solicita al jugador que vuelva a ingresar la opcion

    print("\n")     # Se imprime un espacio
    return opcion       # Se devuelve la opcion ingresada por el jugador

# Funcion del menu para modificar el saldo del jugador
def menu_saldo_jugador():       # Deficion de la funcion menu_saldo_jugador()
    print("==========================================================")
    print("||   Menú BlackJack:                                    ||")
    print("||       1. Ingresar Saldo                              ||")
    print("||       2. Salir                                       ||")
    print("==========================================================")
    
    opcion = int(input("° Opción: "))       # El jugador ingresa la opcion deseada
    while opcion != 1 and opcion != 2:      # Si la opcion ingresada por el jugador no corresponde a ninguna de las mostradas en el menu:
        opcion = int(input("° Ingrese una opción válida: "))        # Se le solicita al jugador que vuelva a ingresar la opcion

    print("\n")     # Se imprime un espacio
    return opcion       # Se devuelve la opcion ingresada por el jugador

# Funcion del menu de decision sobre continuar en el juego del jugador
def menu_continuar_jugador():       # Definicion de la funcion menu_continuar_jugador()
    print("==========================================================")
    print("||   Menú BlackJack:                                    ||")
    print("||       1. Continuar                                   ||")
    print("||       2. Salir                                       ||")
    print("==========================================================")
    
    opcion = int(input("° Opción: "))       # El jugador ingresa la opcion deseada
    while opcion != 1 and opcion != 2:      # Si la opcion ingresada por el jugador no corresponde a ninguna de las mostradas en el menu:
        opcion = int(input("° Ingrese una opción válida: "))        # Se le solicita al jugador que vuelva a ingresar la opcion

    print("\n")     # Se imprime un espacio
    return opcion       # Se devuelve la opcion ingresada por el jugador

# Funcion para crear la baraja y mezclarla
def crear_baraja():     # Definicion de la funcion crear_baraja()
    palos = ["Corazones", "Diamantes", "Treboles", "Picas"]     # Se crea la lista palos con los diferentes palos
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]        # Se crea la lista valores con los diferentes valores que puede tomar cada carta
    baraja = []     # Se inicializa la lista que contendra la baraja
    # Se crea la baraja
    for palo in palos:      # Por cada item palo en la lista de palos:
        for valor in valores:       # Por cada item valor en la lista de valores:
            baraja.append([valor, palo])        # Se guarda en la lista de la baraja, una lista con el valor y el palo

    # Se mezcla la baraja
    n = len(baraja)     # Se guarda la longitud de la lista de la baraja
    for i in range(n):      # Por cada i dentro del rango definido por la longitud de la baraja, es decir de 1 en 1 hasta el final del largo de la baraja
        j = random.randint(0, n - 1)        # Guardamos en la variable j un numero random entre el 0 y la longitud de la baraja - 1
        baraja[i], baraja[j] = baraja[j], baraja[i]     # Se intercambian los elementos en las posiciones i y j de la lista baraja. Es una implementacion del algortimo de barajado de Fisher-Yates
    return baraja       # Devolvemos la lista creada y mezclada de la baraja


# Funcion para calcular el puntaje de cada mano
def calcular_puntaje(mano):     # Definicion de la funcion calcular_puntaje() la cual recibe como argumento la mano de cartas
    puntaje = 0     # Se inicializa en 0 la variable puntaje 
    ases = 0        # Se inicializa en 0 la variable ases
    for carta in mano:      # Por cada item carta en la lista mano
        valor = carta[0]        # Se guarda en la variable valor, el valor de la posicion 0 de la lista de carta en mano
        if valor == "J" or valor == "Q" or valor == "K":        # Si el valor de la carta es J, Q o K:
            puntaje += 10       # Se suma 10 al puntaje
        elif valor == "A":      # Si no, si el valor es A, significa que es un as, por ende puede valer 1 u 11:
            puntaje += 11       # Se suma 11 al puntaje
            ases += 1           # Se suma 1 a la variable ases, indicando que ya tiene un as
        elif valor == "2":      # Si no, si el valor es 2:
            puntaje += 2        # Se suma 2 al puntaje
        elif valor == "3":      # Si no, si el valor es 3:
            puntaje += 3        # Se suma 3 al puntaje
        elif valor == "4":      # Si no, si el valor es 4:
            puntaje += 4        # Se suma 4 al puntaje
        elif valor == "5":      # Si no, si el valor es 5:
            puntaje += 5        # Se suma 5 al puntaje
        elif valor == "6":      # Si no, si el valor es 6:
            puntaje += 6        # Se suma 6 al puntaje
        elif valor == "7":      # Si no, si el valor es 7:
            puntaje += 7        # Se suma 7 al puntaje
        elif valor == "8":      # Si no, si el valor es 8:
            puntaje += 8        # Se suma 8 al puntaje
        elif valor == "9":      # Si no, si el valor es 9:
            puntaje += 9        # Se suma 9 al puntaje
        elif valor == "10":     # Si no, si el valor es 10:
            puntaje += 10       # Se suma 10 al puntaje
    
    while puntaje > 21 and ases > 0:        # Mientras el puntaje sea mayor a 21 y no posea ases:
        puntaje -= 10      # Se resta 10 al puntaje
        ases -= 1       # Se resta 1 a la variable ases
    
    return puntaje      # Se retorna el puntaje total de la mano del jugador

# Funcion para mostrar las manos de los jugadores y el dealer por cada mano
def mostrar_manos(jugadores, dealer, estado_dealer):        # Definicion de la funcion mostrar_manos() la cual recibe como argumentos la lista de jugadores, la mano del dealer, y el estado del dealer (la segunda carta del dealer permanece oculta hasta que todos los jugadores terminaron su mano)
    print("Manos:")     # Se imprime el comienzo de una mano
    # Mano de los jugadores
    for jugador in jugadores:       # Por cada lista de jugador dentro de la lista de jugadores
        print(f"Jugador: {jugador[1]}, Cartas: {jugador[4]}, Puntaje: {calcular_puntaje(jugador[4])}")      # Se imprime el nombre del jugador, las lista de cartas que posee, y el puntaje total de sus cartas, el cual se obtiene mediante la funcion calcular_puntaje y la lista de cartas como argumento 
        
    # Mano del dealer
    if estado_dealer == 'mostrar':      # Si el estado del dealer es "mostrar": (significa que ya todos los jugadores terminaron sus manos)
        print(f"Cartas Dealer: {dealer}, Puntaje: {calcular_puntaje(dealer)}")      # Se imprimen las cartas del dealer, junto con su puntaje final mediante la funcion calcular_puntaje y su lista de cartas como argumento  
    else:       # Si los jugadores aun no terminaron sus manos:
        print(f"Cartas Dealer: {dealer[0]}, (Carta Oculta)")        # Se imprimen la lista de la primera carta del dealer, y la segunda se imprime que esta oculta
    print("\n")     # Se imprime un espacio

# Funcion para obtencion de cartas y eliminacion de la baraja luego de obtenida
def pedir_carta(baraja):        # Definicion de la funcion pedir_carta() la cual recibe como argumento la lista de la baraja
    carta = baraja[0]       # Se guarda la primera lista de carta en la variable carta, de la lista de la baraja
    del baraja[0]       # Se elimina la primera lista de carta de la lista de la baraja
    return carta        # Se devuelve la lista de la carta que obtuvimos

# Funcion para ingresar mas saldo por parte del jugador
def ingresar_saldo():       # Definicion de la funcion ingresar_saldo()
    saldo = int(input("¿Cuánto saldo desea ingresar? "))        # Se pregunta e ingresa el nuevo saldo deseado del jugador
    while saldo < 1:        # Si el saldo ingresado es menor a 1: (no puede ser 0 o negativo)
        saldo = int(input("Por favor, ingrese un saldo correcto. ¿Cuánto saldo desea ingresar? "))      # Se solicita al jugador que vuelva a ingresar el saldo
    
    print("\n")     # Se imprime un espacio
    return saldo        # Se devuelve el nuevo saldo ingresado por el jguador

# Funcion para obtener cuanto desea apostar el jugador de su saldo
def obtener_apuesta(saldo):     # Definicion de la funcion obtener_apuesta() la cual recibe como argumento el saldo del jugador
    apuesta = int(input("¿Cuánto quieres apostar? "))       # Se pregunta e ingresa la apuesta que desea realizar el jugador
    while apuesta > saldo or apuesta < 1:       # Si la apuesta ingresada es mayor al saldo disponible del jugador o es menor a 1 (no puede ser 0 o negativa):
        print("No puedes apostar más de lo que tienes o menos de 1. Intenta de nuevo.")     # Se informa al jugador de su error
        apuesta = int(input("¿Cuánto quieres apostar? "))       # Se le solicita al jugador que vuelva a ingresar la apuesta deseada
    
    print("\n")     # Se imprime un espacio
    return apuesta      # Se devuelve la apuesta deseada del jugador

# Funcion para determinar los resultados finales de la mano
def determinar_ganador(jugadores, dealer):      # Definicion de la funcion determinar_ganador() la cual recibe como argumento la lista de jugadores y la lista de cartas del dealer
    puntaje_dealer = calcular_puntaje(dealer)       # Llamado de funcion calcular_puntaje() la cual recibe como argumento la lista de cartas del dealer y se guarda el resultado en la variable puntaje_dealer
    
    for jugador in jugadores:       # Por cada lista de jugador dentro de la lista de jugadores
        puntaje_jugador = calcular_puntaje(jugador[4])      # Llamado de funcion calcular_puntaje() la cual recibe como argumento la lista de cartas del jugador y se almacena en la variable puntaje_jugador
    
        if puntaje_jugador > 21:        # Si el puntaje del jugador es mayor a 21 (significa que perdio automaticamente):
            print(f"El jugador {jugador[1]}, se paso de 21. El dealer gana")        # Imprimimos el resultado de derrota del jugador
            jugador[2] -= jugador[5]        # Restamos la cantidad apostada al saldo del jugador
        elif puntaje_dealer > 21:       # Si no, si el puntaje del dealer es mayor a 21 (significa que el jugador no se paso pero el dealer si):
            print(f"El dealer se paso de 21, El jugador {jugador[1]} gana")     # Imprimimos el resultado de victoria del jugador
            jugador[2] += jugador[5]        # Sumamos la cantidad apostada al saldo del jugador
        elif puntaje_jugador <= 21 and puntaje_dealer <= 21:        # Si no, si el puntaje del jugador es menor o igual a 21, y el puntaje del dealer es menor o igual a 21 (significa que ni el jugado ni el dealer se pasaron de 21):
            if puntaje_jugador > puntaje_dealer:        # Si ninguno se paso, pero el puntaje del jugador es mayor al del dealer:
                print(f"El jugador {jugador[1]} gano sin pasarse")      # Imprimimos el resultado de victoria del jugador
                jugador[2] += jugador[5]        # Sumamos la cantidad apostada al saldo del jugador
            elif puntaje_jugador < puntaje_dealer:      # Si ninguno se paso, pero el puntaje del jugador es menor al del dealer:
                print(f"El jugador {jugador[1]} perdio sin pasarse")        # Imprimimos el resultado de derrota del jugador
                jugador[2] -= jugador[5]        # Restamos la cantidad apostada al saldo del jugador
            else:       # Si no se cumple ninguna opcion, es porque empataron el jugador y el dealer:
                print(f"El jugador {jugador[1]} empato con el dealer")      # Imprimimos el resultado de empate del jugador
        else:       # Si no se cumple ninguna opcion, es porque empataron el jugador y el dealer:
            print(f"El jugador {jugador[1]} empato con el dealer")      # Imprimimos el resultado de empate del jugador
    
    print("\n")     # Imprimimos un espacio
    return jugadores        # Se devuelve la lista de jugadores con los saldos actualizados

# Funcion para eliminar a los jugadores que no continuan jugando
def eliminar_jugadores_retirados(lista_jugadores):      # Definicion de la funcion eliminar_jugadores_retirados() la cual recibe como argumento la lista de jugadores
    jugadores_actualizados = []     # Se inicializa la lista de jugadores actualizada
    
    for jugador in lista_jugadores:     # Por cada lista de jugador en la lista de jugadores
        if jugador[3] == 1:     # Si el valor en la posicion 3 del jugador es 1 significa que esta jugando:
            jugadores_actualizados.append(jugador)      # Se guarda el jugador en la lista de jugadores actualizada
            
    return jugadores_actualizados       # Se devuelve la lista de jugadores actualiza (la cual ya no posee los jugadores que abandonaron el juego)

# Funcion principal del juego blackjack
def juego_blackjack(jugadores, baraja):     # Definicion de la funcion juego_blackjack() la cual recibe como argumento la lista de jugadores y la lista de la baraja
    cartasDealer = []       # Se inicializa la lista de cartas del dealer
    
    # Se reparten las cartas a los jugadores
    for jugador in jugadores:       # Por cada lista de jugador en la lista de jugadores
        cartasJugadores = []        # Se inicializa la lista de cartas del jugador
        print(f"Saldo actual de {jugador[1]}: $", jugador[2])       # Se imprime el saldo actual del jugador junto con su nombre
        apuesta = obtener_apuesta(jugador[2])       # Llamado de funcion obtener_apuesta() la cual recibe el saldo del jugador como apuesta, y se guarda el resultado en la variables apuesta
        
        for _ in range(2):      # Se itera 2 veces:
            if len(baraja) == 0:        # Se verifica que la baraja no este vacia antes de llamar a la funcion pedir_carta()
                baraja = crear_baraja()     # Si esta vacia entonces se llama a la funcion crear_baraja() para crear y mezclar una nueva baraja, y se guarda en la variable baraja
            cartasJugadores.append(pedir_carta(baraja))     # Se llama a la funcion pedir_carta() la cual recibe como argumento la lista de la baraja, y el resultado se ingresa a la lista de cartas del jugador
        jugador.append(cartasJugadores)     # Se añade a la lista del jugador la lista de cartas creada
        jugador.append(apuesta)     # Se añade a la lista del jugador la apuesta realizada
            
    # Se reparten las cartas al dealer
    for _ in range(2):      # Se itera 2 veces:
        if len(baraja) == 0:        # Se verifica que la baraja no este vacia antes de llamar a la funcion pedir_carta()
            baraja = crear_baraja()     # Si esta vacia entonces se llama a la funcion crear_baraja() para crear y mezclar una nueva baraja, y se guarda en la variable baraja         
        cartasDealer.append(pedir_carta(baraja))        # Se llama a la funcion pedir_carta() la cual recibe como argumento la lista de la baraja, y el resultado se ingresa a la lista de cartas del dealer

    # Se muestran las manos, y como recien se entregaron las cartas, el estado del dealer es oculto 
    mostrar_manos(jugadores, cartasDealer, "oculto")        # Se llama a la funcion mostrar_manos() la cual recibe como argumentos la lista de jugadores, la lista de cartas del dealer, y el estado del dealer "oculto"

    # Turno del jugador
    for jugador in jugadores:       # Por cada lista de jugador en la lista de jugadores
        accion = 1      # Se inicializa en 1 la variable accion (utilizada luego para pedir cartas)
        print(f"Turno del jugador {jugador[1]}")        # Se imprime el turno del jugador con su nombre
        while calcular_puntaje(jugador[4]) < 21 and accion != 2:        # Mientras el resultado de la funcion calcular_puntaje() la cual recibe como argumento la lista de cartas del jugador, es menor a 21 y la accion es distinta de 2:
            accion = menu_accion_jugador()      # Llamado de la funcion menu_accion_jugador() y se guarda el resultado en la variable accion
            if accion == 1:     # Si la accion que selecciono el jugador es 1 (significa que el jugador decidio pedir otra carta):
                if len(baraja) == 0:        # Se verifica que la baraja no este vacia antes de llamar a la funcion pedir_carta()
                    baraja = crear_baraja()     # Si esta vacia entonces se llama a la funcion crear_baraja() para crear y mezclar una nueva baraja, y se guarda en la variable baraja
                jugador[4].append(pedir_carta(baraja))      # Se llama a la funcion pedir_carta() la cual recibe como argumento la lista de la baraja, y el resultado se añade a la lista de cartas del jugador
                mostrar_manos(jugadores, cartasDealer, "oculto")        # Se llama a la funcion mostrar_manos() la cual recibe como argumentos la lista de jugadores, la lista de cartas del dealer, y el estado del dealer "oculto"
            else:       # Si la accion no es 1 (significa que el jugador decidio no pedir mas cartas):
                print("¡Te plantaste!")     # Se imprime la seleccion del jugador
                print("\n")     # Se imprime un espacio

    # Turno del dealer
    while calcular_puntaje(cartasDealer) < 17:      # Mientras el resultado de la funcion calcular_puntaje() la cual recibe como argumento la lista de cartas del dealer, es menor a 17:
        cartasDealer.append(pedir_carta(baraja))        # Se llama a la funcion pedir_carta() la cual recibe como argumento la lista de la baraja, y el resultado se ingresa a la lista de cartas del dealer

    # Fin de la ronda, se muestran las manos de los jugadores y la mano completa del dealer
    print("¡Fin de la Ronda!")      # Se imprime el estado de la ronda
    mostrar_manos(jugadores, cartasDealer, "mostrar")       # Se llama a la funcion mostrar_manos() la cual recibe como argumentos la lista de jugadores, la lista de cartas del dealer, y el estado del dealer "mostrar"

    # Determinamos los resultados finales de la ronda
    resultados = determinar_ganador(jugadores, cartasDealer)        # Se llama a la funcion determinar_ganador() la cual recibe como argumentos la lista de jugadores y la lista de cartas del dealer, y guarda los resultado en la variable resultados

    return resultados, baraja       # Devolvemos los resultados de la ronda, y la lista de la baraja actual

# Funcion principal del juego
def main():     # Definicion de la funcion main()
    opcion_menu_inicial = menu_inicial()        # Llamado de funcion menu_inicial y el resultado se guarda en la variable opcion_menu_inicial
    
    if opcion_menu_inicial == 1:        # Si lo que esta en opcion_menu_inicial es 1: (se selecciono jugar en el menu principal)
        numero_jugadores = menu_jugadores()     # Llamado de funcion menu_jugadores y el resultado se guarda en la variable numero_jugadores
        jugadores = menu_info_jugadores(numero_jugadores)       # Llamado de funcion menu_info_jugadores con el numero_jugadores como argumento y el resultado se guarda en la variable jugadores
        jugar_otra = "si"       # Se setea la variable jugar_otra en "si", la cual sera utilizada para el bucle del juego
        primer_juego = "si"     # Se setea la variable primer_juego en "si", la cual sera utilizada para la primera iteracion del bucle del juego
        jugando = numero_jugadores      # Se guarda numero_jugadores en jugando, el cual sera utilizado para controlar el bucle del juego dependiendo la cantidad de jugadores
        baraja = crear_baraja()     # Llamado de funcion crear baraja y el resultado se guarda en la variable baraja
    else:       # Si lo que esta en opcion menu inicial no es 1: (se selecciono salir en el menu principal)
        menu_salir()        # Llamado de funcion menu_salir
        jugar_otra = "no"       # Se setea la variable jugar_otra en "no", la cual sera utilizada para salir del bucle del juego
    
    while jugar_otra == "si" and jugando >= 1:      # Mientras jugar_otra sea "si" y jugando sea mayor o igual a 1: (es decir mientras se seleccione jugar en el menu principal, y la cantidad de jugadores jugando sea mayor o igual a 1)
        if primer_juego == "si":        # Si primer_juego es igual a "si": (sirve unicamente para la primera iteracion del juego y poder utilizar la lista de jugadores default)
            resultado_jugadores, baraja = juego_blackjack(jugadores, baraja)        # Llamado de funcion principal del juego juego_blackjack con la lista de jugadores y la baraja como argumentos, y los resultamos se guardan en resultado_jugadores y baraja
            primer_juego = "no"     # Una vez realizada la primera iteracion del juego, se setea la variable primer_juego a "no"
        else:       # Si ya se realizo la primera iteracion del juego, entonces:
            resultado_jugadores, baraja = juego_blackjack(resultado_jugadores, baraja)      # Llamado de funcion principal del juego juego_blackjack con la lista de jugadores actualizada y la baraja como argumentos, y los resultamos se guardan en resultado_jugadores y baraja
           
        for jugador in resultado_jugadores:     # Por cada lista de jugador dentro de la lista de jugadores resultado_jugadores:
            print(f"Jugador {jugador[1]}:")     # Se imprime el nombre del jugador
            if jugador[2] == 0:     # Si el saldo del jugador es igual a 0:
                opcion = menu_saldo_jugador()       # Llamado de funcion menu_saldo_jugador y el resultado se guarda en la variable opcion
                if opcion == 1:     # Si la opcion es 1: (El jugador decidio agregar mas saldo)
                    saldo_nuevo = ingresar_saldo()      # Llamado de funcion ingresar_saldo y el resultado se guarda en saldo_nuevo
                    jugador[2] = saldo_nuevo        # Se reemplaza y guarda el nuevo saldo ingresado por el jugador en el saldo del jugador 
                    print(f"¡El jugador {jugador[1]}, ingreso mas saldo!")      # Se imprime que el jugador ingreso mas saldo
                    print("\n")     # Se imprime un espacio
                    del jugador[4]      # Se elimina la lista de cartas del jugador de su lista de jugador
                    del jugador[4]      # Se elimina la apuesta anterior del jugador de su lista de jugador (al eliminar las cartas, la apuesta pasa a la posicion 4)
                else:       # Si la opcion no es 1: (El jugador decidio no agregar mas saldo)
                    print(f"¡Gracias por jugar {jugador[1]}! Saldo final: ${jugador[2]}")       # Se imprime un saludo y se muestra el saldo final del jugador
                    print("\n")     # Se imprime un espacio
                    jugador[3] = 0      # Se setea la posicion 3 de la lista del jugador en 0 (Si esta variable esta en 0, significa que el jugador ya no juega mas)
                    resultado_jugadores = eliminar_jugadores_retirados(resultado_jugadores)     # Llamado de funcion eliminar_jugadores_retirados con la lista de jugadores como argumento y el resultado se guarda en resultado_jugadores
                    jugando -= 1        # Se resta 1 a la variable jugando ya que se elimino un jugador
            else:       # Si el saldo del jugador no es igual a 0:
                print(f"Saldo disponible: ${jugador[2]}")       # Se imprime el saldo disponible del jugador
                opcion = menu_continuar_jugador()       # Llamado de funcion menu_continuar_jugando y el resultado se almacena en la variable opcion
                if opcion == 1:     # Si opcion es 1: (El jugador decidio continuar jugando)
                    print(f"¡El jugador {jugador[1]} continua!")        # Se imprime que el jugador continua
                    print("\n")     # Se imprime un espacio
                    del jugador[4]      # Se elimina la lista de cartas del jugador de su lista de jugador
                    del jugador[4]      # Se elimina la apuesta anterior del jugador de su lista de jugador (al eliminar las cartas, la apuesta pasa a la posicion 4)
                else:       # El jugador decidio no continuar jugando:
                    print(f"¡Gracias por jugar {jugador[1]}! Saldo final: ${jugador[2]}")       # Se imprime un saludo y se muestra el saldo final del jugador
                    print("\n")     # Se imprime un espacio
                    jugador[3] = 0      # Se setea la posicion 3 de la lista del jugador en 0 (Si esta variable esta en 0, significa que el jugador ya no juega mas)
                    resultado_jugadores = eliminar_jugadores_retirados(resultado_jugadores)     # Llamado de funcion eliminar_jugadores_retirados con la lista de jugadores como argumento y el resultado se guarda en resultado_jugadores
                    jugando -= 1        # Se resta 1 a la variable jugando ya que se elimino un jugador
        
# Llamado de la funcion principal para que comience el programa
main()      # Llamamos a la funcion main()