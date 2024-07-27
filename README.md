
# Vicodin

Vicodin es un proyecto de una farmacéutica que permite la gestión de Clientes, Productos y Publicaciones para un pequeño blog. Utiliza la API de Django para dar de alta estos modelos a través de formularios (Forms).

## Instalación
1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Asegurarse de tener pipenv instalado en el sistema y luego ejecutar
```bash
pipenv install -r requirements.txt
```
4. Ejecuta el siguiente comando para iniciar el servidor:
```bash
python manage.py runserver
```

## Uso

Una vez que el proyecto esté en funcionamiento, ir a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para visualizarlo.

En el menú principal, encontrarás cinco opciones: Inicio, Clientes, Productos, Publicaciones y Buscar Productos. Cada opción te dirigirá al formulario correspondiente para dar de alta el modelo relacionado.

- **Inicio:** Página HTML estática que servirá como base para el proyecto final.
- **Clientes:** Formulario para registrar nuevos clientes.
- **Productos:** Formulario para registrar nuevos productos.
- **Publicaciones:** Formulario para crear nuevas publicaciones en el blog.
- **Buscar Productos:** Formulario para buscar productos por el campo de Nombre. Por ejemplo, puedes buscar "Barbijo" para ver algunos productos precargados.

## Administrador

Para acceder al administrador de Django, utiliza las siguientes credenciales:

- **Nombre de usuario:** ayrton
- **Contraseña:** 123123

