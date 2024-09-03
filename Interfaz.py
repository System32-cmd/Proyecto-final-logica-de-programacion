from Servicios import agregar_paquete_servicio, mostrar_paquetes_servicio, eliminar_paquete_servicios_destino, eliminar_paquete_duración_del_servicio_corta, eliminar_paquete_precio_servicio, modificar_paquete_servicio, imprimir_fecha_destino_precio_menor_servicio
from Paquete import mostrar_paquete


lista =  []
# Funcion agregar paquetes opcion 1
def agregar_paquete(lista):
    try:
        fecha_inicio_dia = int(input("Introduzca el día de la fecha de inicio: "))
    except:
        print("Fecha de inicio no válida")
        fecha_inicio_dia = int(input("Introduzca el día de la fecha de inicio: "))

    try:
        fecha_inicio_mes = int(input("Introduzca el mes de la fecha de inicio: "))
    except:
        print("El mes de la fecha de inicio no es válido")
        fecha_inicio_mes = int(input("Introduzca el mes de la fecha de inicio: "))

    try:
        fecha_inicio_año = int(input("Introduzca el año de la fecha de inicio: "))
    except:
        print("Año de fecha de inicio no válido")
        fecha_inicio_año = int(input("Introduzca el año de la fecha de inicio: "))
    try:
        fecha_fin_dia = int(input("Introduzca el día de la fecha de finalización: "))
    except:
        print("Fecha de finalización no válida")
        fecha_fin_dia = int(input("Introduzca el día de la fecha de finalización: "))

    try:
        fecha_fin_mes = int(input("Introduzca el mes de la fecha de finalización:"))
    except:
        print("Mes de fecha de finalización no válido")
        fecha_fin_mes = int(input("Introduzca el mes de la fecha de finalización:"))

    try:
        fecha_fin_año = int(input("Introduzca el año de la fecha de finalización:"))
    except:
        print("Año de fecha de finalización no válida")
        fecha_fin_año = int(input("Ingrese el año de la fecha final:"))

    try:
        destino = str(input("Introduzca el destino:"))
    except:
        print("Destino no válido")
        destino = str(input("Introduzca el destino:"))

    try:
        precio = float(input("Introduzca el precio:"))
    except:
        print("Precio no válido")
        precio = float(input("Introduzca el precio:"))

    agregar_paquete_servicio(lista, fecha_inicio_dia, fecha_inicio_mes, fecha_inicio_año, fecha_fin_dia, fecha_fin_mes, fecha_fin_año, destino, precio)

# Funcion mostrar paquetes opcion 2
def mostrar_paquetes(lista):
    if len(lista) < 1:
        print("Aún no hay paquetes")
    else:
        mostrar_paquetes_servicio(lista)

# Funcion modificar paquete  opcion 3
def modificar_paquete(lista):
    if len(lista) < 1:
        print("Aún no hay paquetes")
    else:
        nuevo_dia_fecha_inicio = int(input("Nuevo día de comienzo:"))
        nuevo_mes_fecha_de_inicio = int(input("Nuevo mes de inicio:"))
        nuevo_año_fecha_de_inicio = int(input("Nuevo año de inicio:"))
        nuevo_dia_fecha_final = int(input("Nuevo día de finalización:"))
        nuevo_mes_fecha_final = int(input("Nuevo mes de finalización:"))
        nuevo_año_fecha_final = int(input("Nuevo fin de año:"))
        nuevo_destino = str(input("el nuevo destino"))
        nuevo_precio = float(input("Precio nuevo"))
        pos = int(input("La posición del paquete que desea modificar:"))
        modificar_paquete_servicio(lista, pos, nuevo_dia_fecha_inicio, '/', nuevo_mes_fecha_de_inicio, '/', nuevo_año_fecha_de_inicio, '-', nuevo_dia_fecha_final, '/',nuevo_mes_fecha_final, '/', nuevo_año_fecha_final, nuevo_destino, nuevo_precio)
        mostrar_paquetes_servicio(lista)

# Funcion eliminar paquetes por destino opcion 4
def eliminar_destino(lista):
    if len(lista) < 1:
        print("Aún no hay paquetes")
    else:
        destino = str(input("Elija el destino deseado:"))
        eliminar_paquete_servicios_destino(lista, destino)
        mostrar_paquetes_servicio(lista)

#  Funcion eliminar paquetes por duracion opcion 5
def eliminar_duración_dias(lista):
    if len(lista) < 1:
        print("Aún no hay paquetes")
    else:
        dia = int(input("Ingrese el número de días deseado:"))
        eliminar_paquete_duración_del_servicio_corta(lista, dia)
        mostrar_paquetes_servicio(lista)

#  Funcion eliminar paquetes por precio de la opcion 6
def eliminar_precio(lista):
    if len(lista) < 1:
        print("Aún no hay paquetes")
    else:
        precio = float(input("Introduzca el precio deseado:"))
        eliminar_paquete_precio_servicio(lista, precio)
        mostrar_paquetes_servicio(lista)

