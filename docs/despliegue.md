# Procedimiento de despliegue del Sistema de Inventario

## 1. Información de la versión

| Dato | Valor |
| --- | --- |
| Repositorio | https://github.com/gemo98/sistema-inventario |
| Versión desplegada | v1.0.0 |
| Fecha de publicación | 2026-11-17 (21:28:03 UTC) |
| Archivo descargado | `sistema-inventario-v1.0.0.zip` |
| Tamaño | 1 784 bytes |
| SHA-256 | `573a4455613d077e9e54c43b31b9dc94e73077009e73a98bf3a1ae90d6ff633d` |
| URL del release | https://github.com/gemo98/sistema-inventario/releases/tag/v1.0.0 |
| Ubicación del despliegue | `~/sistema-inventario/version-v1.0.0` (runner de GitHub Actions) |

La versión v1.1.0 se publica durante el ejercicio de rollback y agrega el
registro de productos.

## 2. Requisitos del entorno

- Linux (probado en Ubuntu; GitHub Actions usa `ubuntu-latest`).
- Python 3.12 o superior.
- `unzip`.
- Cliente y servidor OpenSSH para el despliegue automatizado.
- Acceso al repositorio y a GitHub Releases.

Comprobación:

```bash
python3 --version
unzip -v | head -n 1
ssh -V
```

Evidencia: [`evidencias/02-requisitos-entorno.txt`](evidencias/02-requisitos-entorno.txt).

## 3. Descarga del paquete

El paquete **no se genera de nuevo**: se descarga el artefacto publicado en la
fase RELEASE.

```bash
mkdir -p ~/despliegue-inventario
cd ~/despliegue-inventario
curl -L -o sistema-inventario-v1.0.0.zip \
  https://github.com/gemo98/sistema-inventario/releases/download/v1.0.0/sistema-inventario-v1.0.0.zip
sha256sum sistema-inventario-v1.0.0.zip
```

Evidencia: [`evidencias/01-version-descargada.txt`](evidencias/01-version-descargada.txt).

## 4. Extracción del paquete

```bash
unzip -o sistema-inventario-v1.0.0.zip -d despliegue-v1.0.0
cd despliegue-v1.0.0
find . -type f
```

El paquete contiene:

```text
src/producto.py
src/busqueda.py
```

Evidencia: [`evidencias/03-despliegue-manual-v1.0.0.txt`](evidencias/03-despliegue-manual-v1.0.0.txt).

## 5. Configuración necesaria

El sistema no requiere variables de entorno ni base de datos. Solo necesita
Python y los archivos de `src/`. El punto de entrada es `src/busqueda.py`.

Compilación de comprobación:

```bash
python3 -m compileall src
```

## 6. Ejecución del sistema

```bash
python3 src/busqueda.py
```

Menú de v1.0.0:

1. Buscar por código.
2. Buscar por nombre.
3. Salir.

Menú de v1.1.0:

1. Buscar por código.
2. Buscar por nombre.
3. Registrar producto.
4. Salir.

## 7. Comprobación de que funciona

Para v1.0.0:

```bash
printf '1\nLIB-002\n3\n' | python3 src/busqueda.py
```

Debe mostrarse `Pedro Páramo`, precio `$199.50 MXN` y existencia `8 unidades`.

Para v1.1.0:

```bash
printf '3\nLIB-006\nEl principito\n250\n7\n1\nLIB-006\n4\n' | python3 src/busqueda.py
```

Debe registrarse `LIB-006` y mostrarse después al consultarlo por código.

Evidencias: [`evidencias/04-verificacion-v1.0.0.txt`](evidencias/04-verificacion-v1.0.0.txt)
y [`evidencias/05-despliegue-manual-v1.1.0.txt`](evidencias/05-despliegue-manual-v1.1.0.txt).

## 8. Automatización con GitHub Actions

El workflow se encuentra en `.github/workflows/deploy.yml`. Se ejecuta
manualmente (`workflow_dispatch`) con dos parámetros y también se dispara al
modificar el propio archivo del workflow en `main`, en cuyo caso despliega
v1.0.0 automáticamente para dejar la primera evidencia.

Parámetros de ejecución manual:

| Parámetro | Descripción | Valor por defecto |
| --- | --- | --- |
| `version` | Versión liberada que se desplegará | `v1.0.0` |
| `simulate_failure` | Simula un fallo y ejecuta el rollback a v1.0.0 | `false` |

Pasos del workflow:

1. Prepara un servidor de destino con SSH local dentro del runner
   (`runner@127.0.0.1`) e instala Python/OpenSSH/unzip.
2. Descarga el ZIP de la versión indicada desde GitHub Releases con `gh`.
3. Transfiere el ZIP al servidor con `scp`.
4. Extrae el paquete en `~/sistema-inventario/version-<versión>` con `ssh`.
5. Si `simulate_failure` está activo, inserta una dependencia inexistente para
   provocar el fallo.
