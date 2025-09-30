print('*** Sistema de descuentos VIP ***')
NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy? '))
tiene_memesia = input('Tienes la membresia de la tienda (Si/No)? ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO 
                         and tiene_memesia.strip().lower() == 'si')

print(f'Tienes acceso al descuento VIP? {es_elegible_descuento}')