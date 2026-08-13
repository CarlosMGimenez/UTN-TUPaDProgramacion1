# Ejercicio 1— “Caja del Kiosco”

#Variable
descuento = 10

while True: #Nombre de usuario
    #Pedimos nombre
    nombre_ingresado = input("Ingrese su nombre: ")

    if nombre_ingresado == "":
        print("Debe ingresar un nombre válido")
        continue
    #Validamos si ingresa letras    
    if nombre_ingresado.isalpha():
        nombre_usu = nombre_ingresado
        break
    else:
        print("Ingrese un nombre Válido")
        continue

while True: # cantidad de productos

    #pedimos cantidad de productos
    cant_productos = input("Ingrese las productos que necesita: ")

    #Validamos si ingresa valores vacios 
    if cant_productos == "":
        print("El campo no puede quedar vacio. Ingrese las productos que necesita: ")
        continue

    #Validamos si ingresa valores negativos 
    if cant_productos[0] == "-" and cant_productos[1:].isdigit():
        print("Debe ingresar números enteros mayores a 0")
        continue

    if cant_productos.isdigit():
            productos_ingresados = int(cant_productos)
    else:
        print("Ingrese números enteros válidos")
        continue
            
       
    if productos_ingresados == 0:
        print("Ingrese un valor mayor a cero")
        continue
       
    break



# ACUMULADORES
total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0

        

   

for i in range(1, productos_ingresados + 1):

    while True: 

        tiene_descuento = False
            
        precio_ingresado = input(f"Ingrese el precio del producto Nª {i} ")

        #Validamos si ingresa valores vacios
        if precio_ingresado == "":
            print("El campo no puede quedar vacio. Ingrese las entradas que necesita: ")
            continue
            
        #Validamos si ingresa valores negativos 
        if precio_ingresado[0] == "-" and precio_ingresado[1:].isdigit():
            print("Debe ingresar números enteros mayores a 0")
            continue
            
        if precio_ingresado.isdigit():
            precio = int(precio_ingresado)
            
        else:
            print("Ingrese números enteros válidos")
            continue

        break


    #Tiene descuento??
    while True: #pedir descuento
        ahorro = 0
        pide_descuento = input("Tiene Descuento?? Elija S para 'SI', N para 'NO' ").upper()    

        if pide_descuento == "S":
            tiene_descuento = True
            ahorro = precio * descuento / 100
            totalcondesc = precio - ahorro
            break
        elif pide_descuento == "N":
            tiene_descuento = False 
            totalcondesc = precio  
            break
        else:
            print("Elija entre las opcion S para 'SI', N para 'NO'. Intente nuevamente ")
            continue

    #acumulamos
    total_con_descuentos = total_con_descuentos + totalcondesc
    total_sin_descuentos = total_sin_descuentos + precio
    ahorro_total = ahorro_total + ahorro

    
        

#promedio      
promedio = float(total_con_descuentos / productos_ingresados) 

print(f"Cliente: {nombre_usu} ")
print(f"Cantidad de productos: {productos_ingresados}")

