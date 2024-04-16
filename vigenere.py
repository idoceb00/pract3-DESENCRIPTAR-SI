import numpy as np


def extiende_clave_ciclicamente(clave_num, long_msj):
    # Crea la clave extendida en base a la longitud del mensaje, ciclicamenete

    stop = False
    clave_extendida = ""

    while not stop:
        resto = long_msj - clave_extendida.length

        if clave_num.length == long_msj:
            stop = True
        elif resto < clave_num.length:
            clave_extendida += clave_num[0:resto - 1]
        else:
            clave_extendida += clave_num

    return clave_extendida


def genera_vector(cadena, alfabeto):
    # Crea el vector númerico en base a las posiciones en el alfabeto de de cada uno de los caracteres de la cadena
    lista = list(alfabeto)
    vector = []

    for c in cadena:
        if c in lista:
            vector.append(lista.index(c))

    return vector


# FLUJO PRINCIPAL DEL PROGRAMA
genera_vector("abecemon", "abcdefghijklmno")


