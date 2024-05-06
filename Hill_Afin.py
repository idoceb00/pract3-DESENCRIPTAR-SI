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


def genera_bloques(vector_msj, tam_bloque):
    bloques = []

    for i in range(1, len(vector_msj) + 1):
        if i % tam_bloque == 0:
            bloques.append(vector_msj[(i-tam_bloque): i])
        else:
            continue

    return bloques


def multiplica_bloques_hill(mensaje_bloques, matriz_descifrado):
    """
        Realiza el producto del bloque asignado con la inversa de la matriz de cifrado.

        Parámetros:
        mensaje_bloques (Array): Array de vectores que contiene los bloques en los que se ha dividido el mensaje.
        matriz_cifrado (Array): Matriz que sirve como clave de cifrado por la cual se multiplicara por su inversa.

        Returns:
        Array: Array con los resultados de los prouctos matriciales.
    """
    productos_bloques = []

    for bloque in mensaje_bloques:
        result = np.array(bloque).dot(matriz_descifrado)
        productos_bloques.append(calculo_modular(result))

    return productos_bloques


def multiplica_bloques_afin(mensaje_bloques, matriz_descifrado, v):
    """
        Realiza el producto del bloque asignado con la inversa de la matriz de cifrado.

        Parámetros:
        mensaje_bloques (Array): Array de vectores que contiene los bloques en los que se ha dividido el mensaje.
        matriz_cifrado (Array): Matriz que sirve como clave de cifrado por la cual se multiplicara por su inversa.

        Returns:
        Array: Array con los resultados de los prouctos matriciales.
    """
    productos_bloques = []

    for bloque in mensaje_bloques:
        result = np.array(bloque).dot(matriz_descifrado) - np.dot(v, matriz_descifrado)
        productos_bloques.append(calculo_modular(result))

    return productos_bloques


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
    vector_modular = []

    for n in vector:
        vector_modular.append(int(n % modulo))

    return vector_modular


def concatena_bloques(conjunto_bloques):
    bloques_concatenados = []
    
    for bloque in conjunto_bloques:
        bloques_concatenados += bloque

    return quitar_padding(bloques_concatenados)


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


def calcular_inversa():
    try:
        global alfabeto
        global clave

        # Calculamos la inversa de la matriz.
        det = int(np.round(np.linalg.det(clave)))

        # Calculamos el inverso multiplicativo del determinante en el campo de los enteros módulo el tamaño del
        # alfabeto.
        det_inv = pow(det, -1, len(alfabeto))

        # Calculamos la matriz adjunta de la matriz.
        adjunta = np.linalg.det(clave) * np.linalg.inv(clave).T

        # Transponemosla matriz adjunta para obtenerla matriz cofactor.
        cofactor = adjunta.T

        # Multiplicar cada elemento de la matriz cofactor por el inverso multiplicativo del determinante,
        # y tomar el módulo del tamaño del alfabeto.
        inversa_modulo = (det_inv * cofactor) % len(alfabeto)

        return np.round(inversa_modulo)

    except np.linalg.LinAlgError:
        # La matriz no tiene inversa
        return None


def quitar_padding(msj_padding):
    global alfabeto
    global clave

    tam_bloque = np.shape(clave)[0]

    # Obtiene el último bloque del mensaje
    ultimo_bloque = msj_padding[-tam_bloque:]

    lon_msj_final = calculo_modulo_decimal(ultimo_bloque, len(alfabeto))

    # Elimina el padding
    msj_limpio = msj_padding[0:lon_msj_final]

    return msj_limpio


def calculo_modulo_decimal(vector, mod):
    num = 0
    for i, valor in enumerate(reversed(vector)):
        num += valor * mod**i
    return num


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = "aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:;-()¿?"
tipo_algoritmo = input("Afín?: ")

if tipo_algoritmo == "si":
    clave = np.array([
        [50,    25, 0,  81, 4],
        [10,    39, 19, 67, 51],
        [34,    49, 63, 9,  56],
        [31,    21, 33, 55, 6],
        [82,    69, 34, 48, 1]])

    v = np.array([24,    11,  34, 70, 78])
    msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")

    vector_cifrado = genera_vector(msj_cifrado)

    bloques_cifrado = genera_bloques(vector_cifrado, 5)

    matriz_inversa = calcular_inversa()
    bloques_descifrado = multiplica_bloques_afin(bloques_cifrado, matriz_inversa,v)
    vector_descifrado = concatena_bloques(bloques_descifrado)

    msj_descifrado = genera_cadena(vector_descifrado)
else:
    clave = np.array([[63,    57, 3,  29, 46, 35],
            [30,    52, 21, 80, 44, 12],
            [37,    23, 53, 60, 16, 56],
            [77,    11, 82, 74, 46, 53],
            [33,    56, 81, 72, 37, 37],
            [12,    11, 68, 55, 22, 19]])

    msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")

    vector_cifrado = genera_vector(msj_cifrado)

    bloques_cifrado = genera_bloques(vector_cifrado, 6)

    matriz_inversa = calcular_inversa()

    bloques_descifrado = multiplica_bloques_hill(bloques_cifrado, matriz_inversa)

    vector_descifrado = concatena_bloques(bloques_descifrado)

    msj_descifrado = genera_cadena(vector_descifrado)

print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)
