# Preguntas de reflexión

**1. ¿Cuál es la diferencia entre liberar una versión y desplegarla?**

Liberar (RELEASE) es identificar, empaquetar y publicar una versión del
sistema, por ejemplo v1.0.0 en GitHub Releases. Desplegar (DEPLOY) es tomar ese
paquete ya publicado, instalarlo en un entorno de destino, configurarlo y
verificar que funciona. Liberar produce el artefacto; desplegar lo pone en
operación.

**2. ¿Por qué se utiliza el paquete generado en la fase RELEASE?**

Porque ese paquete es el artefacto oficial, probado y versionado que se
publicó. Usarlo garantiza que se despliega exactamente lo que se liberó, evita
diferencias entre la computadora del desarrollador y el destino y permite
repetir el despliegue de la misma versión.

**3. ¿Qué función tiene el entorno de destino?**

Es el lugar donde el sistema se instala y se ejecuta para los usuarios. Debe
cumplir los requisitos (sistema operativo, lenguaje, dependencias, acceso) y
es donde se realizan las pruebas de funcionamiento posteriores al despliegue.

**4. ¿Qué información se necesita para establecer una conexión SSH?**

La dirección o nombre del servidor, el usuario, la llave privada (o
contraseña), el puerto (normalmente 22) y la llave pública autorizada en el
servidor. En GitHub Actions estos datos se guardan como secretos:
`DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY` y `DEPLOY_PORT`.

**5. ¿Por qué es importante utilizar secretos de GitHub?**

Porque las llaves privadas y las contraseñas no deben quedar escritas en el
repositorio ni en los archivos YAML. Los secretos se almacenan cifrados, se
enmascaran en los logs y solo se inyectan en tiempo de ejecución, lo que reduce
el riesgo de filtraciones.

**6. ¿Qué ventajas ofrece automatizar el despliegue?**

Reduce errores manuales, garantiza que siempre se use el mismo procedimiento y
el mismo artefacto, ahorra tiempo, deja evidencia de cada ejecución y permite
repetir el despliegue o el rollback de forma consistente.

**7. ¿Qué problemas pueden presentarse cuando el entorno de destino no cumple
los requisitos?**

El sistema puede no iniciar (por ejemplo, `python3: command not found`), fallar
al importar módulos, no poder extraer el paquete por falta de `unzip`, no
conectarse por SSH si el servicio o el puerto no están disponibles, o presentar
errores de permisos. Por eso se documentan los requisitos y se comprueban antes
de desplegar.

**8. ¿Por qué es necesario contar con un procedimiento de recuperación?**

Porque una versión nueva puede fallar y el servicio no puede quedar caído. Un
rollback documentado y probado permite volver rápidamente a la última versión
estable, reduce el tiempo de inactividad y deja constancia de lo ocurrido para
corregir la causa.
