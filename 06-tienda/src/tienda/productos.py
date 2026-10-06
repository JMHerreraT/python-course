from dataclasses import dataclass


class ProductoInvalidoError(Exception):
    """Se lanza cuando un producto no cumple las reglas de validación."""


@dataclass
class Producto:
    nombre: str
    precio: float
    categoria: int = 1

    def __post_init__(self) -> None:

        if not self.nombre:
            raise ProductoInvalidoError("El nombre no puede estar vacío")
        if self.precio <= 0:
            raise ProductoInvalidoError(f"El precio debe ser mayor a 0, recibido: {self.precio}")

    def precio_con_igv(self) -> float:
        return round(self.precio * 1.18, 2)