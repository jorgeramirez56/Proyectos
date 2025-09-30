print('*** Valor dentro de Rango ***')
VALOR_MINIMO = 0 
VALOR_MAXIMO = 5 

# Solicitando un valor entre 0 y 5 
valor = int(input('Ingresa un valor: '))

# valor_dentro_rango = valor >= 0 and valor <= 5
valor_dentro_rango = 0 <= valor <= 5
print(f'El valor esta dentro del rango de 0 a 5? {valor_dentro_rango}')