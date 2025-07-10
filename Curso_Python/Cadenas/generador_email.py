# Este programa realiza la generacion de un email a partir de los datos de una persona 
print("*** Generador de Emails ***")


# Datos 
nombre = 'Ubaldo Acosta Soto '
empresa = 'Global Mentoring '
dominio = 'com.mx' 

# Proceso 
nombre_minusculas = nombre.lower()
sudcadena_a = nombre_minusculas[0:6]
subcadena_b = nombre_minusculas[7:13]
subcadena_c = nombre_minusculas[14:18]
nombre_normalizado = ''.join([sudcadena_a, '.', subcadena_b, '.',subcadena_c])
print(f'Nombre usuario: {nombre}')
print(f'Nombre usuario normalizado: {nombre_normalizado}')

empresa_minusculas = empresa.lower()
subcadena_d = empresa_minusculas[0:6]
subcadena_e = empresa_minusculas[7:16]
empresa_normalizada = ''.join(['@', subcadena_d, '', subcadena_e, '.', dominio])
email = ''.join([nombre_normalizado, empresa_normalizada])
print(f'\nNombre empresa: {empresa}')
print(f'Extension del dominio: {dominio}')
print(f'Dominio del email normalizado: {empresa_normalizada}')
print(f'\nEmail final generado: {email}')