6. Ejecuta el sistema por SSH y verifica la salida esperada.
7. Si se simuló el fallo, comprueba que el error aparezca en la salida.
8. Si se simuló el fallo, descarga v1.0.0, la transfiere, la extrae en
   `version-rollback` y verifica que vuelva a funcionar.
9. Publica las salidas y los ZIP como artefacto de evidencia.

### Ejecución

En GitHub: **Actions → Despliegue del Sistema de Inventario → Run workflow**.

Guía paso a paso para subir, ejecutar y descargar evidencias:
[`como-ejecutar-el-workflow.md`](como-ejecutar-el-workflow.md).

Secuencia recomendada para la práctica:

| Ejecución | `version` | `simulate_failure` | Resultado esperado |
| --- | --- | --- | --- |
| 1 | `v1.0.0` | `false` | Despliegue y verificación correctos |
| 2 | `v1.1.0` | `false` | Despliegue con registro de productos |
| 3 | `v1.1.0` | `true` | Fallo simulado + rollback a v1.0.0 |

## 9. Despliegue en un servidor externo real (opcional)

El mismo workflow puede apuntar a una máquina virtual o servidor con SSH.
Basta con reemplazar las variables `SERVER_USER` y `SERVER_HOST` por los
secretos del repositorio:

| Secreto | Contenido |
| --- | --- |
| `DEPLOY_HOST` | IP o nombre del servidor |
| `DEPLOY_USER` | Usuario de acceso |
| `DEPLOY_KEY` | Llave privada SSH |
| `DEPLOY_PORT` | Puerto SSH (normalmente 22) |

Los secretos se configuran en **Settings → Secrets and variables → Actions →
New repository secret**. Nunca deben escribirse en el YAML.

## 10. Problemas que podrían presentarse y cómo resolverlos

| Problema | Causa probable | Solución |
| --- | --- | --- |
| `python3: command not found` | Python no instalado | Instalar Python 3.12+ y verificar con `python3 --version`. |
| `unzip: command not found` | Falta `unzip` | `sudo apt-get install -y unzip`. |
| `ModuleNotFoundError: No module named 'producto'` | Se ejecutó desde otra carpeta | Ejecutar desde la raíz extraída: `python3 src/busqueda.py`. |
| `Permission denied (publickey)` | Llave SSH incorrecta o sin autorizar | Revisar `DEPLOY_KEY`, `authorized_keys` y permisos (`600`). |
| `Connection refused` en el puerto 22 | SSH no iniciado o puerto distinto | Iniciar `ssh` y revisar `DEPLOY_PORT`. |
| `gh: release not found` | La versión aún no se ha publicado | Verificar el tag y que `release.yml` haya terminado. |
| `unzip: cannot find zipfile` | El ZIP no se transfirió | Revisar el paso `scp` y el nombre del archivo. |
| El sistema no registra productos en v1.0.0 | Funcionalidad no incluida en esa versión | Usar v1.1.0 o registrar desde el código. |
| El rollback no encuentra v1.0.0 | El release fue eliminado | Conservar el ZIP descargado y usarlo como respaldo. |

## 11. Procedimiento de rollback

1. Conservar el paquete de la versión estable (`sistema-inventario-v1.0.0.zip`).
2. Detener el uso de la versión con problemas.
3. Extraer de nuevo la versión estable en un directorio limpio
   (`version-rollback`).
4. Ejecutar y verificar la versión estable.
5. Documentar el incidente y la recuperación.

El workflow automatiza estos pasos cuando `simulate_failure` es `true`.
Evidencia local del procedimiento:
[`evidencias/06-rollback.txt`](evidencias/06-rollback.txt).

## 12. Índice de evidencias

| Evidencia | Archivo |
| --- | --- |
| Versión descargada desde Releases | `evidencias/01-version-descargada.txt` |
| Requisitos del entorno | `evidencias/02-requisitos-entorno.txt` |
| Despliegue manual de v1.0.0 | `evidencias/03-despliegue-manual-v1.0.0.txt` |
| Verificación funcional de v1.0.0 | `evidencias/04-verificacion-v1.0.0.txt` |
| Verificación local de v1.1.0 | `evidencias/05-despliegue-manual-v1.1.0.txt` |
| Simulación de fallo y rollback | `evidencias/06-rollback.txt` |
| Ejecución del workflow de despliegue v1.0.0 | `evidencias/07-workflow-v1.0.0.txt` |
| Ejecución de la liberación v1.1.0 | `evidencias/08-release-v1.1.0.txt` |
| Despliegue de v1.1.0 y rollback en Actions | Pendiente de ejecutar (ver `como-ejecutar-el-workflow.md`) |

## 13. Limitación declarada

Para esta entrega el entorno de destino es el runner de GitHub Actions. El
workflow simula un servidor mediante un servicio SSH local (`127.0.0.1`) para
producir evidencia real de transferencia (`scp`) y ejecución remota (`ssh`).
No se utiliza una máquina virtual externa. El procedimiento para un servidor
real se documenta en la sección 9 y solo requiere cambiar los secretos.
