from random import randint

print('**** Generador de IDs ****')
nombre = input('\nIngresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
year = input('Ingresa tu año de nacimiento (YYYY): ')

nombre_sub = nombre[0:2]
apellido_sub = apellido[0:2]
year_sub = year[2:] #[2:] asi se refleja que extraera hasta donde termine la cadena

nombre_normalizado = nombre_sub.upper()
apellido_normalizado = apellido_sub.upper()

codigo = randint(1000, 9999)

ID = f'{nombre_normalizado}{apellido_normalizado}{year_sub}{codigo}'

print(f'Hola {nombre} {apellido} \nTu numero de identificacion (ID) generado por el sistema es: {ID} \nFelicidades!!!')
