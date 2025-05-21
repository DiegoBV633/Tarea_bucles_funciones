numero = int(input("Ingresa un numero entero positivo: "))
impar = 1
resultado= ""

if numero < 0:
    print("El numero tiene que ser positivo")

while impar <= numero:
    if impar % 2 == 1:
        resultado += str(impar) + ","
    impar += 1

print(resultado.rstrip(", "))



