import numpy as np


def extiende_clave_ciclicamente(clave_no_extendida, long_msj):
    # Crea la clave extendida en base a la longitud del mensaje, ciclicamenete

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
    extiende_vector = vector_no_extendido

    for i in range(len(extiende_vector) - 1, long_msj):
        x = 0
        for n in vector_no_extendido:
            pass


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


clave_extendida = extiende_clave_ciclicamente(clave, len(msj_cifrado))
vector_descifrado = calculo_modular_descifrado(genera_vector(msj_cifrado, alfabeto), genera_vector(clave_extendida, alfabeto), alfabeto)

msj_descifrado = genera_cadena(vector_descifrado, alfabeto)

print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)
