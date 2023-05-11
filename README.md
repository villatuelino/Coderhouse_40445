# Copiar este repositorio de la siguiente manera:

Si ya lo tenías clonado, viendo que existe en tu PC la rama "clase_17", entonces ejecuta el siguiente comando en la terminal, en tu proyecto. Dejará tu rama "clase_17" sin modificar, y creará la rama "clase_18":

**`git pull origin clase_18`**

De lo contrario, en una carpeta nueva, vacía, ejecuta en la terminal el siguiente comando:

**`git clone https://github.com/esthorace/Coderhouse_40445.git`**

Para ver este archivo en VScode con mayor legibilidad, presionar `control + shift + v`

- Extensiones sugeridas para trabajar con Django:

    1. **Black Formatter** (sirve para auto formatear el código Python)
    2. **Isort** (sirve para auto ordenar importaciones en Python)
    3. **IntelliCode** (ayuda para varios lenguajes de programación)
    4. **Git Graph** (ayuda para cualquier proyecto Git)
    5. **Django Support** (color de sintaxis y autocompletado para Django)
    6. **SQLite Viewer** (visualizador de bases de datos SQLite3)
    7. **djLint** (formateador y linter para HTML con Django)

Además, he agregado una carpeta llamada `.vscode` que tiene un archivo llamado `settings.json`. He configurado las extensiones para que vayamos trabajando con lo mismo.

## Comandos

`mkdir nueva_carpeta`
> Crea una carpeta llamada nueva_carpeta

`ls`
> Muestra la lista de archivos

`cd nueva_carpeta`
> Cambia de carpeta

`pwd`
> Muestra la ruta actual

`python -m venv .venv`
> Crea un entorno virtual llamado .venv

`source .venv/bin/activate`
> Activa el entorno virtual en Linux o Mac

`.\venv\Scripts\activate`
> Activa el entorno virtual en Windows

`pip list`
> Muestra la lista de paquetes disponibles en el entorno virtual

`pip install django`
> Instala Django

`pip install djlint`
> Instala djLint, necesario para la extensión djLint de VSCode

`django-admin startproject config .`
> Crea un proyecto en el directorio actual

`python manage.py runserver`
> Ejecuta el servidor

`python manage.py startapp app`
> Crea una nueva aplicación llamada app

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin

## Nota sobre Git

Recuerda cambiar de rama a **clase_17** y ver el `README.md` para ver el flujo de trabajo con Git.

## Requirements.txt

Este archivo fue creado con el siguiente comando:
`pip freeze >> requirements.txt`

Si no tienes el entorno virtual creado, puedes abrir el archivo con Visual Studio Code y hacer clic en **Crear ambiente**, luego elegir Venv, luego el intérprete Python (última versión), y finalmente pregunta por las dependencias: elegimos requirements.txt.
