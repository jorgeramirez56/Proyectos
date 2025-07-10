print('*** Sistema de empleados ***')
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('Es jefe departamento (si/no)? ')

# Vamos a convetir a un tipo bool la variable es_jefe_departamento 
es_jefe_departamento = es_jefe_departamento.lower() == 'si'


# Imprimir los valores del empleado 
print('\nDtos del empleo')
print(f'Nombre: {nombre_empleado}')
print(f'Edad : (edad empleado)')
print(f'salario: {salario_empleado:.2f}')
print(f'Es jefe de Departamento? {es_jefe_departamento}')

