def calcula_factura(cantidad, iva=21):
    return cantidad + (cantidad * iva / 100)

valor =(input("Ingrese el valor de la factura sin iva: "))
cantidad = float(valor)
valor_iva =(input("Ingrese el iva personalizado (enter para usar 21%) : "))


if valor_iva.strip()=="":
    valor1 = calcula_factura(cantidad)
else:
    iva = float(valor_iva)
    valor1 = calcula_factura(cantidad, iva)

print("El valor con iva seria:", round(valor1))



