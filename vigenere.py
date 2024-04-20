import numpy as np


def extiende_clave_ciclicamente(clave_no_extendida, long_msj):
    """
        Crea la clave extendida en base a la longitud del mensaje, cíclicamente.

        Parámetros:
        clave_no_extendida (str): La clave original que se desea extender.
        long_msj (int): Longitud del mensaje para el cual se extenderá la clave.

        Returns:
        str: La clave extendida ciclicamente de tamaño longitud del mensaje.
    """

    stop = True
    extiende_clave = ""

    while stop:
        resto = long_msj - len(extiende_clave)
        if resto == 0:
            stop = False
        elif resto < len(extiende_clave):
            extiende_clave += clave_no_extendida[0:resto]
        else:
            extiende_clave += clave_no_extendida

    return extiende_clave


def extiende_clave_flujo(vector_no_extendido, long_msj):
    """
        Crea la clave extendida con la versión de flujo, en base a la longitud del mensaje.

        Parámetros:
        vector_no_extendido (list): Lista de posiciones que representa la clave original que se desea extender.
        long_msj (int): Longitud del mensaje para el cual se extenderá la clave.

        Returns:
        list: Lista que representa la clave extendida con el método de flujo.
    """
    extiende_vector = [n for n in vector_no_extendido]

    for i in range(len(extiende_vector), long_msj):
        x = 0
        for j, n in enumerate(vector_no_extendido):
            x += n * extiende_vector[(len(extiende_vector) - 1) - j]

        extiende_vector.append(x)

    return extiende_vector


def genera_vector(cadena, alfabeto):
    # Crea el vector númerico en base a las posiciones en el alfabeto de cada uno de los caracteres de la cadena
    lista = list(alfabeto)
    vector = []

    for c in cadena:
        if c in lista:
            vector.append(lista.index(c))

    return vector


def genera_cadena(vector, alfabeto):
    # Genera una cadena en base a las posiciones en el alfabeto de almacenadas en el vector.
    cadena = ""

    for n in vector:
        cadena += alfabeto[n]

    return cadena.replace("  ", "\n")


def calculo_modular_descifrado(vector_msj, vector_clave, alfabeto):
    # Convierte los valores de un vector al módulo correspondiente en base a la longitud del formulario
    # @return vector modular, pero en formato array de la librería numpy. Y realiza la operación para descifrar
    modulo = len(alfabeto)
    array = np.array(np.array(vector_msj) - np.array(vector_clave))
    vector_modular = array % modulo

    return vector_modular


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = input("Introduce el alfabeto: ").replace('"', "")
clave = input("Introduce la clave: ").replace('"', "")
msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")

if input("Introduce el tipo de clave cifrado: ").lower() == "(k_1)":

    clave_extendida = extiende_clave_ciclicamente(clave, len(msj_cifrado))
    vector_descifrado = calculo_modular_descifrado(genera_vector(msj_cifrado, alfabeto), genera_vector(clave_extendida, alfabeto), alfabeto)

    msj_descifrado = genera_cadena(vector_descifrado, alfabeto)
else:
    clave_extendida_vector = extiende_clave_flujo(genera_vector(clave, alfabeto), len(msj_cifrado))
    vector_descifrado = calculo_modular_descifrado(genera_vector(msj_cifrado, alfabeto), clave_extendida_vector, alfabeto)

    msj_descifrado = genera_cadena(vector_descifrado, alfabeto)

print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)

