# param lista: lista de paquete
# param fecha_inicio_día: el día de la fecha de inicio del viaje.
# param fecha_inicio_mes: mes de la fecha de inicio.
# param fecha_inicio_año: año de la fecha de inicio.
# param fecha_fin_día: día de fecha de finalización.
# param fecha_fin_mes: mes de fecha de finalización.
# param fecha_fin_año: año de fecha de finalización.
# param destino: el destino.
# param precio: el precio.
# return: lista de paquetes creados.

from ValidacionErrores import validar_paquete
from Paquete import crear_paquete, mostrar_paquete

# param lista: la lista donde se agregarán los paquetes
# param paquete: el paquete que se agregará
# return: lista de paquetes

def agregar_lista(lista, paquete):
    lista.append(paquete)

def agregar_paquete_servicio(lista, fecha_inicio_dia, fecha_inicio_mes, fecha_inicio_año, fecha_fin_dia, fecha_fin_mes, fecha_fin_año, destino, precio):
    paquete = crear_paquete(fecha_inicio_dia, fecha_inicio_mes, fecha_inicio_año, fecha_fin_dia, fecha_fin_mes, fecha_fin_año, destino, precio)
    validar_paquete(paquete)
    agregar_lista(lista, paquete)
    return lista

def mostrar_paquetes_servicio(lista):
    for i in range(0,len(lista)):
        mostrar_paquete(lista[i])
    return lista

def modificar_paquete_servicio(lista, i, fecha_inicio_dia_nuevo, fecha_inicio_mes_nuevo, fecha_inicio_año_nuevo, fecha_fin_dia_nuevo, fecha_fin_mes_nuevo, fecha_fin_año_nuevo, destino_nuevo, precio_nuevo):
    paquete_nuevo=crear_paquete(fecha_inicio_dia_nuevo, fecha_inicio_mes_nuevo, fecha_inicio_año_nuevo, fecha_fin_dia_nuevo, fecha_fin_mes_nuevo, fecha_fin_año_nuevo, destino_nuevo, precio_nuevo)
    lista[i] = paquete_nuevo
    return lista

def eliminar_paquete_servicios_destino(lista, destino_deseado):
    for i in range(0, len(lista)):
        if lista[i]['destino'] == destino_deseado:
            del(lista[i])
    return lista

def numeros_entre_dos_fechas(dia1, mes1, año1, dia2, mes2, año2):
    año = año2 - año1
    mes = mes2 - mes1
    dia = dia2 - dia1
    res = 0
    if año == 0:
        res = 30 * mes + dia
    else:
        res = año * 365 - 30 * mes - dia
    return res

def eliminar_paquete_duración_del_servicio_corta(lista, num_dias_deseado):
    for i in range(0, len(lista)):
        if numeros_entre_dos_fechas(lista[i]['fecha_inicio_dia'], lista[i]['fecha_inicio_mes'], lista[i]['fecha_inicio_año'], lista[i]['fecha_fin_dia'], lista[i]['fecha_fin_mes'], lista[i]['fecha_fin_año']) < num_dias_deseado:
            del(lista[i])
    return lista

def eliminar_paquete_precio_servicio(lista, precio_deseado):
    i = len(lista) - 1
    while (i >= 0):
        if lista[i]["precio"]>precio_deseado:
            del (lista[i])
        i = i - 1
    return lista

def imprimir_fecha_destino_precio_menor_servicio(lista, fecha_destino, precio_dado):
    lista_nueva=[]
    for i in range(0, len(lista)):
        if lista[i]['destino'] == fecha_destino:
            if lista[i]['precio'] < precio_dado:
                lista_nueva.append(lista[i])
    return lista_nueva


