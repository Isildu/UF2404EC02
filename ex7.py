class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{type(self).__name__}({self.nombre}, {self.edad})"


class Alumno(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)   # reutiliza el __init__ de Persona
        self.matricula = matricula
    def __str__(self):
        return f"Alumno({self.nombre}, matrícula={self.matricula})"
    def __eq__(self, other):
        # Dos alumnos son el mismo si tienen la misma matrícula
        return isinstance(other, Alumno) and self.matricula == other.matricula

    def __hash__(self):
        # Necesario porque definimos __eq__, para poder usar sets/dicts
        return hash(self.matricula)

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
    def __str__(self):
        return f"Profesor({self.nombre}, especialidad={self.especialidad})"

class Curso:
    def __init__(self, nombre, profesor, capacidadMax):
        if not isinstance(profesor, Profesor):
            raise TypeError("El profesor del curso debe ser un Profesor.")
        if capacidadMax <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que 0.")
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []
        self.capacidadMax = capacidadMax
    def matricular(self, alumno):
        if not isinstance(alumno, Alumno):
            raise TypeError("Solo se pueden matricular objetos de tipo Alumno.")
        if alumno in self.alumnos:
            raise ValueError(f"{alumno.nombre} ya está matriculado en {self.nombre}.")
        if len(self.alumnos) >= self.capacidadMax:
            raise ValueError(
                f"No hay plazas disponibles en {self.nombre} "
                f"({len(self.alumnos)}/{self.capacidadMax})."
            )
        self.alumnos.append(alumno)
    def desmatricular(self, alumno):
        if not isinstance(alumno, Alumno):
            raise TypeError("Solo se pueden desmatricular objetos de tipo Alumno.")
        if alumno not in self.alumnos:
            raise ValueError(f"{alumno.nombre} no está matriculado en {self.nombre}.")
        self.alumnos.remove(alumno)

    def cambiar_profesor(self, profesor):
        if not isinstance(profesor, Profesor):
            raise TypeError("El curso solo puede ser impartido por un Profesor.")
        self.profesor = profesor
    def __str__(self):
        lineas = [
            f"Curso: {self.nombre}",
            f"  Profesor: {self.profesor}",
            f"  Capacidad: {len(self.alumnos)}/{self.capacidadMax}",
            "  Alumnos:",
        ]
        if not self.alumnos:
            lineas.append("    (sin alumnos matriculados)")
        else:
            for a in self.alumnos:
                lineas.append(f"    - {a}")
        return "\n".join(lineas)
# Personas
prof_marc  = Profesor("Marc", 40, "Python")
prof_laura = Profesor("Laura", 35, "Java")

# Alumnos
ana  = Alumno("Ana", 20, "A001")
luis = Alumno("Luis", 22, "A002")
eva  = Alumno("Eva", 21, "A003")

# Curso con capacidad 2
python = Curso("Python Básico", prof_marc, capacidadMax=2)

python.matricular(ana)
python.matricular(luis)

print(python)
print("-" * 40)

# Cambiar de profesor
python.cambiar_profesor(prof_laura)

# Desmatricular
python.desmatricular(luis)

# Matricular a otro
python.matricular(eva)

print(python)