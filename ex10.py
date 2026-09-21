class Producto:
    def __init__(self, id, nombre, precio_base):
        if not isinstance(precio_base, (int, float)) or precio_base < 0:
            raise ValueError(f"El precio base de '{nombre}' no es válido: {precio_base}")
        self.id = id
        self.nombre = nombre
        self.precio = precio_base

    def __str__(self):
        return f"Producto({self.nombre}, precio={self.precio})"
    def calcular_precio(self):
        return self.precio
    
class ProductoFisico(Producto):
    COSTE_ENVIO = 10
    def __init__(self, id, nombre, precio_base):
        super().__init__(id, nombre, precio_base)

    def __str__(self):
        return f"ProductoFisico({self.nombre}, precio={self.precio}, coste_envio={self.COSTE_ENVIO})"
    def calcular_precio(self):
        return self.precio + self.COSTE_ENVIO

class ProductoDigital(Producto):
    def __init__(self, id, nombre, precio_base, tamaño):
        super().__init__(id, nombre, precio_base)
        if not isinstance(tamaño, (int, float)) or tamaño < 0:
            raise ValueError(f"El tamaño de '{nombre}' no es válido: {tamaño}")
        self.tamaño = tamaño

    def __str__(self):
        return f"ProductoDigital({self.nombre}, precio={self.precio}, tamaño={self.tamaño})"
    def calcular_precio(self):
            return self.precio;

class Suscripcion(Producto):
    def __init__(self, id, nombre, precio_base, meses):
        super().__init__(id, nombre, precio_base)
        if not isinstance(meses, int) or meses <= 0:
            raise ValueError(f"El número de meses de '{nombre}' no es válido: {meses}")
        self.meses = meses

    def __str__(self):
        return f"Suscripcion({self.nombre}, precio={self.precio}, meses={self.meses})"    
    def calcular_precio(self):
        return self.precio * self.meses

class Pedido:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        if any(p.id == producto.id for p in self.productos):
            raise ValueError(f"Ya existe un producto con id {producto.id} en el pedido")
        self.productos.append(producto)

    def eliminar(self, id_producto):
        self.productos = [producto for producto in self.productos if producto.id != id_producto]

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.calcular_precio()
        return total

class ProductoDescuento(Producto):
    def __init__(self, id, nombre, precio_base, porcentaje_descuento):
        super().__init__(id, nombre, precio_base)
        if not isinstance(porcentaje_descuento, (int, float)) or not (0 <= porcentaje_descuento <= 100):
            raise ValueError(
                f"El porcentaje de descuento de '{nombre}' no es válido: {porcentaje_descuento}"
            )
        self.porcentaje_descuento = porcentaje_descuento

    def __str__(self):
        return (
            f"ProductoDescuento({self.nombre}, precio={self.precio}, "
            f"descuento={self.porcentaje_descuento}%)"
        )

    def calcular_precio(self):
        return self.precio * (1 - self.porcentaje_descuento / 100)