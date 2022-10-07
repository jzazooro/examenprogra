class Alumno():

    def __init__(self):
        nombrealumno = input("introduce el nombre del alumno: ")
        notaalumno = input("introduce la nota del alumno: ")
        if 0 <= notaalumno <= 10:
            self.nombre = nombrealumno
            self.nota = notaalumno

    def resultado(self):
        if self.nota >= 5:
            print("Enhorabuena, usted ha aprobado")
        if self.nota < 5:
            print("Lo siento, usted ha suspendido")