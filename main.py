from ej1.lanzador1 import main1
from ej2.lanzador2 import main2
from ej3.lanzador3 import main3
from ej4.lanzador4 import main4
from ej5.lanzador5 import main5

if __name__ == '__main__':
    ejercicio = input("Que ejercicio desea hacer: ")
    if ejercicio == 1:
        main1()
    if ejercicio == 2:
        main2()
    if ejercicio == 3:
        main3()
    if ejercicio == 4:
        main4()
    if ejercicio == 5:
        main5()
