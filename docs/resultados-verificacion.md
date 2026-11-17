# Resultados de las verificaciones

## Entorno

| Elemento | Valor |
| --- | --- |
| Sistema operativo | Linux x86_64 |
| Python | 3.13.16 |
| UnZip | 6.00 |
| OpenSSH | 10.6p2 |
| Fecha de verificación | 2026-11-17 |

## v1.0.0

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| El paquete se descarga desde GitHub Releases | OK | `evidencias/01-version-descargada.txt` |
| El paquete se extrae correctamente | OK | `evidencias/03-despliegue-manual-v1.0.0.txt` |
| La sintaxis compila (`compileall`) | OK | `evidencias/03-despliegue-manual-v1.0.0.txt` |
| El programa inicia correctamente | OK | `evidencias/03-despliegue-manual-v1.0.0.txt` |
| Se consultan productos registrados | OK | `evidencias/04-verificacion-v1.0.0.txt` |
| Se muestran correctamente los datos | OK | `evidencias/04-verificacion-v1.0.0.txt` |
| Se presenta algún error de ejecución | No | `evidencias/04-verificacion-v1.0.0.txt` |
| Se pueden registrar productos nuevos | No en v1.0.0; sí en v1.1.0 | `evidencias/05-despliegue-manual-v1.1.0.txt` |

Resultado de la prueba por código:

```text
Código:      LIB-002
Nombre:      Pedro Páramo
Precio:      $199.50 MXN
Existencia:  8 unidades
```

Resultado de la prueba por nombre (`quijote`): se encontró
`Don Quijote de la Mancha` con los datos completos.

## v1.1.0

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| El código compila y las 14 pruebas pasan | OK | `python3 -m unittest discover -s tests -v` |
| Se registra un producto nuevo | OK | `evidencias/05-despliegue-manual-v1.1.0.txt` |
| El producto registrado se consulta por código | OK | `evidencias/05-despliegue-manual-v1.1.0.txt` |
| Se rechazan códigos duplicados y datos inválidos | OK | `tests/test_registro.py` |

Producto registrado durante la verificación:

```text
Código:      LIB-006
Nombre:      El principito
Precio:      $250.00 MXN
Existencia:  7 unidades
```

## Rollback

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Se detecta el fallo simulado (`ModuleNotFoundError`) | OK | `evidencias/06-rollback.txt` |
| Se recupera v1.0.0 desde el paquete conservado | OK | `evidencias/06-rollback.txt` |
| La versión recuperada vuelve a funcionar | OK | `evidencias/06-rollback.txt` |

## Conclusión

El despliegue manual de v1.0.0 y v1.1.0 funciona correctamente. La versión
v1.1.0 incorpora el registro de productos y conserva las funciones de consulta
y búsqueda. El procedimiento de rollback permitió recuperar v1.0.0 y verificar
su funcionamiento.
