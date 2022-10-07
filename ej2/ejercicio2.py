class Alumnodos():

    def __init__(self):
        nombrealumno = input("introduce el nombre del alumno: ")
        notaalumno = input("introduce la nota del alumno: ")
        if 0 <= notaalumno <= 10:
            self.nombre = nombrealumno
            self.nota = notaalumno

    def __str__(self):
        return(self.nombre, self.nota)

    def resultadonuevo(self):
        if self.nota >= 5:
            print("Lo siento, el alumno ha suspendido")
        if self.nota < 5:
            print("El alumno ha aprobado")