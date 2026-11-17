import io
import os
import sys
import unittest
from contextlib import redirect_stdout

# Permite importar producto.py desde la carpeta src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from producto import Producto


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.p1 = Producto("P001", "Teclado", 350, 10)
        self.p2 = Producto("P002", "Mouse", 180, 5)

    def capturar_salida(self, producto):
        """Ejecuta mostrar_informacion() y devuelve lo que imprimió."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            producto.mostrar_informacion()
        return buffer.getvalue()

    def test_cp01_crear_producto(self):
        """CP01 - Crear producto"""
        self.assertIsInstance(self.p1, Producto)
        self.assertEqual(self.p1.codigo, "P001")
        self.assertEqual(self.p1.nombre, "Teclado")
        self.assertEqual(self.p1.precio, 350)
        self.assertEqual(self.p1.existencia, 10)

    def test_cp02_mostrar_codigo(self):
        """CP02 - Mostrar código"""
        self.assertEqual(self.p1.codigo, "P001")
        self.assertIn("P001", self.capturar_salida(self.p1))

    def test_cp03_mostrar_nombre(self):
        """CP03 - Mostrar nombre"""
        self.assertEqual(self.p1.nombre, "Teclado")
        self.assertIn("Teclado", self.capturar_salida(self.p1))

    def test_cp04_mostrar_precio(self):
        """CP04 - Mostrar precio"""
        self.assertEqual(self.p1.precio, 350)
        self.assertIn("350.00", self.capturar_salida(self.p1))

    def test_cp05_mostrar_existencia(self):
        """CP05 - Mostrar existencia"""
        self.assertEqual(self.p1.existencia, 10)
        self.assertIn("10 unidades", self.capturar_salida(self.p1))

    def test_cp06_mostrar_informacion_completa(self):
        """CP06 - Mostrar información completa"""
        salida = self.capturar_salida(self.p1)
        for dato in ("P001", "Teclado", "350.00", "10 unidades"):
            self.assertIn(dato, salida)

    def test_cp07_crear_segundo_producto(self):
        """CP07 - Crear segundo producto"""
        self.assertEqual(self.p2.codigo, "P002")
        self.assertEqual(self.p2.nombre, "Mouse")
        self.assertEqual(self.p2.precio, 180)
        self.assertEqual(self.p2.existencia, 5)
        # No se confunde con el primero
        self.assertEqual(self.p1.codigo, "P001")
        self.assertEqual(self.p1.nombre, "Teclado")


if __name__ == "__main__":
    unittest.main()