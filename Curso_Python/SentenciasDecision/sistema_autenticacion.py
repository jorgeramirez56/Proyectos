print('**** Sistema de Autenticacion ****')

# Datos 
USUARIO = 'jorge'
PASSWORD = 'LPk427j'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa el password: ')

if USUARIO == usuario and PASSWORD == password:
    print('Bienvenido al sistema')
elif PASSWORD == password:
    print('Usuario invalido')
elif USUARIO == usuario: 
    print('Password invalido')
else: 
    print('Usuario y password invalidos')