# Crea una lista de diccionarios con 3 productos. 
# Cada uno debe tener 
# nombre, precio y categoria, 
# y al menos dos productos deben compartir categoría.
# Recorre la lista e imprime solo los productos 
# que cuesten más de 20.
# Usando un set, imprime las categorías sin repetir.

# Guarda en una tupla el nombre y 
# el precio del producto más caro, e imprímela.

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
    
category_set = set()

higher_price = 0
my_tuple = ()
for product in products_list:
    category_set.add(product["categoria"])
    if product["precio"]> 20:
        print(f"product higher than 20: {product} \n")
    if product["precio"] > higher_price: 
        higher_price = product["precio"]
        my_tuple = (product["nombre"], product["precio"])

print(f"categorias sin repetir: {category_set} \n")
print(f"producto mas caro: {my_tuple}")

