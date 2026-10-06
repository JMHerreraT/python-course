import pytest
from tienda.productos import Producto
from tienda.carrito import Carrito

"""
tests/test_carrito.py, con un test para cada caso:

Un carrito nuevo tiene total 0. ✅
Después de agregar productos, el total es correcto. ✅
buscar encuentra un producto sin importar mayúsculas o minúsculas. ✅
buscar lanza KeyError si el producto no existe. ✅
"""

def test_carrito_nuevo_tiene_total_cero():
    carrito = Carrito()

    assert carrito.total() == 0

def test_total_correcto():
    producto = Producto("Laptop", 20)
    producto_dos = Producto("Tablet", 10)

    carrito = Carrito()

    carrito.agregar(producto)
    carrito.agregar(producto_dos)

    assert carrito.total() == 35.4

def test_buscar_producto_en_carrito():
    producto = Producto("Laptop", 20)
    carrito = Carrito()

    carrito.agregar(producto)

    assert carrito.buscar("laptop") == producto

def test_buscar_producto_lanza_error():
    producto = Producto("Laptop", 20)
    carrito = Carrito()

    carrito.agregar(producto)
    with pytest.raises(KeyError):
        carrito.buscar("Computadora")
