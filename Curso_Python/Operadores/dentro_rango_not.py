# Revisar si una variale se encuentra dentro de rango de 1 a 10
dato = int(input('Proporcione un dato entero: '))

# Revisamos si esta dentro de rango 
esta_dentro_rango = 1 <= dato <= 10
print(f'Variable esta dentro de rango (1 a 10)? {esta_dentro_rango}')

# Revisamos la logica inversa, si el dato esta fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f'Variable esta fuera de rango (entre 1 y 10)? {esta_fuera_rango}')