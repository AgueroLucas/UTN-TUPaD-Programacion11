#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe 
# imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) 
# para realizar la impresión por pantalla.

nombre="Lucas"

print(f"Hola {nombre}, felicidades por completar el desafio #2 ")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre= input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")   
edad=int(input("Ingrese su edad:"))
departamento=input("En que departamento vive:")

print(f"Hola {nombre} {apellido}, tienes {edad} años de edad y vives en el departamento de {departamento} ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio del círculo: "))

PI = 3.14
P = 2 * PI * radio
A = PI * (radio ** 2)

print(f"El área del círculo es de {A}, y su perímetro es {P}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos=float(input("Ingrese cantidad de segundos deseada:"))

hora= segundos / 3600

print(f"Las horas equivalentes son: {hora}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero=int(input("Ingrese un numero: "))

for i in range(1 , 11):
    resultado = numero * i
    print(f" {numero} x {i} = {resultado}")
    

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1=int(input("Ingrese un numero 1 distindo de cero: "))
numero2=int(input("Ingrese un numero 2 distindo de cero: "))

suma= numero1+numero2
division= numero1/numero2
multiplicacion= numero1*numero2
resta= numero1-numero2

print(f"La suma es: {suma} , la division es: {division}, la multiplicacion es: {multiplicacion}, la resta es: {resta} ")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente

altura=float(input("Ingrese su altura:"))
peso=float(input("Ingrese su peso: "))

imc=altura/(peso)**2

print(f"El indice de masa corporal es de: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

Celsius=float(input("Ingrese grados Celsius a transformar: "))

fahrenheit= (9/5*Celsius )+ 32


print(f"Los grados Fahrenheit son: {fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero1=int(input("Ingrese el primer numero : "))
numero2=int(input("Ingrese el segundo numero : "))
numero3=int(input("Ingrese el tercer numero : "))


promedio=(numero1+numero2+numero3)/3

print(f"El promedio de los tres numeros es: {promedio}")