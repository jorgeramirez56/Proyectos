print('**** Sistema de envios ****')

## Constantes
ENVIO_NACIONAL = 10
ENVIO_INTERNACIONAL = 20

envio_nacional = 'nacional'
envio_internacional = 'internacional'

destino = input('Tu envio sera Nacional o Internacional: ').strip().lower()
peso = float(input('Cuanto pesa tu envio en Kg? '))

if envio_nacional == destino: 
    costo = peso * ENVIO_NACIONAL
elif envio_internacional == destino:
    costo = peso * ENVIO_INTERNACIONAL
else:
    print('Error, vuelve a intentarlo') 
    

print(f'Tipo de envio: {destino}')
print(f'Peso o masa de tu envio en Kg: {peso}')
print(f'El costo de tu envio es de: {costo}')


