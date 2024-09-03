# Importacion de funciones desde paquete.py
from Paquete import obtener_fecha_inicio_día, obtener_fecha_inicio_mes, obtener_fecha_inicio_año, obtener_fecha_fin_día, \
    obtener_fecha_fin_mes, obtener_fecha_fin_año, obtener_precio, obtener_destino

# Acontinuacion se valida si para la los valores ingresados para cada uno de los parametros no cumple con el tipo de dato permitido y si es así se lanza el mensaje de error

#la función isinstance() va a comprobar si el primer argumento pertenece a la clase enviada como segundo argumento
def validar_paquete(paquete):
    error = ""
    if isinstance(obtener_fecha_inicio_día(paquete), str) == True:
        error += "dia de inicio no válido\n"
    if isinstance(obtener_fecha_inicio_día(paquete), float) == True:
        error += "dia de inicio no válido\n"
    if isinstance(obtener_fecha_inicio_mes(paquete), str) == True:
        error += "mes de inicio no válido\n"
    if isinstance(obtener_fecha_inicio_mes(paquete), float) == True:
        error += "mes de inicio no válido\n"
    if isinstance(obtener_fecha_inicio_año(paquete), str) == True:
        error += "año de inicio no válido\n"
    if isinstance(obtener_fecha_inicio_año(paquete), float) == True:
        error += "año de inicio no válido\n"
    if isinstance(obtener_fecha_fin_día(paquete), str) == True:
        error += "dia final no válido\n"
    if isinstance(obtener_fecha_fin_día(paquete), float) == True:
        error += "dia final no válido\n"
    if isinstance(obtener_fecha_fin_mes(paquete), str) == True:
        error += "mes final no válido\n"
    if isinstance(obtener_fecha_fin_mes(paquete), float) == True:
        error += "mes final no válido\n"
    if isinstance(obtener_fecha_fin_año(paquete), str) == True:
        error += "año final no válido\n"
    if isinstance(obtener_fecha_fin_año(paquete), float) == True:
        error += "año final no válido\n"
    if isinstance(obtener_precio(paquete), str) == True:
        error += "precio invalido\n"
    if obtener_destino(paquete) == "":
        error += "destino invalido\n"
    if obtener_fecha_inicio_mes(paquete) <= 0:
        error += "El mes de la fecha de inicio no es válido\n"
    if obtener_fecha_inicio_mes(paquete) > 12:
        error += "El mes de la fecha de inicio no es válido\n"
    if obtener_fecha_fin_año(paquete) <= 0:
        error += "Año de finalización no válido\n"
#len(s) Retorna el tamaño (el número de elementos) de un objeto
#La función raise se usa para indicar que se ha producido un error o una condición excepciona
    if len(error) > 0:
        raise ValueError(error)
