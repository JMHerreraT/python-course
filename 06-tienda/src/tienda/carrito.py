from .productos import Producto


class Carrito:
    def __init__(self) -> None:
        # Lista: un carrito puede tener productos repetidos y conserva el orden en que se agregan
        self._productos: list[Producto] = []

    def agregar(self, producto: Producto) -> None:
        self._productos.append(producto)

    def buscar(self, nombre: str) -> Producto:
        for producto in self._productos:
            if nombre.lower() == producto.nombre.lower():
                print(f"PRODUCTO encontrado: {producto}")

                return producto
        raise KeyError(f"Producto con nombre {nombre} no encontrado o no existe")

    def total(self) -> float:
        return round(sum(p.precio_con_igv() for p in self._productos), 2)

    def __repr__(self) -> str:
        return f"Carrito({len(self._productos)} productos, total={self.total()})"