# Apuntes

## Instrucciones

### 1. Crear el ambiente virtual

python -m venv nombre_ambiente

### 2. Activar el ambiente virtual

Linux:
source nombre_ambiente/bin/activate.fish

Windows:
<nombre_ambiente>\Scripts\activate

#### Si no se puede activar
Set-ExecutionPolicy Bypass -Scope CurrentUser

#### Desactivar ambiente virtual
deactivate

### 3. Actualizar PIP

python -m pip install --upgrade pip

### 4. Instalar Django

pip install django

### 5. Crear el entorno de Django

django-admin startproject motor_django .

    En nuestro caso:

django-admin startproject core .

### 6. Crear la carpeta App

django-admin startapp nombre_aplicacion







# Evaluacion 1
Pagina de bienvenida
pagina de error que solo contenga "Hubo un error"