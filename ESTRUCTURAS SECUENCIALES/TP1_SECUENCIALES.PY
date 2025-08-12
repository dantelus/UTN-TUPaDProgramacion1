#TP1 SECUENCIALES - ALUMNO DANTE CARUSO

#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = input("Ingrese su edad: ")
Lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Lugar_de_residencia}")

#Ejercicio 4
radio = float(input("Ingrese el radio del circulo: "))
area = round(3.14159 * (radio**2),2)
perimetro = round(2 * 3.14159 * radio, 2)
print("El area del circulo es: ", area)
print("El perimetro del circulo es: ", perimetro)

#Ejercicio 5
segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))
horas = round(segundos_ingresados / 3600, 2)
print(f"{segundos_ingresados} segundos equivale a {horas} horas!")

#Ejercicio 6
numero = int(input("Ingrese un numero entero: "))
uno = numero * 1
dos = numero * 2
tres = numero * 3 
cuatro = numero * 4
cinco = numero * 5 
seis = numero * 6
siete = numero * 7
ocho = numero * 8 
nueve = numero * 9 
diez = numero * 10 
print(f"La tabla de multiplicar del numero {numero}: ")
print(f"{numero} * 1 = {uno}")
print(f"{numero} * 2 = {dos}")
print(f"{numero} * 3 = {tres}")
print(f"{numero} * 4 = {cuatro}")
print(f"{numero} * 5 = {cinco}")
print(f"{numero} * 6 = {seis}")
print(f"{numero} * 7 = {siete}")
print(f"{numero} * 8 = {ocho}")
print(f"{numero} * 9 = {nueve}")
print(f"{numero} * 10 = {diez}")

#Ejercio 7
print("INGRESE DOS NUMERO ENTEROS DISTINTOS DEL CERO")
a = float(input("Primer numero: "))
b = float(input("segundo numero: "))
suma = a + b
resta = a - b
division = round(a / b,2)
multiplicacion = a * b
print(f"""
        La suma de los dos numeros es: {suma}
        La resta de los dos numeros es: {resta}
        La division de los dos numeros es: {division}
        La multiplicacion de los dos numeros es: {multiplicacion}
        """)

#Ejercicio 8
print("Indice de masa corporal")
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = round(peso/(altura*altura),2)
print("Su indice de masa corporal es de ", imc)

#Ejercicio 9 
grados_celsius = float(input("Ingrese grados celsius: "))
grados_fahrenheit = round(grados_celsius * 1.8 + 32, 2)
print(f"{grados_celsius} grados celsius equivale a {grados_fahrenheit} grados fahrenheit")

#Ejercicio 10
a = float(input("Ingrese primer numero: "))
b = float(input("Ingrese segundo numero: "))
c = float(input("Ingrese tercer numero: "))
promedio = round((a+b+c)/3, 2)
print(f"El promedio de los numeros ingresados es: {promedio} ")


#
