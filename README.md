# Proyecto E-commerce Django
Aplicación web desarrollada en Django para la gestión de productos.

1. Funcionalidades
 - Crear productos
 - Editar productos
 - Eliminar productos
 - Listar productos

2. Tecnologías utilizadas
 - Python
 - Django
 - Bootstrap
 - SQLite3
  
3. Base de Datos
   Motor de Base de Datos utilizado: SQLite3 (por defecto en Django)
   Puede ser cambiado a PostgreSQL, MySQL u otro según configuración en `settings.py`.


4. Descripción del Modelo de Datos

Modelo `Categoria`

Campos:
    nombre → CharField, nombre de la categoría
    Relación: `Producto` tiene ForeignKey a `Categoria`.

Modelo `Producto`
Campos:
    nombre` → CharField, nombre del producto
    categoria` → ForeignKey a `Categoria`
    precio` → IntegerField, precio del producto (solo enteros)
    Relación: cada producto pertenece a una categoría.


5. Rutas Principales

| Ruta | Método | Funcionalidad |
|------|--------|---------------|
| `` | GET | Listado de productos |
| `create/` | GET/POST | Crear un nuevo producto |
| `edit/<id>/` | GET/POST | Editar producto existente |
| `delete/<id>/` | GET/POST | Eliminar producto |



6.  Cómo ejecutar el proyecto (Microsoft)
a. Ingresar a la carpeta donde esta el proyecto (donde esta manage.py)  
b. Crear entorno virtual:      python -m venv env
c. Activar el entorno virtual:    env\Scripts\activate 
d. Intalar dependencias:          pip install django
e. Aplicar migraciones:           python manage.py makemigrations
                                  python manage.py migrate
f. Crear superusuario:            python manage.py createsuperuser
g. Ejecutar servidor:             python manage.py runserver
h. Abir navegador (microsoft):    http://127.0.0.1:8000/


5. Evidencias
Las capturas se encuentrar en la carpeta Capturas:
- Lista de productos  (Captura 1)
- Crear producto  (Captura 2)
- Editar producto  (Captura 3)
- Panel administrador  (Capturas 4 y 5)
 
