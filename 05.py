"""
Ejercicio 5

Vas a rehacer el ejercicio 4 con clases.

Crea una dataclass Producto con nombre, precio y categoria, y un método precio_con_igv().
Mueve la validación a la propia clase: si el nombre está vacío o el precio es menor o igual a 0, que lance ProductoInvalidoError al crear el producto.
Pista: una dataclass genera __init__ automáticamente, así que no puedes escribirlo tú. Investiga el método __post_init__, que se ejecuta justo después del __init__ generado.
Crea una clase Carrito (normal, no dataclass) con:
agregar(producto)
buscar(nombre), que lance KeyError si no existe
total(), que devuelva la suma de precios con IGV
__repr__, para que al imprimirlo muestre cuántos productos tiene y el total
Decisión de estructura: dentro de Carrito, ¿guardas los productos en una lista o en un diccionario? Elige y justifica en un comentario de una línea. Pista: fíjate qué operaciones tiene la clase.
Prueba: crea un carrito, agrega tres productos válidos, intenta crear uno inválido, busca uno que existe y otro que no, e imprime el carrito.

Ya no necesitas validar que falten campos, como hacía CAMPOS_REQUERIDOS. ¿Por qué? Piénsalo mientras lo escribes; es parte de lo que ganas al usar clases.
"""

from dataclasses import dataclass


class ProductoInvalidoError(Exception):
    """Se lanza cuando un producto no cumple las reglas de validación."""  # CAMBIO 1


@dataclass
class Producto:
    nombre: str
    precio: float
    categoria: int = 1

    # CAMBIO 2: se eliminó validate_product; la validación va directo aquí
    def __post_init__(self) -> None:
        if not self.nombre:
            raise ProductoInvalidoError("El nombre no puede estar vacío")
        if self.precio <= 0:
            raise ProductoInvalidoError(f"El precio debe ser mayor a 0, recibido: {self.precio}")

    def precio_con_igv(self) -> float:
        return round(self.precio * 1.18, 2)


class Carrito:
    # CAMBIO 3: se eliminó la anotación "productos: list[Producto]" a nivel de clase

    def __init__(self) -> None:  # CAMBIO 4
        # Lista: un carrito puede tener productos repetidos y conserva el orden en que se agregan
        self._productos: list[Producto] = []

    def agregar(self, producto: Producto) -> None:  # CAMBIO 5
        self._productos.append(producto)

    def buscar(self, nombre: str) -> Producto:
        for producto in self._productos:
            if nombre.lower() == producto.nombre.lower():  # CAMBIO 6
                return producto
        raise KeyError(f"Producto con nombre {nombre} no encontrado o no existe")

    def total(self) -> float:
        return round(sum(p.precio_con_igv() for p in self._productos), 2)  # CAMBIO 7

    def __repr__(self) -> str:
        return f"Carrito({len(self._productos)} productos, total={self.total()})"  # CAMBIO 8


# CAMBIO 9: pruebas

carrito = Carrito()

# 1. Tres productos válidos
carrito.agregar(Producto("Laptop", 3000))
carrito.agregar(Producto("Mouse", 50))
carrito.agregar(Producto("Teclado", 120, categoria=2))
print(carrito)

# 2. Producto inválido: falla al CREARLO, no al agregarlo
try:
    carrito.agregar(Producto("", 10))
    print("Agregado (no debería llegar aquí)")
except ProductoInvalidoError as e:
    print(f"Producto inválido: {e}")

# 3. Búsqueda que existe
try:
    print(f"Encontrado: {carrito.buscar('mouse')}")
except KeyError as e:
    print(f"No encontrado: {e}")

# 4. Búsqueda que no existe
try:
    print(f"Encontrado: {carrito.buscar('Monitor')}")
except KeyError as e:
    print(f"No encontrado: {e}")

print(carrito)         