import numpy as np


def extiende_clave_ciclicamente(clave_num, long_msj):
    # Crea la clave extendida en base a la longitud del mensaje, ciclicamenete

    stop = False
    clave_extendida = ""

    while not stop:
        resto = long_msj - len(clave_extendida)

        if clave_num.length == long_msj:
            stop = True
        elif resto < len(clave_num):
            clave_extendida += clave_num[0:resto - 1]
        else:
            clave_extendida += clave_num

    return clave_extendida


def genera_vector(cadena, alfabeto):
    # Crea el vector númerico en base a las posiciones en el alfabeto de cada uno de los caracteres de la cadena
    lista = list(alfabeto)
    vector = []

    for c in cadena:
        if c in lista:
            vector.append(lista.index(c))

    return calculo_modular(vector, alfabeto)


def genera_cadena(vector, alfabeto):
    # Genera una cadena en base a las posiciones en el alfabeto de almacenadas en el vector.
    cadena = ""

    for n in vector:
        cadena += alfabeto[n]

    return cadena


def calculo_modular(vector_decimal, alfabeto):
    # Convierte los valores de un vector al módulo correspondiente en base a la longitud del formulario
    # @return vector modular, pero en formato array de la librería numpy
    modulo = len(alfabeto)
    array = np.array(vector_decimal)
    vector_modular = array % modulo

    return vector_modular


# Función que suma las los vectores


# FLUJO PRINCIPAL DEL PROGRAMA
# genera_vector("abecemon", "abcdefghijklmno")
genera_cadena([1, 2, 3, 4, 5, 6], "abcdefghijklmno")
calculo_modular([30, 60, 125], "abcdefghijklmno")
