def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

elegir = input("Elegir si quiere de decimal a binario (b) o binario a decimal (d): ").strip().lower()

if elegir == "b":
    dec = int(input("Ingrese el número decimal: "))
    dec_resultado = decimal_a_binario(dec)
    print("Número en binario:", dec_resultado)

elif elegir == "d":
    binario = input("Ingrese el número binario: ")
    bin_resultado = binario_a_decimal(binario)
    print("Número en decimal:", bin_resultado)

else:
    print("❌ Opción no válida. Escribe 'b' o 'd'.")