print("*************************************************")
print(f"Total sin descuento: {total_sin_descuentos} ")
print(f"Total con descuento: {total_con_descuentos} ")
print(f"Ahorro: {ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#**************************************************
#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#**************************************************
#Credenciales
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 3
acceso = False


for i in range(1, intentos + 1):
    #Ingreso de usuario
    print("Ingrese su usuario y contraseña\n")
    
    while True:
        usuario_ingresado = input(f"Intento {i}/{intentos} - Usuario: ") 
        clave_ingresada   = input("Contraseña: ")
        #Validación de datos 
        if usuario_ingresado =="" or clave_ingresada == "":
            print("Hay campos sin completar. Por favor ingrese los datos correspondientes.")
            continue
        else:
            break
    if (usuario_ingresado != usuario_correcto) or (clave_ingresada != clave_correcta):
        print("Las credenciales no coinciden. Verifique")
        if i == intentos:
            print("Usuario Bloqueado")
            break        
    else: #Le damos acceso
        acceso = True
        break


#Una vez que ya tiene acceso mostramos menú con opciones
if acceso == True :
    print("Elija una opción entre 1 y 4 del siguiente menú\n")

    #Menú de opciones
    while True:
       
        print("1- Estado.")
        print("2- Cambiar Clave.")
        print("3- Mensaje.")
        print("4- Salir")

       

        opciones_menu_ingresada = input("Selecciona una opción: ")

        #Validación de las opciones
        if not opciones_menu_ingresada.isdigit():
            print("Por favor ingrese una de las opciones. Entre 1 y 4")
            continue
        else: 
            opcion_valida = int(opciones_menu_ingresada)
            if opcion_valida == 0 or opcion_valida > 4:
                print("Opcion fuera de rango. Intente de nuevo")
                continue
            break
    #Estado        
    if opcion_valida == 1:
        print("Inscripto")
    #Cambiar Clave
    elif opcion_valida == 2:
        while True:
            nueva_clave = input("Ingrese la nueva Clave: ")
            if nueva_clave == "":
                print("La clave esta vacia. Intente nuevamente!!")
                continue
            elif len(nueva_clave) < 6:
                print("La clave debe tener minimo 6 caracteres!")
                continue
            clave_correcta = nueva_clave
            print("La clave se modifico correctamente!")    
            break   
    #Mensaje    
    elif opcion_valida == 3:
        print("No esperes saber Delphi para empezar: empezá con Delphi, y cada línea te va a enseñar a saber.") 

    #Salir opcion 4
    elif opcion_valida == 4:
        print("Gracias. Hasta la proxima")


#***********************************************
# Ejercicio 3 — Agenda de Turnos con Nombres
#**********************************************

# Ingreso de Operador
while True:
    operador_ingresado = input("Ingrese el nombre del operador: ")

    if operador_ingresado == "":
        print("El nombre no puede quedar vacío")
        continue

    if operador_ingresado.isalpha():
        operador = operador_ingresado
        break
    else:
        print("Ingrese solamente letras")


# Turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


# Menú de opciones
while True:

    print("1- Reservar turno")
    print("2- Cancelar turno")
    print("3- Ver agenda del día")
    print("4- Ver resumen general")
    print("5- Cerrar sistema")

    opcion_ingresada = input("Elija una opción: ")

    if not opcion_ingresada.isdigit():
        print("Ingrese un número del 1 al 5")
        continue

    opcion = int(opcion_ingresada)

    if opcion == 0 or opcion > 5:
        print("Opción fuera de rango")
        continue


    # Reservar
    if opcion == 1:

        while True:
            dia_ingresado = input("Elija el día: 1-Lunes / 2-Martes: ")

            if not dia_ingresado.isdigit():
                print("Ingrese 1 o 2")
                continue

            dia = int(dia_ingresado)

            if dia < 1 or dia > 2:
                print("Opción fuera de rango")
                continue

            break


        while True:
            paciente_ingresado = input("Ingrese el nombre del paciente: ")

            if paciente_ingresado == "":
                print("El nombre no puede quedar vacío")
                continue

            if paciente_ingresado.isalpha():
                paciente = paciente_ingresado
                break
            else:
                print("Ingrese solamente letras")


        if dia == 1:

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno el Lunes")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente")

            else:
                print("No hay turnos disponibles el Lunes")


        elif dia == 2:

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno el Martes")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente")

            else:
                print("No hay turnos disponibles el Martes")


    # Cancelar
    elif opcion == 2:

        while True:
            dia_ingresado = input("Elija el día: 1-Lunes / 2-Martes: ")

            if not dia_ingresado.isdigit():
                print("Ingrese 1 o 2")
                continue

            dia = int(dia_ingresado)

            if dia == 0 or dia > 2:
                print("Opción fuera de rango")
                continue

            break


        while True:
            paciente_ingresado = input("Ingrese el nombre del paciente: ")

            if paciente_ingresado == "":
                print("El nombre no puede quedar vacío")
                continue

            if paciente_ingresado.isalpha():
                paciente = paciente_ingresado
                break
            else:
                print("Ingrese solamente letras")


        if dia == 1:

            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado")

            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado")

            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado")

            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado")

            else:
                print("El paciente no tiene turno el Lunes")


        elif dia == 2:

            if paciente == martes1:
                martes1 = ""
                print("Turno cancelado")

            elif paciente == martes2:
                martes2 = ""
                print("Turno cancelado")

            elif paciente == martes3:
                martes3 = ""
                print("Turno cancelado")

            else:
                print("El paciente no tiene turno el Martes")


    # Ver agenda
    elif opcion == 3:

        while True:
            dia_ingresado = input("Elija el día: 1-Lunes / 2-Martes: ")

            if not dia_ingresado.isdigit():
                print("Ingrese 1 o 2")
                continue

            dia = int(dia_ingresado)

            if dia < 1 or dia > 2:
                print("Opción fuera de rango")
                continue

            break


        if dia == 1:

            print("Agenda Lunes")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")


        elif dia == 2:

            print("Agenda Martes")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")


    # Resumen
    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1

        if martes1 != "":
            ocupados_martes = ocupados_martes + 1

        if martes2 != "":
            ocupados_martes = ocupados_martes + 1

        if martes3 != "":
            ocupados_martes = ocupados_martes + 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print(f"Lunes: {ocupados_lunes} ocupados - {disponibles_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados - {disponibles_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")

        else:
            print("Hay empate")


    # Salir
    elif opcion == 5:
        print(f"Gracias {operador}. Sistema cerrado.")
        break


#************************************************************
# Ejercicio 4  Escape Room: La Bóveda
#************************************************************

# Variables 
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueado = False


# Ingreso del agente

while True:

    nombre_ingresado = input("Ingrese el nombre del agente: ")

    if nombre_ingresado == "":
        print("El nombre no puede quedar vacío")
        continue

    if nombre_ingresado.isalpha():
        nombre_agente = nombre_ingresado
        break
    else:
        print("Ingrese solamente letras")


