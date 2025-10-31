#Práctico 11: Aplicación de la Recursividad 

#Ejercicios

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 

# Función que muestra el factorial de todos los números entre 1 y el número dado por el usuario
def mostrar_factoriales():
    num = int(input("Ingrese un número: "))
    for i in range(1, num + 1):
        print(f"El factorial de {i} es {factorial(i)}")

mostrar_factoriales()

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

# Función recursiva para calcular el valor de Fibonacci en la posición n
def fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1:  
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

# Función que muestra la serie completa de Fibonacci hasta la posición indicada por el usuario
def mostrar_fibonacci():
    num = int(input("Ingrese un número: "))
    for i in range(num):
        print(f"F({i}) = {fibonacci(i)}")

mostrar_fibonacci()

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1). Prueba esta función en un algoritmo general.

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:  
        return 1
    else:
        return base * potencia(base, exponente - 1) 

# Función para probar la potencia
def mostrar_potencia():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

mostrar_potencia()

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
#procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:  # si el número es 0, retornamos una cadena vacía
        return ''
    else:
        # dividir el número por 2 y agregar el resto
        return decimal_a_binario(n // 2) + str(n % 2)

# Función principal que maneja el caso cuando el número es 0
def convertir_a_binario(n):
    if n == 0:
        return '0'  #para el 0, ya que su representación binaria es "0"
    else:
        return decimal_a_binario(n)


numero = int(input("Ingrese un número decimal: "))
print(f"El número {numero} en binario es: {convertir_a_binario(numero)}")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Si el primer y el último carácter son iguales, verificamos la subcadena interior
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False  # Si no coinciden, no es un palíndromo


palabra = input("Ingrese una palabra: ").lower()
print(es_palindromo(palabra)) 

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    # si el número es 0, la suma es 0
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)  # Sumar el último dígito y llamar recursivamente


numero = int(input("Ingrese un número entero positivo: "))
print(suma_digitos(numero))


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.

def contar_bloques(n):
    # si n es 1, devuelve 1
    if n == 1:
        return 1
    else:
        # Sumar los bloques del nivel actual con los bloques del resto de la pirámide
        return n + contar_bloques(n - 1)

print(contar_bloques(1)) 
print(contar_bloques(2)) 
print(contar_bloques(4))  


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # si el número es 0, hemos terminado
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito es igual al dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)  # Incrementamos el contador y llamamos recursivamente
        else:
            return contar_digito(numero // 10, digito)  # Solo llamamos recursivamente sin incrementar el contador

print(contar_digito(12233421, 2))  
print(contar_digito(5555, 5))     
print(contar_digito(123456, 7))   