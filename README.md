# sistema-inventario

Sistema de consola para la gestión del inventario de una librería. Permite
consultar los libros registrados, buscar por código o por nombre y registrar
productos nuevos.

## Requisitos

- Python 3.12 o superior (probado con Python 3.13).

## Ejecución

```bash
python3 src/busqueda.py
```

El menú permite:

1. Buscar por código.
2. Buscar por nombre.
3. Registrar un producto.
4. Salir.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Despliegue

El procedimiento de despliegue, la automatización con GitHub Actions y las
evidencias se encuentran en [`docs/despliegue.md`](docs/despliegue.md). La guía
para ejecutar el workflow y descargar las evidencias está en
[`docs/como-ejecutar-el-workflow.md`](docs/como-ejecutar-el-workflow.md).
