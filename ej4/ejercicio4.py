from this import d


def division(a, b):
    try: 
        numero = a/b
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
    else:
        print(numero)

def conlista(lista):
    try:
        lista=[10]
    except IndexError:
        print("la lista no tiene tantos elementos")
    else:
        print(lista)

def ejpaises(paises):
    try:
        paises["alemania"]
    except KeyError:
        print("ese elemento no esta en la lista")
    else: 
        print(paises)
def ejtipos():
    try:
        resultado="2"+10
    except TypeError:
        print("no piuedes operar este tipo de variables")
    else:
        print(resultado)