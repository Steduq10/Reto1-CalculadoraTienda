print("*****************************")
print("    Iniciando Calculadora    ")
print("*****************************")

valorUnitario = int(input("Por favor, ingrese el valor unitario del producto (sin IVA incluido): "))

iva = input("¿El producto tiene IVA? S/N: ")

while iva == "S":
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = (valorUnitario*cantidad) + (cantidad*valorUnitario*0.19)
    print(f"SUBTOTAL: {subtotal} (IVA incluido)")
    
while iva == "N":
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = (valorUnitario * cantidad)
    print(f"SUBTOTAL: {subtotal} (PRODUCTO SIN IVA)")
