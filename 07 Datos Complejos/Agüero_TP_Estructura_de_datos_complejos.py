# Práctico 6: Estructuras de datos complejas
# Objetivo: trabajar con diccionarios en Python

# -----------------------------
# EJERCICIO 1,2,3
# -----------------------------
# 1) Diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario luego de agregar nuevas frutas:")
print(precios_frutas)
print("--------------------------------------------------")

# 2) Actualizar precios de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario luego de actualizar precios:")
print(precios_frutas)
print("--------------------------------------------------")

# 3) Crear una lista solo con las frutas (sin los precios)
frutas = list(precios_frutas.keys())

print("Lista de frutas sin precios:")
print(frutas)

# -----------------------------
# EJERCICIO 4
# -----------------------------

# Crear un diccionario vacío para guardar los contactos
contactos = {}

# Cargar 5 contactos ingresados por el usuario
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    contactos[nombre] = numero  # Guardar en el diccionario

print("Agenda cargada correctamente ")
print("--------------------------------")

# Consultar un número por nombre
consulta = input("Ingresá el nombre del contacto que querés consultar: ")

# Verificar si el nombre existe en el diccionario
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró un contacto con el nombre '{consulta}'.")
    
    
# -----------------------------
# EJERCICIO 5
# -----------------------------   

#Solicita al usuario una frase y muestra:
# - Las palabras únicas (usando un set)
# - Un diccionario con la cantidad de veces que aparece cada palabra

# Pedir al usuario una frase
frase = input("Ingresá una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# Crear un set con las palabras únicas
palabras_unicas = set(palabras)

# Crear un diccionario para contar las repeticiones
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)


# -----------------------------
# EJERCICIO 6
# -----------------------------
#Ingresar los nombres de 3 alumnos y una tupla de 3 notas para cada uno
# Luego, mostrar el promedio de cada alumno

# Crear un diccionario vacío
alumnos = {}

# Cargar los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    # Guardar las notas como una tupla en el diccionario
    alumnos[nombre] = (nota1, nota2, nota3)

print("Promedios de cada alumno:")
print("--------------------------")

# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")
    
    
# -----------------------------
# EJERCICIO 7
# -----------------------------

# Sets de ejemplo con nombres de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Lucas", "María", "Jorge", "Lucía"}
parcial2 = {"Lucas", "María", "Carlos", "Lucía", "Valentina"}

# Estudiantes que aprobaron ambos parciales (intersección)
aprobados_ambos = parcial1 & parcial2
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)

# Estudiantes que aprobaron solo uno de los parciales (diferencia simétrica)
aprobados_solo_uno = parcial1 ^ parcial2
print("Estudiantes que aprobaron solo uno de los parciales:", aprobados_solo_uno)

# Estudiantes que aprobaron al menos un parcial (unión)
aprobados_al_menos_uno = parcial1 | parcial2
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)


# -----------------------------
# EJERCICIO 8
# -----------------------------

# Diccionario inicial de productos y stock
productos = {
    "Manzanas": 10,
    "Bananas": 15,
    "Leche": 20
}

def mostrar_productos():
    print("Productos disponibles:")
    for nombre, stock in productos.items():
        print(f"{nombre}: {stock} unidades")

while True:
    print("\n--- Gestión de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in productos:
            print(f"Stock de {nombre}: {productos[nombre]} unidades")
        else:
            print("El producto no existe.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in productos:
            try:
                unidades = int(input("Ingrese la cantidad a agregar: "))
                productos[nombre] += unidades
                print(f"Nuevo stock de {nombre}: {productos[nombre]} unidades")
            except ValueError:
                print("Por favor ingrese un número válido.")
        else:
            print("El producto no existe.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del nuevo producto: ")
        if nombre in productos:
            print("El producto ya existe.")
        else:
            try:
                stock = int(input("Ingrese la cantidad inicial: "))
                productos[nombre] = stock
                print(f"Producto {nombre} agregado con stock {stock}")
            except ValueError:
                print("Por favor ingrese un número válido.")

    elif opcion == "4":
        mostrar_productos()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intente de nuevo.")
        
        
# -----------------------------
# EJERCICIO 9
# -----------------------------
#Diccionario con claves como tuplas (día, hora) y valores como eventos
# 1. Definición del diccionario de la agenda
agenda = {
    # Clave: Tupla (día, hora) | Valor: Evento
    ("lunes", "10:00"): "Reunión de planificación",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Entrenamiento",
    ("viernes", "14:00"): "Presentación a clientes"
}

# --- Parte para consultar una actividad específica ---

# 2. Definir el día y la hora a consultar
dia_consulta = "jueves"
hora_consulta = "09:30"

# 3. Crear la clave de consulta como una tupla
clave_consulta = (dia_consulta, hora_consulta)

# 4. Consultar la actividad usando .get() para manejar si no hay evento
# .get(clave, valor_por_defecto) devuelve 'No hay actividad programada' si la clave no existe.
actividad = agenda.get(clave_consulta, "No hay actividad programada")

# 5. Imprimir el resultado
print(f"--- Consulta de Agenda ---")
print(f"Día y Hora consultada: {dia_consulta} a las {hora_consulta}")
print(f"Actividad: {actividad}")
    
    
    
# -----------------------------
# EJERCICIO 10
# -----------------------------
    
# Diccionario original (País: Capital)
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Colombia": "Bogotá"
}

# Construye el diccionario invertido usando una comprensión de diccionario
# La sintaxis es: {valor_original: clave_original for clave_original, valor_original in original.items()}
invertido = {capital: pais for pais, capital in original.items()}

# Imprime ambos diccionarios para verificar
print(f"Diccionario Original (País: Capital): {original}")
print("-" * 40)
print(f"Diccionario Invertido (Capital: País): {invertido}")
