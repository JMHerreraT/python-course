"""
Ejercicio 4

Con la misma products_list:

Crea la excepción ProductoInvalidoError.
Escribe validar_producto(producto: dict) -> None, que lance ProductoInvalidoError con un mensaje claro si:
falta alguna de las claves nombre, precio o categoria,
nombre está vacío,
precio es menor o igual a 0.
Escribe agregar_producto(productos: list[dict], producto: dict) -> None, que valide el producto y, si pasa, lo agregue a la lista.
Escribe buscar_producto(productos: list[dict], nombre: str) -> dict, que devuelva el producto con ese nombre o lance KeyError si no existe.
Pruébalo: agrega un producto válido y tres inválidos (uno por cada regla), y busca un producto que existe y otro que no. 
Cada intento debe ir en su propio try/except e imprimir el mensaje del error sin que el programa se caiga.

Pista para el punto 2: "nombre" in producto te dice si la clave existe. 
Y para revisar varias claves de una vez, piensa qué estructura sirve para preguntar "¿está?".
"""

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

class ProductoInvalidoError(Exception):
    """Se lanza cuando un producto no cumple las reglas de validación."""  # CAMBIO 1


CAMPOS_REQUERIDOS = {"nombre", "precio", "categoria"}


def validar_producto(producto: dict) -> None:
    """Lanza ProductoInvalidoError si el producto no cumple las reglas."""
    faltantes = CAMPOS_REQUERIDOS - producto.keys()
    if faltantes:
        raise ProductoInvalidoError(f"Faltan campos: {faltantes}")

    if not producto["nombre"]:
        raise ProductoInvalidoError("El nombre no puede estar vacío")

    if producto["precio"] <= 0:
        raise ProductoInvalidoError(f"El precio debe ser mayor a 0, recibido: {producto['precio']}")

def agregar_producto(productos: list[dict], producto: dict) -> None:
    """
    Valida el producto y, si pasa, lo agrega a la lista.
    """
    validar_producto(producto)
    productos.append(producto)
    # CAMBIO 2: se quitaron los print

def buscar_producto(productos: list[dict], nombre: str) -> dict:
    """
    Devuelve el producto con ese nombre o lanza KeyError si no existe.
    """
    for producto in productos:
        if nombre.lower() == producto["nombre"].lower():  # CAMBIO 3
            return producto
    raise KeyError(f"Producto con nombre {nombre} no encontrado o no existe")  # CAMBIO 4


# CAMBIO 5: cada prueba en su propio try/except

# 1. Producto válido
try:
    valid_product = {"nombre": "Producto Y", "precio": 30, "categoria": 1}
    agregar_producto(products_list, valid_product)
    print(f"Agregado: {valid_product['nombre']}. Total de productos: {len(products_list)}")
except ProductoInvalidoError as e:
    print(f"Producto inválido: {e}")

# 2. Inválido: falta una clave
try:
    agregar_producto(products_list, {"nombre": "Sin precio", "categoria": 1})
    print("Agregado (no debería llegar aquí)")
except ProductoInvalidoError as e:
    print(f"Producto inválido: {e}")

# 3. Inválido: nombre vacío
try:
    agregar_producto(products_list, {"nombre": "", "precio": 10, "categoria": 1})
    print("Agregado (no debería llegar aquí)")
except ProductoInvalidoError as e:
    print(f"Producto inválido: {e}")

# 4. Inválido: precio <= 0
try:
    invalid_product = {"nombre": "Producto X", "precio": 0, "categoria": 1}
    agregar_producto(products_list, invalid_product)
    print("Agregado (no debería llegar aquí)")
except ProductoInvalidoError as e:
    print(f"Producto inválido: {e}")

# 5. Búsqueda que existe
try:
    encontrado = buscar_producto(products_list, "producto y")
    print(f"Encontrado: {encontrado}")
except KeyError as e:  # CAMBIO 6
    print(f"No encontrado: {e}")

# 6. Búsqueda que no existe
try:
    encontrado = buscar_producto(products_list, "Producto Z")
    print(f"Encontrado: {encontrado}")
except KeyError as e:
    print(f"No encontrado: {e}")