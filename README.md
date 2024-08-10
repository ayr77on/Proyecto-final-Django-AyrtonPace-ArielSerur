
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

## Descripción del Proyecto

Una vez ingresando a la URL, se puede ver el inicio de la página. Se pueden ver 4 opciones en el menú:

1. **Inicio**: Lleva a la página de inicio.
2. **Sobre nosotros**: Página explicando quiénes somos.
3. **Productos**: Una página para ver los productos cargados.
4. **Buscar productos**: Un formulario para buscar los productos cargados.

## Autenticación

Tenemos la opción para loguearnos y registrarnos en el sistema. Aquí detallo algunos usuarios ya cargados:

- **Usuario**: Ayrton  
  **Contraseña**: Test123!

- **Usuario**: Ariel  
  **Contraseña**: Test123!

- **Usuario**: Farma  
  **Contraseña**: Test123!

## Funcionalidades después de Iniciar Sesión

Una vez logueados en el sistema, se encontrarán con una opción más en el menú que es **"Publicaciones"**. Esta opción se habilita una vez que se ingresa al sistema porque se pensó como una especie de intranet donde solamente los usuarios autenticados pueden ver las publicaciones realizadas. Tambien se pueden comentar las publicaciones para demostrar tu opinión acerca de los demas posteos.

### Roles de Usuarios

- **Ayrton y Ariel**: Son super administradores. Esto quiere decir que cuando estos usuarios ingresan al sistema, pueden modificar y borrar las publicaciones que hicieron otros usuarios.
- **Farma**: Es un administrador corriente que solo puede editar y modificar sus publicaciones.

## Metodología de Trabajo

Para el desarrollo del proyecto, nos juntamos para trabajar mediante la metodología de pair programming, es decir, se iba haciendo el trabajo a la par para ir entendiendo los conceptos, aprendiendo de los errores juntos y ayudándonos para encontrar la solución.


## Administrador

Para acceder al administrador de Django, utiliza las siguientes credenciales:

- **Nombre de usuario:** Ayrton
- **Contraseña:** Test123!


## Demo del sistema
[URL VIDEO](https://www.youtube.com/watch?v=t17pKjN1oAc)



