# Copiar este repositorio de la siguiente manera:

Si ya lo tenías clonado, viendo que existe en tu PC la rama "clase_18", entonces ejecuta el siguiente comando en la terminal, en tu proyecto. Dejará tu rama "clase_17" sin modificar, y creará la rama "clase_18":

**`git pull origin clase_19`**

De lo contrario, en una carpeta nueva, vacía, ejecuta en la terminal el siguiente comando:

**`git clone https://github.com/esthorace/Coderhouse_40445.git`**

Para ver este archivo en VScode con mayor legibilidad, presionar `control + shift + v`

He agregado una carpeta llamada `.vscode` que tiene un archivo llamado `settings.json`. He configurado las extensiones para que vayamos trabajando con lo mismo.

## Comandos para crear un proyecto y una aplicación

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

`mkdir project`
> Crea un directorio llamado project

`cd project`
> Cambia de directorio

`django-admin startproject config .`
> Crea un proyecto en el directorio actual, en la carpeta config

`python manage.py runserver`
> Ejecuta el servidor. Para pararlo: control + c (cmd + c en Mac)

`mkdir apps`
> Crea un directorio llamado 'apps' que contendrá las aplicaciones de Django

`cd apps`
> Cambia de directorio para poder crear las aplicaciones

`django-admin startapp nombre_app`
> Crea una nueva aplicación (recuerda registrarla en settings.py)

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin

## Nota sobre Git y las clases

Puedes cambiar de ramas para ver cada clase.

## Requirements.txt

Este archivo fue creado con el siguiente comando:
`pip freeze >> requirements.txt`

Si no tienes el entorno virtual creado, puedes abrir el archivo con Visual Studio Code y hacer clic en **Crear ambiente**, luego elegir Venv, luego el intérprete Python (última versión), y finalmente pregunta por las dependencias: elegimos requirements.txt.
