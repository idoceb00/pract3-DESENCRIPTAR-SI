import numpy as np


def extiende_clave_ciclicamente(clave_no_extendida, long_msj):
    """
        Crea la clave extendida con base en la longitud del mensaje, cíclicamente.

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
        Crea la clave extendida con la versión de flujo, con base en la longitud del mensaje.

        Parámetros:
        vector_no_extendido (list): Lista de posiciones que representa la clave original que se desea extender.
        long_msj (int): Longitud del mensaje para el cual se extenderá la clave.

        Returns:
        list: Lista que representa la clave extendida con el método de flujo.
    """
    # Si se iguala al vector, se almacenaría dinámicamente, así son dos variables distintas
    extiende_vector = [n for n in vector_no_extendido]

    for i in range(len(extiende_vector), long_msj):
        x = 0
        for j, n in enumerate(vector_no_extendido):
            x += n * extiende_vector[(len(extiende_vector) - 1) - j]

        extiende_vector.append(x)

    return extiende_vector


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


def calculo_modular_descifrado(vector_msj, vector_clave):
    """
        Convierte los valores de un vector al módulo correspondiente en base a la longitud del formulario.

        Parámetros:
        vector_msj (list): Lista que representa el vector del mensaje cifrado.
        vector_clave (list): Lista que representa el vector de la clave utilizada para cifrar.
        alfabeto (str): Cadena que representa el alfabeto utilizado.

        Returns:
        np.array: Array de numpy que representa el vector modular resultante del descifrado.
    """
    global alfabeto
    modulo = len(alfabeto)
    array = np.array(np.array(vector_msj) - np.array(vector_clave))
    vector_modular = array % modulo

    return vector_modular


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = input("Introduce el alfabeto: ").replace('"', "")
clave = input("Introduce la clave: ").replace('"', "")
msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")
msj_descifrado = ""

while True:
    try:
        tipo_clave = int(input("Introduce el tipo de clave cifrado: "))

        if tipo_clave == 1:

            clave_extendida = extiende_clave_ciclicamente(clave, len(msj_cifrado))
            vector_descifrado = calculo_modular_descifrado(genera_vector(msj_cifrado), genera_vector(clave_extendida))

            msj_descifrado = genera_cadena(vector_descifrado)
            break
        elif tipo_clave == 2:
            clave_extendida_vector = extiende_clave_flujo(genera_vector(clave), len(msj_cifrado))
            vector_descifrado = calculo_modular_descifrado(genera_vector(msj_cifrado), clave_extendida_vector)

            msj_descifrado = genera_cadena(vector_descifrado)
            break
        else:
            print("ERROR. El tipo de clave debe ser '1' o '2'")
            continue
    except ValueError:
        print("ERROR. Introduce un número ('1' o '2')")
        continue

print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)
