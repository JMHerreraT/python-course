import pytest
from tienda.productos import Producto, ProductoInvalidoError

"""
tests/test_producto.py, con un test para cada caso:

Un producto válido se crea correctamente (verifica su nombre y precio). ✅
Un nombre vacío lanza ProductoInvalidoError. ✅
Un precio igual a 0 lanza ProductoInvalidoError.✅
Un precio negativo lanza ProductoInvalidoError. ✅
precio_con_igv() calcula bien (por ejemplo, 100 → 118.0). ✅
"""

def test_producto_valido():
    p = Producto("Laptop Valida", 200)
    assert p.nombre == "Laptop Valida" 
    assert p.precio == 200

def test_precio_con_igv():
    p = Producto("Laptop", 100)
    assert p.precio_con_igv() == 118.0           # expect(...).toBe(...) en Jest


def test_nombre_vacio_lanza_error():
    with pytest.raises(ProductoInvalidoError, match="vacío"):   # expect(() => ...).toThrow()
        Producto("", 10)

def test_precio_cero_lanza_error():
    with pytest.raises(ProductoInvalidoError, match="mayor"):   # expect(() => ...).toThrow()
        Producto("Producto con precio cero", 0)

def test_precio_negativo_lanza_error():
    with pytest.raises(ProductoInvalidoError, match="mayor"):   # expect(() => ...).toThrow()
        Producto("Producto con precio negativo", -20)