# Valores aleatorios con la funcion randint()

# 2 formas de importar: 
# import random
# from random import randint

from random import randint

# Generar un numero aleatorio entre 1 y 10
numero = randint(1, 10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

# Simular un dado de seis caras 
dado = randint(1, 6)
print(f'El resultado de lanzar el dado es: {dado}')

