class Producto:
    """Representa un libro a la venta en una librería."""

    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo          # Código del producto
        self.nombre = nombre          # Nombre del producto (título del libro)
        self.precio = precio          # Precio en pesos mexicanos
        self.existencia = existencia  # Unidades en inventario

    def mostrar_informacion(self):
        """Muestra en pantalla la información del producto."""
        print("=" * 45)
        print(f"Código:      {self.codigo}")
        print(f"Nombre:      {self.nombre}")
        print(f"Precio:      ${self.precio:,.2f} MXN")
        print(f"Existencia:  {self.existencia} unidades")
        print("=" * 45)


def registrar_producto(inventario, codigo, nombre, precio, existencia):
    """Crea un producto, lo agrega al inventario y lo devuelve.

    Lanza ValueError cuando los datos no son válidos o el código ya existe.
    """
    codigo = "" if codigo is None else str(codigo).strip()
    nombre = "" if nombre is None else str(nombre).strip()

    if not codigo:
        raise ValueError("El código no puede estar vacío.")
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    for producto in inventario:
        if producto.codigo.upper() == codigo.upper():
            raise ValueError(f"Ya existe un producto con el código {codigo}.")

    try:
        precio = float(precio)
        existencia = int(existencia)
    except (TypeError, ValueError):
        raise ValueError(
            "El precio debe ser numérico y la existencia un número entero."
        )

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if existencia < 0:
        raise ValueError("La existencia no puede ser negativa.")

    producto = Producto(codigo, nombre, precio, existencia)
    inventario.append(producto)
    return producto


libros = [
    Producto("LIB-001", "Cien años de soledad", 389.00, 12),
    Producto("LIB-002", "Pedro Páramo", 199.50, 8),
    Producto("LIB-003", "Don Quijote de la Mancha", 459.90, 5),
    Producto("LIB-004", "La casa de los espíritus", 329.00, 0),
    Producto("LIB-005", "Rayuela", 299.00, 3),
]


def main():
    print("\n  INVENTARIO DE LA LIBRERÍA\n")
    for libro in libros:
        libro.mostrar_informacion()


if __name__ == "__main__":
    main()