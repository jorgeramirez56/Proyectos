print("*** Tienda en linea ****")
# Datos
COMPRA_MINIMA = 1000
compra = float(input('Cual fue el monto de tu compra? '))
miembro = input('Eres miembro de la tienda (Si/No): ').lower()
eres_miembro = 'Si'.lower()

if compra > COMPRA_MINIMA and eres_miembro == miembro:
    descuento = compra * 0.10
    monto_descuento = compra - descuento
    print(f'Felicidades has obtenido un descuento del 10%')
    print(f'El monto de tu compra es de: {compra}')
    print(f'El descuento es de: {descuento} ')
    print(f'El monto total con descuento aplicado es de: {monto_descuento}')
elif eres_miembro == miembro: 
    descuento = compra * 0.05
    monto_descuento = compra - descuento
    print(f'Felicidades has obtenido un descuento del 5%')
    print(f'El monto de tu compra es de: {compra}')
    print(f'El descuento es de: {descuento} ')
    print(f'El monto total con descuento aplicado es de: {monto_descuento}')
else: 
    print('No obtuviste ningun descuento')
    print(f'El monto de tu compra es de: {compra}')