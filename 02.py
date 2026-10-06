# Ejercicio 2

# Usa la misma products_list y resuelve cada punto en una sola línea con comprehensions o funciones incorporadas, sin for tradicional:

# Una lista solo con los nombres de los productos de categoría 1.
# Un diccionario donde la clave sea el nombre y el valor el precio: {"Producto 1": 32, ...}. 
# Pista: existe la dict comprehension, {clave: valor for ...}.
# La suma de todos los precios. Pista: busca la función sum().
# El producto más barato, como tupla (nombre, precio).

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

print("Una lista solo con los nombres de los productos de categoría 1.")
my_list = [product for product in products_list if product["categoria"] == 1]
print(f"my_list: {my_list}")

print("\nUn diccionario donde la clave sea el nombre y el valor el precio: {'Producto 1': 32, ...}.")
print("Pista: existe la dict comprehension, {clave: valor for ...}.")

my_dict = { product['nombre']: product["precio"] for product in products_list }
print(f"my_dict: {my_dict}")

print("\nLa suma de todos los precios. Pista: busca la función sum().")
product_sum = sum(product['precio'] for product in products_list)
print(f"Sum of all product's prices: {product_sum}")

print("\nEl producto más barato, como tupla (nombre, precio).")
my_tuple = min(products_list, key=lambda p: p["precio"])
print(f"Cheapest product: {my_tuple}")

