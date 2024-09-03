
# param fecha_inicio_día: el día de la fecha de inicio del viaje, parámetro de tipo int
# param fecha_inicio_mes: mes de la fecha de inicio, parámetro de tipo int
# param fecha_inicio_año: año de la fecha de inicio, parámetro de tipo int
# param fecha_fin_día: día de fecha de finalización, parámetro de tipo int
# param fecha_fin_mes: mes de fecha de finalización, parámetro de tipo int
# param fecha_fin_año: año de fecha de finalización, parámetro de tipo int
# param destino: destino, parámetro de tipo int
# param precio: precio, parámetro de tipo flotante
# return: El paquete de viaje, parámetro de tipo de paquete.


def crear_paquete(fecha_inicio_día, dfecha_inicio_mes, fecha_inicio_año, fecha_fin_día, fecha_fin_mes, fecha_fin_año, destino, precio):
    return{
        "fecha_inicio_día":fecha_inicio_día,
        "fecha_inicio_mes":dfecha_inicio_mes,
        "fecha_inicio_año":fecha_inicio_año,
        "fecha_fin_día":fecha_fin_día,
        "fecha_fin_mes":fecha_fin_mes,
        "fecha_fin_año":fecha_fin_año,
        "destino":destino,
        "precio":precio
    }

def obtener_fecha_inicio_día(paquete):
    return paquete["fecha_inicio_día"]

def obtener_fecha_fin_día(paquete):
    return paquete["fecha_fin_día"]

def obtener_fecha_inicio_mes(paquete):
    return paquete["fecha_inicio_mes"]

def obtener_fecha_fin_mes(paquete):
    return paquete["fecha_fin_mes"]

def obtener_fecha_inicio_año(paquete):
    return paquete["fecha_inicio_año"]

def obtener_fecha_fin_año(paquete):
    return paquete["fecha_fin_año"]

def obtener_destino(paquete):
    return paquete["destino"]

def obtener_precio(paquete):
    return paquete["precio"]

def mostrar_fechainicio(paquete):
    print(obtener_fecha_inicio_día(paquete), '/', obtener_fecha_inicio_mes(paquete), '/',obtener_fecha_inicio_año(paquete))

def mostrar_fechafinal(paquete):
    print(obtener_fecha_fin_día(paquete), '/', obtener_fecha_fin_mes(paquete), '/',obtener_fecha_fin_año(paquete))

def mostrar_paquete(paquete):
    print(obtener_fecha_inicio_día(paquete), '/', obtener_fecha_inicio_mes(paquete), '/', obtener_fecha_inicio_año(paquete), '-', obtener_fecha_fin_día(paquete), '/', obtener_fecha_fin_mes(paquete), '/', obtener_fecha_fin_año(paquete), '-', obtener_destino(paquete), '-', obtener_precio(paquete))


