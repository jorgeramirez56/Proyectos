print('*** Generacion Ticket de venta ***')
precio_leche = float(input('Precio de leche: '))
precio_pan = float(input('Precio del pan: '))
precio_lechuga = float(input('Precio de la lecuga: '))
precio_platanos = float(input('Precio de los platanos: '))
descuento = int(input('Ingrese el descuento que guste aplicar (10% / 15%): '))
descuento_normalizado = descuento / 100

# Calculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicando escuento
descuento_aplicado = subtotal * descuento_normalizado

# Subtotal con descuento 
subtotal_con_descuento = subtotal - descuento_aplicado

# Calculo de impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto 

print(f'Subtotal: ${subtotal_con_descuento:.2f}\nDescuento: {descuento}%\nImpuesto (16%): ${impuesto:.2f}\nCosto total de la compra: ${costo_total_compra:.2f}')

