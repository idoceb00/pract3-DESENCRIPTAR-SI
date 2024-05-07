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
    """
    Genera una lista de bloques a partir de un mensaje, basándose en un tamaño de bloque especificado.

    Esta función divide un vector de mensaje en bloques de un tamaño dado. Recorre el vector y agrupa
    los elementos en sub-listas (bloques) según el tamaño de bloque proporcionado. Solo se incluyen
    en la lista de bloques aquellos que tienen la longitud exacta del tamaño de bloque especificado.

    Args:
        vector_msj (list): El mensaje original representado como una lista de elementos.
        tam_bloque (int): El número de elementos que debe tener cada bloque.

    Returns:
        list: Una lista de bloques, donde cada bloque es una sub-lista del mensaje original.

    Raises:
        ValueError: Si 'tam_bloque' no es un entero positivo.
        TypeError: Si 'vector_msj' no es una lista.
    """
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
    """
    Concatena una lista de bloques en un solo mensaje.

    Esta función toma una lista de bloques (cada bloque representado como una lista de elementos)
    y los concatena en un solo mensaje. Luego, se llama a la función 'quitar_padding' para eliminar
    cualquier padding que pueda estar presente en el mensaje concatenado.

    Args:
        conjunto_bloques (list): Una lista de bloques, donde cada bloque es una lista de elementos.

    Returns:
        np.array: El mensaje concatenado sin padding.

    Raises:
        TypeError: Si 'conjunto_bloques' no es una lista.
    """
    bloques_concatenados = []
    
    for bloque in conjunto_bloques:
        bloques_concatenados += bloque

    return elimina_padding(bloques_concatenados)


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
    """
    Calcula la inversa modular de una matriz 'clave' utilizando el tamaño del 'alfabeto' como módulo.

    La función primero intenta calcular el determinante de la matriz 'clave' y su inverso multiplicativo
    en el módulo de la longitud del 'alfabeto'. Luego, calcula la matriz adjunta y la multiplica por el
    inverso multiplicativo para obtener la inversa modular. Finalmente, devuelve la inversa modular redondeada.

    Returns:
        np.array: Una matriz que es la inversa modular de 'clave' si existe, de lo contrario None.

    Raises:
        np.linalg.LinAlgError: Si la matriz 'clave' no es invertible.
    """

    try:
        global alfabeto
        global clave

        inv = int(np.round(np.linalg.det(clave)))
        inv_mult = pow(inv, -1, len(alfabeto))

        matriz_adj = (np.linalg.det(clave) * np.linalg.inv(clave).T).T
        inversa_modulo = (inv_mult * matriz_adj) % len(alfabeto)

        return np.round(inversa_modulo)

    except np.linalg.LinAlgError:
        return None


def elimina_padding(msj_padding):
    """
    Elimina el padding de un mensaje cifrado basado en el tamaño del bloque de la 'clave'.

    Esta función asume que el mensaje tiene un padding que se añadió durante el proceso de cifrado
    y que el último bloque del mensaje contiene la longitud del mensaje original antes del padding.
    La función calcula el tamaño del bloque a partir de la forma de la matriz 'clave' y utiliza
    este tamaño para identificar y eliminar el padding del mensaje.

    Args:
        msj_padding (np.array): El mensaje cifrado con padding.

    Returns:
        np.array: El mensaje original sin padding.

    Raises:
        ValueError: Si 'msj_padding' no es del tipo o forma esperada.
    """
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
    """
    Calcula el valor decimal de un número representado en un sistema modular.

    Esta función toma un vector que representa un número en un sistema de base 'mod' y lo convierte
    a su equivalente decimal. El vector se recorre en orden inverso, multiplicando cada dígito por
    la base elevada a la potencia correspondiente a su posición, sumando estos valores para obtener
    el número decimal final.

    Args:
        vector (list): Una lista de enteros que representa el número en la base 'mod'.
        mod (int): La base del sistema modular.

    Returns:
        int: El valor decimal del número representado en el sistema modular.

    Raises:
        TypeError: Si 'vector' no es una lista o 'mod' no es un entero.
    """
    num = 0
    for i, valor in enumerate(reversed(vector)):
        num += valor * mod**i
    return num


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = "-()TUÚVWXYZAÁBCDEÉFGHIÍJKLMNÑOÓPópqrstuvwxyzaábcdeéfghiíjklmnñoQRS ,.:;"
tipo_algoritmo = input("Afín?: ")

if tipo_algoritmo == "si":
    clave = np.array([
        [63,57, 3,  29 ],
        [30,52, 21, 30 ],
        [37,23, 53, 60 ],
        [67,11, 22, 69 ]])

    v = np.array([24,11, 1, 34 ])
    msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")

    vector_cifrado = genera_vector(msj_cifrado)

    bloques_cifrado = genera_bloques(vector_cifrado, 4)

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
