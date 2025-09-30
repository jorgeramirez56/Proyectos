print('*** Aplicacion de Reserva de hoteles ***')

# Tarifas 
CUARTO_VISTA_MAR = 190.5
CUARTO_SIN_VISTA_MAR = 150.5

# Datos del usuario
nombre_cliente = input('Ingresa tu nombre completo: ')
dias_estadia = int(input('Ingresa los dias de estadia en el hotel: '))
cuarto_vista_mar = input('Cuarto con vista al mar (Si/No): ').lower()

# Condiciones y calclos 
if cuarto_vista_mar == 'si':
    costo_total = dias_estadia * CUARTO_VISTA_MAR
    # print(f'Costo total de la estancia: {costo_total}')
    # print(f'Cuarto con vista al mar: {cuarto_vista_mar}')
else: 
    costo_total = dias_estadia * CUARTO_SIN_VISTA_MAR
    # print(f'Costo total de la estancia: {costo_total}')
    # print(f'Cuarto con vista al mar: {cuarto_vista_mar}')

print('-------------- Detalles de la reservacion ----------')
print(f'Cliente: {nombre_cliente}')
print(f'Dias de estadia: {dias_estadia}')
print(f'Costo Total: {costo_total}')
print(f'Cuarto con vista al mar: {cuarto_vista_mar}')
