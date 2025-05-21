
altitud = int(input("Ingrese altitud del arbol: "))
punta_arbol = 1

if altitud < 0:
    print ("Solo numeros positivos")
else:
    while punta_arbol <= altitud:
        espacios = ' ' * (altitud - punta_arbol)
        hojas = '*' * (2 * punta_arbol - 1)
        print(espacios + hojas)
        punta_arbol += 1

    tronco = ' ' * (altitud - 1) + '*'
    print(tronco)