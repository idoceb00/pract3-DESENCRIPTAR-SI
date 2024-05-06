import numpy as np

def genera_vector(cadena):
    """
        Crea el vector númerico con base en las posiciones en el alfabeto de cada uno de los caracteres de la cadena.

        Parámetros:
        cadena (str): Cadena de caracteres que se desea convertir en un vector numérico.
        alfabeto (str): Cadena que representa el alfabeto sobre el cual se mapearán los caracteres.

        Returns:
        list: Lista que representa el vector numérico generado.
    """
    global alfabeto
    lista = list(alfabeto)
    vector = []

    for c in cadena:
        if c in lista:
            vector.append(lista.index(c))

    return vector

# Padding


def genera_bloques(vector_msj, tam_bloque):
    # SEPARAR EN BLOQUES EL MENSAJE
    bloques = []

    for i in range(1, len(vector_msj) + 1):
        if i % tam_bloque == 0:
            bloques.append(vector_msj[(i-tam_bloque): i])
        else:
            continue

    return bloques

# MULTIPLICAR CADA BLOQUE POR LA MATRIZ INVERSA USANDO EL MÉTODO DE HILL


def calculo_modular(vector):
    """
        Convierte los valores de un vector al módulo correspondiente en base a la longitud del alfabeto.

        Parámetros:
        vector(list): vector número al que aplicarle las reglas del módulo

        Returns:
        np.array: Array de numpy que representa el vector modular resultante del descifrado.
    """
    global alfabeto
    modulo = len(alfabeto)
    vector_modular = vector % modulo

    return vector_modular


# CONCATENAR BLOQUES

# GENERAR EL MENSAJE
def genera_cadena(vector):
    """
        Genera una cadena con base en las posiciones en el alfabeto almacenadas en el vector.

        Parámetros:
        vector (list): Lista que representa un vector numérico.
        alfabeto (str): Cadena que representa el alfabeto a partir del cual se generará la cadena.

        Returns:
        str: Cadena de caracteres generada a partir del vector y el alfabeto proporcionados.
    """
    global alfabeto
    cadena = ""

    for n in vector:
        cadena += alfabeto[n]

    return cadena.replace("  ", "\n")


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = input("Introduce el alfabeto: ").replace('"', "")
clave = input("Introduce la clave: ").replace('"', "")
msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")
msj_descifrado = ""


print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)
