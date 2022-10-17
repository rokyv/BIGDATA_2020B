
import pstats
from tabnanny import verbose
import numpy as np
import argparse


def calcular_min_max(lista_numeros, verbose= 1):
    """
    Retorna los valores mínimo y máximo de una lista de numeros
    Args:
        lista_numeros: type list

    """
    min_value = min(lista_numeros)
    max_value = max(lista_numeros)

    if verbose == 1:
        print("Valor Mínimo", min_value)
        print("Valor Máximo", max_value)
    else:
        pass
    return min_value, max_value

def calcular_valores_centrales(lista_numeros, verbose= 1):
    """Calcula la media y la desviación estandar de una lista de números

    Args:
        lista_numeros (list): Lista con valore numéricos
        verbose (bool, optional): para decidir si imprimir mensajes en pantalla.

    Returns:
        tuple: (media, dev_std)
    """


    media = np.mean (lista_numeros)
    dev_std = np.std(lista_numeros)

    if verbose == 1:
        print("Media", media)
        print("Desviación Estandar", dev_std)
    else:
        pass

    return media, dev_std

def calcular_valores(lista_numeros, verbose = 1):
    """Returna una tupla con valoes suma, Mínimo, Máximo, media y desviación estandar de una lista de números 

    Args:
        lista_numeros (list): Lista con valore numéricos
        verbose (bool, optional): para decidir si imprimir mensajes en pantalla.

    Returns:
        tuple: (suma, min, max, media, dev_std)
    """

    suma = np.sum(lista_numeros)
    min_val, max_val = calcular_min_max(lista_numeros, verbose)
    media, dev_std = calcular_valores_centrales(lista_numeros, verbose)

    return suma, min_val, max_val, media, dev_std

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verbose",
        type= int, 
        default=1,
        help="Para imprimir en pantalla información"
    )

    args = parser.parse_args()

    #print('*****',args.verbose, type(args.verbose))
    #v = bool (args.verbose)
    #print('verbose',v,type(v))

    


    lista_valores = [5, 4, 8, 9, 21]
    #calcular_valores(lista_numeros = lista_valores, verbose=True)
    calcular_valores(
        lista_numeros = lista_valores, 
        verbose= args.verbose
    )


if __name__ == "__main__":
    main()
