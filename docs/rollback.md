# Procedimiento de recuperación (rollback)

## Objetivo

Regresar a la última versión estable (v1.0.0) cuando una versión recién
desplegada no funciona correctamente.

## Requisitos

- Conservar el paquete `sistema-inventario-v1.0.0.zip` descargado de GitHub
  Releases.
- Tener acceso al servidor de destino (o al runner, en la simulación).
- Conocer el directorio de despliegue: `~/sistema-inventario`.

## Procedimiento manual

1. Identificar el fallo y detener el uso de la versión afectada.
2. Verificar que el paquete estable esté disponible:

   ```bash
   ls -lh ~/sistema-inventario/sistema-inventario-v1.0.0.zip
   sha256sum ~/sistema-inventario/sistema-inventario-v1.0.0.zip
   ```

3. Extraer la versión estable en un directorio limpio:

   ```bash
   cd ~/sistema-inventario
   rm -rf version-rollback
   mkdir -p version-rollback
   unzip -o sistema-inventario-v1.0.0.zip -d version-rollback
   ```

4. Ejecutar y verificar:

   ```bash
   cd ~/sistema-inventario/version-rollback
   printf '1\nLIB-002\n3\n' | python3 src/busqueda.py
   ```

   Debe mostrarse `Pedro Páramo`.

5. Registrar el incidente: versión afectada, síntoma, hora, versión restaurada
   y resultado de la verificación.

## Procedimiento automatizado

El workflow `.github/workflows/deploy.yml` incluye el parámetro
`simulate_failure`. Cuando se ejecuta con `version = v1.1.0` y
`simulate_failure = true`:

1. Despliega v1.1.0.
2. Inserta una dependencia inexistente (`import modulo_inexistente`) para
   simular un fallo.
3. Ejecuta el sistema y registra el error.
4. Descarga v1.0.0 desde GitHub Releases.
5. La transfiere por `scp` y la extrae en `version-rollback`.
6. Ejecuta y verifica v1.0.0.
7. Publica `salida-ejecucion.txt`, `salida-rollback.txt` y los listados como
   artefactos.

## Evidencia local de la simulación

```text
Traceback (most recent call last):
  File ".../src/busqueda.py", line 1, in <module>
    import modulo_inexistente
ModuleNotFoundError: No module named 'modulo_inexistente'
Código de salida: 1
```

Después de restaurar v1.0.0:

```text
Código:      LIB-002
Nombre:      Pedro Páramo
Precio:      $199.50 MXN
Existencia:  8 unidades
RESULTADO: ROLLBACK OK - v1.0.0 restaurada y funcionando.
```

Evidencia completa: [`evidencias/06-rollback.txt`](evidencias/06-rollback.txt).