#  Funcion mostrar paquetes segun un presupuesto opcion 7
def imprimir_fecha_destino_precio_menor_servicio(lista):
    if len(lista) < 1:
        print("Aún no hay paquetes")
    else:
        dest = str(input("Ingrese el destino deseado: "))
        precio = float(input("Introduzca el precio deseado: "))
    nueva_lista = imprimir_fecha_destino_precio_menor_servicio(lista, dest, precio)
    for i in range(0, len(nueva_lista)):
        mostrar_paquete(nueva_lista[i])

# Funcion para agregar un cliente opcion 8
clientes = []
def agregar_cliente():
    nombre = str(input("Ingrese el nombre del cliente: "))
    apellido = str(input("Ingrese el apellido del cliente: "))
    email = input("Ingrese el email del cliente: ")
    telefono = int(input("Ingrese el telefono del cliente: "))
    cliente = {"id": len(clientes) + 1, "nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono}
    clientes.append(cliente)
    print("Cliente agregado con éxito!")
    # Agregar el cliente a la lista de clientes

# Funcion para visualizar los clientes opcion 9
def visualizar_clientes():
    print("Clientes agregados:")
    for cliente in clientes:
        print(cliente)

# Funcion para eliminar un cliente opcion 10
def eliminar_cliente():
    print("Clientes agregados:")
    for i, cliente in enumerate(clientes):
        print(f"{i+1}. {cliente}")
    opcion = input("Ingrese el número del cliente que desea eliminar: ")
    try:
        opcion = int(opcion)
        if opcion > 0 and opcion <= len(clientes):
            del clientes[opcion-1]
            print("Cliente eliminado con éxito.")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")

# Funcion para agregar un vuelo opcion 11
vuelos = []
def agregar_vuelo():
    id_vuelo = len(vuelos) + 1
    origen = str(input("Ingrese el origen del vuelo: "))
    destino = str(input("Ingrese el destino del vuelo: "))
    dia_salida = int(input("Ingrese el día de salida del vuelo: "))
    mes_salida = input("Ingrese el mes de salida del vuelo: ")
    año_salida = int(input("Ingrese el año de salida del vuelo: "))
    hora_salida = input("Ingrese la hora de salida del vuelo: ")
    vuelo = {"id": id_vuelo, "origen": origen, "destino": destino, "fecha_salida": (dia_salida, '/', mes_salida, '/', año_salida), '-' "hora_salida": hora_salida}
    vuelos.append(vuelo)
    print("Vuelo agregado con éxito!")

# Funcion para visualizar los vuelos opcion 12
def visualizar_vuelos():
    print("Vuelos agregados:")
    for vuelo in vuelos:
        print(vuelo)

# Funcion para eliminar un vuelo opcion 13
def eliminar_vuelo():
    print("Vuelos agregados:")
    for i, vuelo in enumerate(vuelos):
        print(f"{i+1}. {vuelo}")
    opcion = int(input("Ingrese el número del vuelo que desea eliminar: "))
    try:
        opcion = int(opcion)
        if opcion > 0 and opcion <= len(vuelos):
            del vuelos[opcion-1]
            print("Vuelo eliminado con éxito.")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")

# Funcion para agregar un hotel opcion 14
hoteles = []
def agregar_hotel():
    id_hotel = len(hoteles) + 1
    nombre = input("Ingrese el nombre del hotel: ")
    direccion = input("Ingrese la direccion del hotel: ")
    hotel = {"id": id_hotel, "nombre": nombre, "direccion": direccion}
    hoteles.append(hotel)
    print("Hotel agregado con éxito!")

# Funcion para visualizar los hoteles opcion 15
def visualizar_hoteles():
    print("Hoteles agregados:")
    for hotel in hoteles:
        print(hotel)

# Funcion para eliminar un hotel opcion 16
def eliminar_hotel():
    print("Hoteles agregados:")
    for i, hotel in enumerate(hoteles):
        print(f"{i+1}. {hotel}")
    opcion = input("Ingrese el número del hotel que desea eliminar: ")
    try:
        opcion = int(opcion)
        if opcion > 0 and opcion <= len(hoteles):
            del hoteles[opcion-1]
            print("Hotel eliminado con éxito.")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")

# Funcion para realizar una reserva de vuelo opcion 17
reservas = []
def realizar_reserva_vuelo():
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(vuelo)
    id_vuelo = int(input("Ingrese el id del vuelo que desea reservar: "))
    vuelo = next((vuelo for vuelo in vuelos if vuelo["id"] == id_vuelo), None)
    if vuelo:
        cliente_id = int(input("Ingrese el id del cliente que realiza la reserva: "))
        cliente = next((cliente for cliente in clientes if cliente["id"] == cliente_id), None)
        if cliente:
            reserva = {"id": len(reservas) + 1, "vuelo": vuelo, "cliente": cliente}
            reservas.append(reserva)
            print("Reserva realizada con éxito!")
        else:
            print("Cliente no encontrado")
    else:
        print("Vuelo no encontrado")

# Funcion para realizar una reserva de hotel opcion 18
def realizar_reserva_hotel():
    print("Hoteles disponibles:")
    for hotel in hoteles:
        print(hotel)
    id_hotel = int(input("Ingrese el id del hotel que desea reservar: "))
    hotel = next((hotel for hotel in hoteles if hotel["id"] == id_hotel), None)
    if hotel:
        cliente_id = int(input("Ingrese el id del cliente que realiza la reserva: "))
        cliente = next((cliente for cliente in clientes if cliente["id"] == cliente_id), None)
        if cliente:
            reserva = {"id": len(reservas) + 1, "hotel": hotel, "cliente": cliente}
            reservas.append(reserva)
            print("Reserva realizada con éxito!")
        else:
            print("Cliente no encontrado")
    else:
        print("Hotel no encontrado")

# funciones para visualizar y eliminar reservas opcion 19 - 22
def visualizar_reservas_vuelos():
    print("Reservas de vuelos:")
    for reserva in reservas:
        if "vuelo" in reserva:
            print(reserva)

def visualizar_reservas_hoteles():
    print("Reservas de hoteles:")
    for reserva in reservas:
        if "hotel" in reserva:
            print(reserva)

def eliminar_reserva_vuelo():
    print("Reservas de vuelos:")
    for i, reserva in enumerate(reservas):
        if "vuelo" in reserva:
            print(f"{i+1}. {reserva}")
    opcion = input("Ingrese el número de la reserva que desea eliminar: ")
    try:
        opcion = int(opcion)
        if opcion > 0 and opcion <= len(reservas):
            for reserva in reservas:
                if "vuelo" in reserva:
                    del reservas[opcion-1]
                    print("Reserva de vuelo eliminada con éxito.")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")

def eliminar_reserva_hotel():
    print("Reservas de hoteles:")
    for i, reserva in enumerate(reservas):
        if "hotel" in reserva:
            print(f"{i+1}. {reserva}")
    opcion = input("Ingrese el número de la reserva que desea eliminar: ")
    try:
        opcion = int(opcion)
        if opcion > 0 and opcion <= len(reservas):
            for reserva in reservas:
                if "hotel" in reserva:
                    del reservas[opcion-1]
                    print("Reserva de hotel eliminada con éxito.")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")

# Imprime el menú principal.
def print_menu():
    print("=====Menú=====")
    print("   1. Agregar paquete de viaje")
    print("   2. Visualización de todos los paquetes de viaje")
    print("   3. Cambiar paquete de viaje")
    print("   4. Eliminar todos los paquetes de viaje disponibles para un destino determinado")
    print("   5. Eliminar todos los paquetes de viaje que tengan una duración inferior a un número determinado de días")
    print("   6. Eliminar todos los paquetes de viaje que tengan un precio superior a una cantidad determinada")
    print("   7. Imprimir paquetes de viaje con un destino determinado y con un precio inferior a una cantidad determinada")
    print("   8. Agregar cliente")
    print("   9. Visualizar todos los clientes")
    print("   10. Eliminar cliente")
    print("   11. Agregar vuelo")
    print("   12. Visualizar vuelos")
    print("   13. Eliminar vuelo")
    print("   14. Agregar hotel")
    print("   15. Visualizar hoteles")
    print("   16. Eliminar hotel")
    print("   17. Realizar reserva de vuelo")
    print("   18. Realizar reserva de hotel")
    print("   19. Visualizar reservas de vuelos")
    print("   20. Visualizar reservas de hoteles")
    print("   21. Eliminar reserva de vuelo")
    print("   22. Eliminar reserva de hotel")
    print("   23. Salir")

# Implementa las opciones del menu.
def run_menu():
    finalizar = False
    while not finalizar:
        print_menu()
        opcion = input("Ingrese la opción deseada: ").strip()
        if opcion == '1':
            agregar_paquete(lista)
        elif opcion == '2':
            mostrar_paquetes(lista)
        elif opcion == '3':
            modificar_paquete(lista)
        elif opcion == '4':
            eliminar_destino(lista)
        elif opcion == '5':
            eliminar_duración_dias(lista)
        elif opcion == '6':
            eliminar_precio(lista)
        elif opcion == '7':
            imprimir_fecha_destino_precio_menor_servicio(lista)
        elif opcion == "8":
            agregar_cliente()
        elif opcion == "9":
            visualizar_clientes()
        elif opcion == "10":
            eliminar_cliente()
        elif opcion == "11":
            agregar_vuelo()
        elif opcion == "12":
            visualizar_vuelos()
        elif opcion == "13":
            eliminar_vuelo()
        elif opcion == "14":
            agregar_hotel()
        elif opcion == "15":
            visualizar_hoteles()
        elif opcion == "16":
            eliminar_hotel()
        elif opcion == "17":
            realizar_reserva_vuelo()
        elif opcion == "18":
            realizar_reserva_hotel()
        elif opcion == "19":
            visualizar_reservas_vuelos()
        elif opcion == "20":
            visualizar_reservas_hoteles()
        elif opcion == "21":
            eliminar_reserva_vuelo()
        elif opcion == "22":
            eliminar_reserva_hotel()
        elif opcion == "23":
            print("Gracias por utilizar nuestro sistema de reservas.")
            finalizar
            exit()
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
