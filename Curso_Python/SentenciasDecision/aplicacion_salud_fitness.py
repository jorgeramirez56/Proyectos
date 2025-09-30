print('*** Aplicacion de Salud y Fitness ***')

# Constantes 
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 

# Pedimos los valores al usuario 
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

# Varificar si el usuario alcanzo la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calculamos as calorias quemadas 
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la informacion 
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de paosos diarios es de: {META_PASOS_DIARIOS} pasos')
