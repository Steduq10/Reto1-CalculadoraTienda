print("*****************************")
print("    Iniciando Calculadora    ")
print("*****************************")

valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))

iva = input("¿El producto tiene IVA? S/N: ")

if  iva == "S":
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = (valorUnitario*cantidad) + (cantidad*valorUnitario*0.19)
    print(f"SUBTOTAL: {subtotal} (IVA incluido)")
    lista = [subtotal]
    print(lista)
    agregar = input("Faltan productos por agregar? S/N:")
    while agregar == "S":
        valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))
        iva = input("¿El producto tiene IVA? S/N: ")
        if iva == "S":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad) + (cantidad * valorUnitario * 0.19)
            lista.append(subtotal)
            print(f"SUBTOTAL: {subtotal} (IVA incluido)")
            print(lista)
            agregar = input("Faltan productos por agregar? S/N:")
        elif iva == "N":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad)
            lista.append(subtotal)
            print(f"SUBTOTAL: {subtotal} (IVA incluido)")
            print(lista)
            agregar = input("Faltan productos por agregar? S/N:")
        else:
            agregar == "N"


elif iva == "N":
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = (valorUnitario * cantidad)
    lista = [subtotal]
    print(f"SUBTOTAL: {subtotal} (IVA incluido)")
    print(lista)
    agregar = input("Faltan productos por agregar? S/N:")
    while agregar == "S":
        valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))
        iva = input("¿El producto tiene IVA? S/N: ")
        if iva == "S":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad) + (cantidad * valorUnitario * 0.19)
            lista.append(subtotal)
            print(f"SUBTOTAL: {subtotal} (IVA incluido)")
            print(lista)
            agregar = input("Faltan productos por agregar? S/N:")

        elif iva == "N":
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = (valorUnitario * cantidad)
            lista.append(subtotal)
            print(f"SUBTOTAL: {subtotal} (IVA incluido)")
            print(lista)
            agregar = input("Faltan productos por agregar? S/N:")
        else:
            agregar == "N"

print(lista)