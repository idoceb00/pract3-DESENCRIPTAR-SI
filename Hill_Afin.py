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

# SEPARAR EN BLOQUES EL MENSAJE

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
    productos_bloques = np.array([])
    
    for bloque in mensaje_bloques:
        result = np.array(bloque).dot(np.linalg.inv(matriz_cifrado))
        productos_bloques = np.append(productos_bloques, result, axis=0)

    return productos_bloques

# CALCULO MODULAR

# CONCATENAR BLOQUES
def concatena_bloques(conjunto_bloques):
    bloques_concatenados = []
    
    for bloque in conjunto_bloques:
        bloques_concatenados = np.append(bloques_concatenados, bloque)

    return bloques_concatenados


# GENERAR EL MENSAJE


# FLUJO PRINCIPAL DEL PROGRAMA
alfabeto = input("Introduce el alfabeto: ").replace('"', "")
clave = input("Introduce la clave: ").replace('"', "")
msj_cifrado = input("Introduce el mensaje cifrado: ").replace('"', "")
msj_descifrado = ""


print("\nMENSAJE DESCIFRADO: \n")
print(msj_descifrado)