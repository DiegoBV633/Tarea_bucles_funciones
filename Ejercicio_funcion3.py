def area_circulo(radio):
    return 3.14 * radio**2

def volumen_cilindro(altura, radio):
    return altura * area_circulo(radio)

radio = float(input("Ingrese el radio: "))
area = area_circulo(radio)
print ("El area del circulo es:", area)

altura = float(input("Ingrese el altura: "))
volumen = volumen_cilindro(altura, radio)
print ("El volumen del cilindro es:", volumen)