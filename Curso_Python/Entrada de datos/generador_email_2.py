from random import randint
print("Sistema generador de Emails")
nombre = input('Ingresa tu nombre(s): ')
apellidos = input('Ingresa tus apellidos: ')
empresa = input('Ingresa el nombre de tu empresa: ')
extension_dominio = input('Ingresa la extension del dominio (ejemplo: .com.mx): ')

# Normalizando los datos
nombre_normalizado = nombre.strip()
nombre_normalizado = nombre_normalizado.replace(' ','.')
nombre_normalizado = nombre_normalizado.lower()

apellidos_normalizado = apellidos.strip()
apellidos_normalizado = apellidos_normalizado.replace(' ','.')
apellidos_normalizado = apellidos_normalizado.lower()

empresa_normalizado = empresa.strip()
empresa_normalizado = empresa_normalizado.replace(' ','')
empresa_normalizado = empresa_normalizado.lower()

dominio = f'@{empresa_normalizado}'

#Generando el Email 
email = f'{nombre_normalizado}.{apellidos_normalizado}{dominio}{extension_dominio}'
print(f'Felicidades\nTu email generado es: {email}')

