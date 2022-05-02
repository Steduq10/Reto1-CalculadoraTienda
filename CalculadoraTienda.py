print("*****************************")
print("    Iniciando Calculadora    ")
print("*****************************")

valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))

iva = input("¿El producto tiene IVA? S/N: ")

if  iva == "S" or iva == "s":
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = (valorUnitario*cantidad) + (cantidad*valorUnitario*0.19)
    print("IVA incluído")
    lista = [subtotal]
    print(f"SUBTOTAL: {subtotal}")
    agregar = input("Faltan productos por agregar? S/N:")
    while agregar == "S" or agregar == "s":
        valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))
        iva = input("¿El producto tiene IVA? S/N: ")
        if iva == "S" or iva == "s":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad) + (cantidad * valorUnitario * 0.19)
            lista.append(subtotal)
            print("IVA incluído")
            subtotal = 0
            for i in lista:
                subtotal += i
            print(f"SUBTOTAL: {subtotal}")
            agregar = input("Faltan productos por agregar? S/N:")
        elif iva == "N" or iva == "n":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad)
            lista.append(subtotal)
            print("PRODUCTO SIN IVA")
            subtotal = 0
            for i in lista:
                subtotal += i
            print(f"SUBTOTAL: {subtotal}")
            agregar = input("Faltan productos por agregar? S/N:")
        else:
            agregar == "N"


elif iva == "N" or iva == "n":
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = (valorUnitario * cantidad)
    lista = [subtotal]
    print("PRODUCTO SIN IVA")
    print(f"SUBTOTAL: {subtotal}")
    agregar = input("Faltan productos por agregar? S/N:")
    while agregar == "S" or agregar == "s":
        valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))
        iva = input("¿El producto tiene IVA? S/N: ")
        if iva == "S" or iva == "s":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad) + (cantidad * valorUnitario * 0.19)
            lista.append(subtotal)
            print("IVA incluído")
            subtotal = 0
            for i in lista:
                subtotal += i
            print(f"SUBTOTAL: {subtotal}")
            agregar = input("Faltan productos por agregar? S/N:")

        elif iva == "N" or iva == "n":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad)
            lista.append(subtotal)
            print("PRODUCTO SIN IVA")
            subtotal = 0
            for i in lista:
                subtotal += i
            print(f"SUBTOTAL: {subtotal}")
            agregar = input("Faltan productos por agregar? S/N:")
        else:
            agregar == "N"


print(f"TOTAL A COBRAR: {subtotal}")
