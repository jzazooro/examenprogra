class Alumno():
    lista=[]
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print(nombre)
        print(nota)
        for nota in Alumno:
            if nota < 5:
                print("Lo siento, usted ha suspendido")
            if nota >= 5:
                print("Enhorabuena, usted ha aprobado")
def crear(nombre, nota):
        alumno = Alumno(nombre, nota)
        for alumno in Alumno:
            lista=lista.append(alumno)
crear(jose, 5)

