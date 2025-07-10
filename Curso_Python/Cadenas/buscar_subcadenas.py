# Buscar subcadenas 
cadena = "Hola, mundo!"
indice = cadena.find("mundo")

print(f'Indice de la subcadena mundo: {indice}')

# NOTA: Independientemente de cuantas veces aparezca la subcadena mundo, siempre se imprimira  
# el indice del primer caracter en donde encuentre la primera subcadena

# Obtener el indice de la subcadena de Hola 


# como python es sensible a las mayusculas y 
# minisculas no encontrara la subcadena hola
#indice = cadena.find('hola')
#print(f'Indice de la subcadena de Hola {indice}') 


indice = cadena.find('Hola')
print(f'Indice de la subcadena de Hola: {indice}') 

