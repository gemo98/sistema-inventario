import unicodedata
from producto import libros, registrar_producto


def normalizar(texto):
    """Convierte a minúsculas y quita acentos para comparar sin errores."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def buscar_por_codigo(inventario, codigo):
    """Regresa el producto con ese código exacto, o None si no existe."""
    for producto in inventario:
        if producto.codigo.upper() == codigo.strip().upper():
            return producto
    return None


def buscar_por_nombre(inventario, texto):
    """Regresa la lista de productos cuyo nombre contiene el texto."""
    buscado = normalizar(texto.strip())
    return [p for p in inventario if buscado in normalizar(p.nombre)]


def main():
    while True:
        print("\n--- BÚSQUEDA DE LIBROS ---")
        print("1. Buscar por código")
        print("2. Buscar por nombre")
        print("3. Registrar producto")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            codigo = input("Código (ej. LIB-002): ")
            producto = buscar_por_codigo(libros, codigo)
            if producto:
                producto.mostrar_informacion()
            else:
                print("No se encontró ningún libro con ese código.")

        elif opcion == "2":
            texto = input("Nombre o parte del nombre: ")
            resultados = buscar_por_nombre(libros, texto)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} resultado(s):")
                for producto in resultados:
                    producto.mostrar_informacion()
            else:
                print("No se encontró ningún libro con ese nombre.")

        elif opcion == "3":
            print("\n--- REGISTRAR PRODUCTO ---")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            existencia = input("Existencia: ")
            try:
                producto = registrar_producto(
                    libros, codigo, nombre, precio, existencia
                )
            except ValueError as error:
                print(f"No se pudo registrar: {error}")
            else:
                print("\nProducto registrado correctamente:")
                producto.mostrar_informacion()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
