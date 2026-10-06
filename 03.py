"""
Ejercicio 3

Usando la misma products_list, escribe estas funciones con type hints y docstring:

productos_por_categoria(productos, categoria): devuelve la lista de nombres de esa categoría.
precio_con_igv(precio, igv=18): devuelve el precio con IGV incluido, redondeado a 2 decimales.
resumen(productos): devuelve tres valores a la vez: cantidad de productos, precio total y el nombre del producto más caro.
Llámala y desempaqueta el resultado en tres variables.
Llama a precio_con_igv usando argumentos por nombre, en orden invertido.

Pista para los type hints de listas y diccionarios: list[dict], list[str], etc.
"""

# CAMBIO 1: se eliminó "import math", ya no se usa

products_list = [
    {
        "nombre": "Producto 1",
        "precio": 32,
        "categoria": 1
    },
    {
        "nombre": "Producto 2",
        "precio": 5,
        "categoria": 1
    },
    {
        "nombre": "Producto 3",
        "precio": 20,
        "categoria": 2
    },
]

def productos_por_categoria(productos: list[dict], categoria: int) -> list[str]:
    """
    Devuelve la lista de nombres de esa categoría.
    """
    nombres = [product["nombre"] for product in productos if product["categoria"] == categoria]  # CAMBIO 2
    return nombres  # CAMBIO 2

def precio_con_igv(precio: float, igv: int = 18) -> float:  # CAMBIO 3
    """
    Devuelve el precio con IGV incluido, redondeado a 2 decimales.
    """
    precio_con_impuesto = precio * (1 + igv / 100)  # CAMBIO 4
    return round(precio_con_impuesto, 2)  # CAMBIO 5


def resumen(productos: list[dict]) -> tuple[int, int, str]:  # CAMBIO 6
    """
    devuelve tres valores a la vez:
        - cantidad de productos
        - precio total
        - el nombre del producto más caro
    """

    cantidad_productos = len(productos)
    total_price: int = sum(producto["precio"] for producto in productos)

    expensive_product = max(productos, key=lambda p: p["precio"])["nombre"]  # CAMBIO 7

    return cantidad_productos, total_price, expensive_product  # CAMBIO 8

cantidad_productos, total_price, expensive_product = resumen(products_list)
print(f"Cantidad de productos -> {cantidad_productos}\nPrecio total -> {total_price}\nProducto mas caro -> {expensive_product}")  # CAMBIO 9

# CAMBIO 10: probar las otras funciones
print(productos_por_categoria(products_list, 1))
print(precio_con_igv(100))
print(precio_con_igv(igv=18, precio=100))  # argumentos por nombre, en orden invertido
