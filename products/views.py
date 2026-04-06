from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from django.contrib import messages

# Create your views here.


# LISTAR PRODUCTOS
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista.html", {"productos": productos})


# CREAR PRODUCTO


def crear_producto(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        categoria_id = request.POST.get("categoria", "").strip()
        precio = request.POST.get("precio", "").strip()

        errores = []

        if not nombre:
            errores.append("El nombre es obligatorio.")
        if not categoria_id:
            errores.append("Debe seleccionar una categoría.")
        if not precio:
            errores.append("El precio es obligatorio.")
        else:
            try:
                precio = float(precio)
                if precio <= 0:
                    errores.append("El precio debe ser mayor a 0.")
            except ValueError:
                errores.append("El precio debe ser un número válido.")

        if errores:
            for error in errores:
                messages.error(request, error)
            return render(
                request,
                "crear.html",
                {
                    "categorias": categorias,
                    "nombre": nombre,
                    "precio": request.POST.get("precio", ""),
                    "categoria_id": categoria_id,
                },
            )
        categoria = get_object_or_404(Categoria, id=int(categoria_id))
        Producto.objects.create(nombre=nombre, categoria=categoria, precio=precio)
        messages.success(request, f"Producto '{nombre}' creado correctamente.")
        return redirect("lista_productos")

    return render(request, "crear.html", {"categorias": categorias})


# EDITAR PRODUCTO


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        categoria_id = request.POST.get("categoria", "").strip()
        precio = request.POST.get("precio", "").strip()

        errores = []

        if not nombre:
            errores.append("El nombre es obligatorio.")
        if not categoria_id:
            errores.append("Debe seleccionar una categoría.")
        if not precio:
            errores.append("El precio es obligatorio.")
        else:
            try:
                precio = float(precio)
                if precio <= 0:
                    errores.append("El precio debe ser mayor a 0.")
            except ValueError:
                errores.append("El precio debe ser un número válido.")

        if errores:
            for error in errores:
                messages.error(request, error)
            return render(
                request,
                "editar.html",
                {
                    "producto": producto,
                    "categorias": categorias,
                    "nombre": nombre,
                    "precio": request.POST.get("precio", ""),
                    "categoria_id": categoria_id,
                },
            )

        categoria = get_object_or_404(Categoria, id=int(categoria_id))
        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.save()
        messages.success(request, f"Producto '{nombre}' actualizado correctamente.")
        return redirect("lista_productos")

    return render(
        request, "editar.html", {"producto": producto, "categorias": categorias}
    )


# ELIMINAR PRODUCTO
def eliminar_producto(request, id):
    if request.method == "POST":
        try:
            producto = Producto.objects.get(id=id)
            producto.delete()
            messages.success(request, "Producto eliminado correctamente")
        except Producto.DoesNotExist:
            messages.error(request, "El producto no existe")

    return redirect("lista_productos")
