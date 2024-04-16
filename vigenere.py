# FLUJO PRINCIPAL DEL PROGRAMA

def extiende_clave(clave, long_msj):
    # Crea la clave extendida en base a la longitud del mensaje

    stop = False
    clave_extendida = ""

    while not stop:
        resto = long_msj - clave_extendida.length

        if clave.length == long_msj:
            stop = True
        elif resto < clave.length:
            clave_extendida += clave[0:resto - 1]
        else:
            clave_extendida += clave

    return clave_extendida




