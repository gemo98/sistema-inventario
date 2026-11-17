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