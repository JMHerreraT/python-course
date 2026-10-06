from tienda.carrito import Carrito
from tienda.productos import Producto, ProductoInvalidoError


def main() -> None:
    carrito = Carrito()
    carrito.agregar(Producto("Laptop", 3000))
    carrito.agregar(Producto("Mouse", 50))
    carrito.agregar(Producto("Teclado", 120, categoria=2))
    print(carrito)

    try:
        Producto("", 10)
    except ProductoInvalidoError as e:
        print(f"Producto inválido: {e}")


if __name__ == "__main__":
    main()