# Juego

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False:

    print("***************************************")
    print(f"Agente: {nombre_agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print("***************************************")

    print("1- Forzar cerradura")
    print("2- Hackear panel")
    print("3- Descansar")

    opcion_ingresada = input("Elija una opción: ")

    if not opcion_ingresada.isdigit():
        print("Ingrese una opción entre 1 y 3")
        continue

    opcion = int(opcion_ingresada)

    if opcion < 1 or opcion > 3:
        print("Opción fuera de rango")
        continue


    # Forzar cerradura
    if opcion == 1:

        energia = energia - 20
        tiempo = tiempo - 2

        forzar_seguidas = forzar_seguidas + 1

        if forzar_seguidas == 3:

            print("La cerradura se trabó")
            print("ALARMA ACTIVADA!")
            alarma = True

        else:
            if energia < 40:

                while True:
                    numero_ingresado = input("Ingrese un número entre 1 y 3: ")

                    if not numero_ingresado.isdigit():
                        print("Ingrese un número válido")
                        continue

                    numero = int(numero_ingresado)

                    if numero < 1 or numero > 3:
                        print("Ingrese un número entre 1 y 3")
                        continue
                    break

                if numero == 3:
                    alarma = True
                    print("ALARMA ACTIVADA!")

            if alarma == False:

                cerraduras_abiertas = cerraduras_abiertas + 1
                print("Cerradura abierta correctamente")


    # Hackear panel
    elif opcion == 2:

        forzar_seguidas = 0

        energia = energia - 10
        tiempo = tiempo - 3

        print("Iniciando hackeo...")

        for i in range(1, 5):

            codigo_parcial = codigo_parcial + "A"
            print(f"Paso {i}/4 - Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas = cerraduras_abiertas + 1
            print("Se abrió una cerradura automáticamente")


    # Descansar
    elif opcion == 3:

        forzar_seguidas = 0

        energia = energia + 15

        if energia > 100:
            energia = 100

        tiempo = tiempo - 1

        if alarma == True:
            energia = energia - 10
            print("La alarma está activa. Perdió 10 de energía extra.")

        print("Descansó y recuperó energía.")


    # Bloqueo por alarma

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:

        print("La alarma bloqueó el sistema.")
        bloqueado = True
        break


# Resultado final

if cerraduras_abiertas == 3:

    print("***************************************")
    print("VICTORIA!")
    print("Abriste las 3 cerraduras")
    print("***************************************")

elif bloqueado == True:

    print("***************************************")
    print("DERROTA")
    print("El sistema quedó bloqueado.")
    print("***************************************")

elif energia <= 0 or tiempo <= 0:

    print("***************************************")
    print("DERROTA")
    print("Te quedaste sin energía o sin tiempo.")
    print("***************************************")


#************************************************************
# Ejercicio 5 — "Escape Room: La Arena del Gladiador"
#************************************************************

# Nombre del Gladiador
while True:

    nombre_ingresado = input("Nombre del Gladiador: ")

    if nombre_ingresado == "":
        print("Error: Solo se permiten letras.")
        continue

    if nombre_ingresado.isalpha():
        nombre_gladiador = nombre_ingresado
        break
    else:
        print("Error: Solo se permiten letras.")


# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True


print("--- BIENVENIDO ---")
print("=== INICIO DEL COMBATE ===")


# Combate
while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador == True:

        print(f"{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        while True:

            opcion_ingresada = input("Opción: ")

            if not opcion_ingresada.isdigit():
                print("Error: Ingrese un número válido.")
                continue

            opcion = int(opcion_ingresada)

            if opcion < 1 or opcion > 3:
                print("Error: Elija una opción entre 1 y 3.")
                continue

            break


        # Ataque Pesado
        if opcion == 1:

            if vida_enemigo < 20:
                daño = ataque_pesado * 1.5
                print("¡Golpe Crítico!")
            else:
                daño = float(ataque_pesado)

            vida_enemigo = vida_enemigo - daño

            print(f"¡Atacaste al enemigo por {daño} puntos de daño!")


        # Ráfaga Veloz
        elif opcion == 2:

            print("¡Inicias una ráfaga de golpes!")

            for i in range(3):

                vida_enemigo = vida_enemigo - 5

                print("> Golpe conectado por 5 de daño")


        # Curar
        elif opcion == 3:

            if pociones > 0:

                vida_jugador = vida_jugador + 30
                pociones = pociones - 1

                print("Te curaste 30 puntos de vida.")

            else:

                print("¡No quedan pociones!")


        turno_gladiador = False


    # Turno del enemigo
    if turno_gladiador == False and vida_jugador > 0 and vida_enemigo > 0:

        vida_jugador = vida_jugador - ataque_enemigo

        print("¡El enemigo te atacó por 12 puntos de daño!")

        turno_gladiador = True


# Fin del juego
if vida_jugador > 0:

    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")

else:

    print("DERROTA. Has caído en combate.")
    
        










