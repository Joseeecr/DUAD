precio_producto = int(input("Vamos a calcular el precio de su producto con descuento! Ingrese el precio original "))
if(precio_producto < 100):
    precio_descuento = precio_producto * 0.98
else:
    precio_descuento = precio_producto * 0.90
print(f"El precio final de su producto con descuento aplicado es ${precio_descuento}")