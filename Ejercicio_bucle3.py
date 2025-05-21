contraseña_correcta = "Hola123"

intento = 0
contraseña = ""

while contraseña != contraseña_correcta:
    contraseña = input("Ingresa una contraseña: ")
    intento += 1

print("Contrseña correcta. Tu numero de intentos fue:", intento)