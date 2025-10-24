# Cargar productos en una lista de diccionarios
productos = []

# Paso 1: Leer productos desde el archivo
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Paso 2: Mostrar productos
print("Productos actuales:")
for producto in productos:
    print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

# Paso 3: Agregar nuevo producto desde teclado
nuevo_nombre = input("Ingrese el nombre del producto a agregar: ")
nuevo_precio = float(input("Ingrese el precio: "))
nueva_cantidad = int(input("Ingrese la cantidad: "))

# Agregar al diccionario en memoria
productos.append({
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
})

# Paso 4: Buscar producto por nombre
buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == buscar.lower():
        print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("El producto no existe.")

# Paso 5: Guardar todos los productos actualizados en el archivo
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo actualizado correctamente.")
