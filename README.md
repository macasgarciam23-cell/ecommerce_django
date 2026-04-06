# Proyecto E-commerce Django

1. Motor de Base de Datos utilizado: SQLite3 (por defecto en Django)
    Puede ser cambiado a PostgreSQL, MySQL u otro según configuración en `settings.py`.


2. Descripción del Modelo de Datos

# Modelo `Categoria`

Campos:
    nombre → CharField, nombre de la categoría
    Relación: `Producto` tiene ForeignKey a `Categoria`.

# Modelo `Producto`
Campos:
    nombre` → CharField, nombre del producto
    categoria` → ForeignKey a `Categoria`
    precio` → IntegerField, precio del producto (solo enteros)
    Relación: cada producto pertenece a una categoría.



3. Rutas Principales del Módulo de Administración

| Ruta | Método | Funcionalidad |
|------|--------|---------------|
| `` | GET | Listado de productos |
| `create/` | GET/POST | Crear un nuevo producto |
| `edit/<id>/` | GET/POST | Editar producto existente |
| `delete/<id>/` | GET/POST | Eliminar producto |


# 4. Pasos para Ejecutar el Proyecto

1. Clonar el repositorio o descomprimir el proyecto.
2. Crear un entorno virtual (opcional pero recomendado):
   Terminal 
   python -m venv env
   env\Scripts\activate  # Windows
   source env/bin/activate  # Mac/Linux

3. Dependencias: 
    pip install django 


4. Aplicar migraciones
    python manage.py makemigrations
    python manage.py migrate

5. Crear superusuario (opcional, para panel admin):
    python manage.py createsuperuser

6. Ejecutar servidor 
    python manage.py runserver

7. Acceder al navegador 
127.0.0.1:8000
    


# Evidencias
    
 Listado de Productos (Captura 1 "Lista_Productos")

 Formulario Crear Producto (Captura 2 "Crear_Producto")

 Formulario Editar Producto (Captura 3 "Editar_producto")

 Panel Administrativo Django (Captura 4 "Admin_categoria" y 5 "Admin_Productos)