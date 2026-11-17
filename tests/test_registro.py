import os
import sys
import unittest

# Permite importar los módulos desde la carpeta src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from producto import Producto, registrar_producto


class TestRegistroProducto(unittest.TestCase):

    def setUp(self):
        self.inventario = [
            Producto("LIB-001", "Cien años de soledad", 389.00, 12)
        ]

    def test_registrar_producto_valido(self):
        """CP08 - Registrar un producto nuevo en el inventario."""
        producto = registrar_producto(
            self.inventario, "LIB-006", "El principito", "250", "7"
        )

        self.assertIsInstance(producto, Producto)
        self.assertEqual(producto.codigo, "LIB-006")
        self.assertEqual(producto.nombre, "El principito")
        self.assertEqual(producto.precio, 250.0)
        self.assertEqual(producto.existencia, 7)
        self.assertEqual(len(self.inventario), 2)
        self.assertIs(self.inventario[-1], producto)

    def test_codigo_duplicado(self):
        """CP09 - Rechazar un código que ya existe (sin distinguir mayúsculas)."""
        with self.assertRaises(ValueError):
            registrar_producto(self.inventario, "lib-001", "Otro libro", 100, 1)

        self.assertEqual(len(self.inventario), 1)

    def test_precio_no_numerico(self):
        """CP10 - Rechazar un precio que no es numérico."""
        with self.assertRaises(ValueError):
            registrar_producto(self.inventario, "LIB-007", "Libro", "abc", 1)

        self.assertEqual(len(self.inventario), 1)

    def test_precio_negativo(self):
        """CP11 - Rechazar un precio negativo."""
        with self.assertRaises(ValueError):
            registrar_producto(self.inventario, "LIB-007", "Libro", -10, 1)

        self.assertEqual(len(self.inventario), 1)

    def test_existencia_negativa(self):
        """CP12 - Rechazar una existencia negativa."""
        with self.assertRaises(ValueError):
            registrar_producto(self.inventario, "LIB-007", "Libro", 100, -1)

        self.assertEqual(len(self.inventario), 1)

    def test_codigo_vacio(self):
        """CP13 - Rechazar un código vacío."""
        with self.assertRaises(ValueError):
            registrar_producto(self.inventario, "  ", "Libro", 100, 1)

        self.assertEqual(len(self.inventario), 1)

    def test_nombre_vacio(self):
        """CP14 - Rechazar un nombre vacío."""
        with self.assertRaises(ValueError):
            registrar_producto(self.inventario, "LIB-007", "  ", 100, 1)

        self.assertEqual(len(self.inventario), 1)


if __name__ == "__main__":
    unittest.main()
