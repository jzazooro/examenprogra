from ej1.lanzador1 import main1
from ej2.lanzador2 import main2
from ej4.lanzador4 import main4

if __name__ == '__main__':
    ejercicio = input("Que ejercicio desea hacer: ")
    if ejercicio == 1:
        main1()
    if ejercicio == 2:
        main2()
    if ejercicio == 4:
        main4()
