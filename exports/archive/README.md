Archivos archivados desde el repositorio raíz.

Motivo: mover binarios grandes fuera de la raíz del repositorio para mantener el tamaño y evitar commits accidentales.

Archivos movidos:
- Carrera_de_Analista_de_Datos.mp4    (ubicación original: exports/)

Si necesitas restaurar algún archivo al lugar original, ejecutar:

```powershell
git mv exports\archive\Carrera_de_Analista_de_Datos.mp4 exports\
git commit -m "restore: mover archivo de vuelta"
git push
```
