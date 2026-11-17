# Cómo ejecutar y evidenciar el workflow

## 1. Subir los cambios y el tag

Desde la raíz del repositorio:

```bash
git push origin main
git push origin v1.1.0
```

El primer comando dispara automáticamente el workflow **Despliegue del Sistema
de Inventario** para v1.0.0, porque el archivo `deploy.yml` cambió. El segundo
dispara **Liberación del Sistema de Inventario**, que publica el release v1.1.0
con el archivo `sistema-inventario-v1.1.0.zip`.

Esperar a que termine la liberación antes de continuar.

## 2. Ejecutar el despliegue de v1.1.0

En GitHub:

1. Ir a **Actions**.
2. Seleccionar **Despliegue del Sistema de Inventario**.
3. Pulsar **Run workflow**.
4. Elegir `version = v1.1.0` y `simulate_failure = false`.
5. Ejecutar y esperar el resultado.

## 3. Ejecutar el fallo simulado y el rollback

Repetir **Run workflow** con:

- `version = v1.1.0`
- `simulate_failure = true`

El run mostrará el `ModuleNotFoundError`, luego la descarga de v1.0.0, su
transferencia, la ejecución y el mensaje `ROLLBACK_OK`.

## 4. Descargar evidencias

En cada run, al final de la página, descargar el artefacto
`evidencia-despliegue-<versión>`. Contiene:

- `salida-ejecucion.txt`
- `salida-rollback.txt` (solo en el run de rollback)
- `listado-destino.txt`
- `listado-rollback.txt` (solo en el run de rollback)
- el ZIP desplegado

Guardar también una captura de pantalla del resumen del run y de la lista de
artefactos.

## 5. Completar el informe

En `docs/INFORME_DESPLIEGUE.html` (y volver a generar el PDF), sustituir la nota
pendiente de la sección 6 por:

- El enlace al run de v1.0.0.
- El enlace al run de v1.1.0.
- El enlace al run de fallo y rollback.
- Las capturas de pantalla correspondientes.

Para regenerar el PDF:

```bash
soffice --headless --convert-to pdf --outdir docs docs/INFORME_DESPLIEGUE.html
```

## 6. Verificación rápida del workflow

Antes de ejecutarlo se puede comprobar la sintaxis del YAML con:

```bash
ruby -ryaml -e 'YAML.load_file(".github/workflows/deploy.yml"); puts "YAML OK"'
```

Y las pruebas del proyecto con:

```bash
python3 -m unittest discover -s tests -v
```
