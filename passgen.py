import string
import random

longitud = int(input("Ingrese el número de caracteres para su contraseña: "))
num = int(input("¿Cuantas contraseñas quiere generar?: "))

caracteres = string.ascii_letters + string.digits + string.punctuation


# se utiliza _ por darle un valor a la variable temporal
for _ in range(num):
    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    print("La contraseña generada es: " + contrasena)
