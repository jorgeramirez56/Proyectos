print('**** Sistema de Calificaciones ****')

calificacion = int(input('Ingresa tu calificacion: '))
if calificacion >= 9 and calificacion <= 10: 
    print('Felicidades, has obtenido una A')
elif calificacion >= 8 and calificacion < 9:
    print('Buen trabajo, obtuviste una B') 
elif calificacion >= 7 and calificacion < 8:
    print('Bien, Obtuviste una C')
elif calificacion >= 6 and calificacion < 7: 
    print('Obtuviste una D')
elif calificacion >= 0 and calificacion < 6:
    print('Echale ganas, has obtenido una F')
else: 
    print('Valor desconocido')
