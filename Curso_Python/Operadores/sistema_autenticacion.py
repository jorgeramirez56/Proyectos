print('*** Sistema de Autenticacion ***')
USUARIO = 'jorge56'
PASSWORD = '270502'
usuario = input('Ingresa el nombre de usuario: ')
password = input('Ingresa el password: ')

resultado = usuario.strip() == USUARIO and password.strip() == PASSWORD
print(f'Datos correctos? {resultado}')