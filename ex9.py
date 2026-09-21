from datetime import date
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo = None, fecha_devolucion = None):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo or date.today()
        self.fecha_devolucion = fecha_devolucion
    @property
    def activo(self):
        return self.fecha_devolucion is None

    def __repr__(self):
        return (f"Prestamo({self.usuario.nombre} -> "
                f"'{self.libro.titulo}', activo={self.activo})")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def _buscar_libro(self, isbn):
        return next((l for l in self.libros if l.isbn == isbn), None)

    def _buscar_usuario(self, id_usuario):
        return next((u for u in self.usuarios if u.id_usuario == id_usuario), None)


    def agregar_libro(self, libro):
        if self._buscar_libro(libro.isbn):
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        if self._buscar_usuario(usuario.id_usuario):
            raise ValueError(f"Ya existe un usuario con id {usuario.id_usuario}")
        self.usuarios.append(usuario)

    def prestar(self, isbn, id_usuario):
        libro = self._buscar_libro(isbn)
        usuario = self._buscar_usuario(id_usuario)
        if not libro:
            return f"No existe un libro con ISBN {isbn}"
        if not usuario:
            return f"No existe un usuario con id {id_usuario}"
        if not libro.disponible:
            return f"El libro '{libro.titulo}' ya está prestado"
        activos = [p for p in self.prestamos
                   if p.usuario is usuario and p.activo]
        if len(activos) >= 3:
            return f"El usuario {usuario.nombre} ya tiene 3 libros prestados"

        prestamo = Prestamo(usuario, libro)   # objetos, no strings
        libro.disponible = False
        self.prestamos.append(prestamo)
        return prestamo
    
    def devolver(self, isbn):
        prestamo = next((p for p in self.prestamos if p.libro.isbn == isbn and p.activo), None)
        if not prestamo:
            return None, f"No hay un préstamo activo para el ISBN {isbn}"

        prestamo.fecha_devolucion = date.today()
        prestamo.libro.disponible = True
        return prestamo
    def prestamos_activos(self):
        return [p for p in self.prestamos if p.activo]

b = Biblioteca()

b.agregar_libro(Libro("Cien años de soledad", "G. García Márquez", "978-0307474728"))
b.agregar_libro(Libro("1984", "George Orwell", "978-0451524935"))

b.registrar_usuario(Usuario("Ana", 1))
b.registrar_usuario(Usuario("Luis", 2))

b.prestar("978-0307474728", 1)   # Ana toma Cien años de soledad
b.prestar("978-0451524935", 1)   # Ana toma 1984

print(b.prestamos_activos())
# [Prestamo(Ana -> 'Cien años de soledad', activo=True),
#  Prestamo(Ana -> '1984', activo=True)]

b.devolver("978-0451524935")
print(b.prestamos_activos())
# [Prestamo(Ana -> 'Cien años de soledad', activo=True)]

# Intentar prestar un libro ya prestado → error controlado
b.prestar("978-0307474728", 2)