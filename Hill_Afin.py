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
def multiplica_bloques(mensaje_bloques, matriz_cifrado):
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
        result = np.array(bloque).dot(np.linalg.inv(matriz_cifrado))
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


# CONCATENAR BLOQUES
def concatena_bloques(conjunto_bloques):
    bloques_concatenados = []
    
    for bloque in conjunto_bloques:
        bloques_concatenados += bloque

    return bloques_concatenados


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

    print(vector)
    for n in vector:
        cadena += alfabeto[n]

    return cadena.replace("  ", "\n")


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = input("Introduce el alfabeto: ").replace('"', "")
clave = [[63,    57, 3,  29, 46, 35],
         [30,    52, 21, 80, 44, 12],
         [37,    23, 53, 60, 16, 56],
         [77,    11, 82, 74, 46, 53],
         [33,    56, 81, 72, 37, 37],
         [12,    11, 68, 55, 22, 19]]

msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")

vector_cifrado = genera_vector(msj_cifrado)

bloques_cifrado = genera_bloques(vector_cifrado, 6)

bloques_descifrado = multiplica_bloques(bloques_cifrado, clave)

vector_descifrado = concatena_bloques(bloques_descifrado)

msj_descifrado = genera_cadena(vector_descifrado)

print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)
