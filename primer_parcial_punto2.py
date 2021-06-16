###2. Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, 
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el
# mensaje, resolver las siguientes actividades:
# c. escribir una función que elimine de la cola todas las notificaciones de
# Facebook;
# d. escribir una función que muestre todas las notificaciones de Twitter, cuyo
# mensaje incluya la palabra ‘Python’, si perder datos en la cola;
# e. utilizar una pila para almacenar temporalmente las notificaciones de
# Instagram y mostrar el contenido de dicha pila.
from cola import Cola
from pila import Pila
cola_aplicacion = Cola()
pila_insta = Pila()


class aplicaciones(object):
    nombre, hora_notificacion, mensaje = '', '', ''

    def __init__(self, nombre, hora_notificacion, mensaje):
            self.nombre = nombre
            self.hora_notificacion = hora_notificacion
            self.mensaje = mensaje

    def __str__(self):
          return self.nombre + '-. ' + self.hora_notificacion + ' .- ' + self.mensaje

dato = aplicaciones ('facebook','00:20','juana dio me gusta')
cola_aplicacion.arribo(dato)
dato = aplicaciones ('instagram','17:25','etiqueta en sorteo')
cola_aplicacion.arribo(dato)
dato = aplicaciones ('facebook','09:30','invitacion a juego')
cola_aplicacion.arribo(dato)
dato = aplicaciones ('classroom','15:30','nuevo mensaje en el tablon')
cola_aplicacion.arribo(dato)
dato = aplicaciones ('twitter','18:45','nuevo rtw')
cola_aplicacion.arribo(dato)
dato = aplicaciones ('twitter','19:00','python, nuevo curso gratis')
cola_aplicacion.arribo(dato)
dato = aplicaciones ('instagram','06:30','nuevo mensaje')
cola_aplicacion.arribo(dato)


cantidad_elemento = 0
while (cantidad_elemento < cola_aplicacion.tamanio()):
    dato = cola_aplicacion.mover_final ()
    print (dato)
    cantidad_elemento += 1

print ()

# ##punto a
# cantidad_elemento_puntoa = 0
# while (cantidad_elemento_puntoa < cola_aplicacion.tamanio()):
#     dato = cola_aplicacion.atencion()

#     if (dato.nombre != 'facebook'): 
#         cola_aplicacion.arribo(dato)

#     cantidad_elemento_puntoa += 1


###punto b
# cantidad_elemento_puntob = 0
# while (cantidad_elemento_puntob < cola_aplicacion.tamanio()):
#     dato = cola_aplicacion.mover_final()

#     if ((dato.nombre == 'twitter') and ('python' in dato.mensaje)): 
#         print (dato)

#     cantidad_elemento_puntob += 1

###punto c
# cantidad_elemento_puntoc= 0
# while (cantidad_elemento_puntoc < cola_aplicacion.tamanio()):
#     dato = cola_aplicacion.mover_final()

#     if (dato.nombre == 'instagram'): 
#         pila_insta.apilar(dato)
#     cantidad_elemento_puntoc += 1

# print ('notificaciones de instagram')
# while (not pila_insta.pila_vacia()):
#     aux=pila_insta.desapilar()
#     print(aux)


