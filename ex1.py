class Usuario:
    total = 0
    def __init__(self, nombre, cursos=None):
        self.nombre = nombre
        self.cursos = cursos if cursos is not None else [] # Si no se corregia se asignaria Python a todos
        Usuario.total += 1 #No estaba definido antes de la suma asi que ahora si, creo que esto tambien soluciono el punto de que se sume bien el numero de usuarios
    def agregar_curso(self, curso):
        self.cursos.append(curso) #cursos se define como self.cursos
u1 = Usuario("Ana")
u2 = Usuario("Marc")
u1.agregar_curso("Python")
print(u1.cursos)
print(u2.cursos)
print(Usuario.total)