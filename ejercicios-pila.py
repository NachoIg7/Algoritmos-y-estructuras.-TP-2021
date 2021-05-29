# Realizar un algoritmo que permita ingresar elementos en una pila,
#  y que estos queden ordenados de forma creciente.
#  Solo puede utilizar una pila auxiliar como estructura extra –no se 
# pueden utilizar métodos de ordenamiento–

from pila import Pila
from random import randint

# pila_datos = Pila()
# pila_aux = Pila()
# num=int


# for i in range (0,5):
#     num =  int(input('ingrese numero para agregar a la pila: '))
#     if pila_datos.pila_vacia() or (num >= pila_datos.elemento_cima()): 
#             pila_datos.apilar(num)
#             print ( "numero cargado")
#     else:
#         while (not pila_datos.pila_vacia() and num < pila_datos.elemento_cima()):  
#             pila_aux.apilar(pila_datos.desapilar())
#         pila_datos.apilar(num)
#         print ( "numero cargado")

#         while (not pila_aux.pila_vacia()):
#             pila_datos.apilar(pila_aux.desapilar())

# while (not pila_datos.pila_vacia()):
#     print (pila_datos.desapilar())


  
    
















#ejercicio 16
#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire 
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que 
#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.



# pila1 = Pila()
# pila2 = Pila()
# pila_repetido = Pila()
# pila1_aux = Pila()

# #Cargamos personajes pila 1
# pila1.apilar('enano verde')
# pila1.apilar('chiwi')
# pila1.apilar('arturo')

# #Cargamos personajes pila 2
# pila2.apilar('droide')
# pila2.apilar('tenebroso')
# pila2.apilar('enano verde')


    


# while(not pila1.pila_vacia()):
#     aux=pila1.desapilar()
#     if ( aux == pila2.elemento_cima()):
#         pila_repetido.apilar(aux)
#         pila2.desapilar()
#         print ('personaje repetido cargado')
#     else:
#         pila1_aux.apilar(aux)
#         print ('no hay coincidencia')

# while(not pila2.pila_vacia() and not pila1_aux.pila_vacia()):
#     aux=pila2.desapilar()
#     if (aux == pila1_aux.elemento_cima()):
#         pila_repetido.apilar(aux)
#         print ('personaje repetido cargado')
#     else:
    
#         print ('no hay coincidencia')

# while (not pila_repetido.pila_vacia()):
#     print (pila_repetido.desapilar())


















#ejercicio 22
#Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The 
#Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada 
#misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó, 
# #costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
# de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos 
# quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la 
# que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

# class Bitacora(object):
#     planeta, capturado, recompensa = '', '', float

#     def __init__(self, planeta, capturado, recompensa):
#          self.planeta = planeta
#          self.capturado = capturado
#          self.recompensa = recompensa

#     def __str__(self):
#          return self.planeta+' - '+self.capturado+' - '+self.recompensa

# boba = Pila()
# djarin = Pila()

# #cargamos bitacora de Boba Fett

# dato = Bitacora ('tierra','han solo',10000000)
# boba.apilar(dato)
# dato = Bitacora ('rojo','droide',200)
# boba.apilar(dato)
# dato = Bitacora ('azul','enano verde',10)
# boba.apilar(dato)
# dato = Bitacora ('mercurio','asesino',5542)
# boba.apilar(dato)


# #cagamos bitacora de Din Djarin
# dato = Bitacora ('257','soldado',4478)
# djarin.apilar(dato)
# dato = Bitacora ('900','luke',845600)
# djarin.apilar(dato)
# dato = Bitacora ('7882','lela',420)
# djarin.apilar(dato)


# contador_capturas_boba = 0
# contador_capturas_djarin = 0
# captura = False
# num_mision = 0
# cont_mision = 0
# mision_captura = 0
# acum_boba = float
# acum_djarin = float

# print ('Planetas visitados por Boba Fett')
# acum_boba = 0
# while (not boba.pila_vacia()):
#     x = boba.desapilar()
#     contador_capturas_boba = contador_capturas_boba + 1
#     cont_mision = cont_mision + 1
#     acum_boba = acum_boba + x.recompensa
#     print (x.planeta)
        

#     if (x.capturado == 'han solo'):
#         captura = True
#         mision_captura = cont_mision

# print ('En total realizo ' + str(contador_capturas_boba) + ' capturas')

# print ('Recaudó ' + str(acum_boba) + ' creditos galacticos')


# print ('Planetas visitados por Din Djarin')
# acum_djarin = 0
# while (not djarin.pila_vacia()):
#     x = djarin.desapilar()
#     contador_capturas_djarin = contador_capturas_djarin + 1
#     acum_djarin = acum_djarin + x.recompensa
#     print (x.planeta)

# print ('En total realizo ' + str(contador_capturas_djarin) + ' capturas')

# print ('Recaudó ' + str(acum_djarin) +  ' creditos galacticos')

# if (acum_boba > acum_djarin):
#     print ('El mercenario Boba Fett acumulo mas creditos galacticos')
# else:
#     print ('El mercenario Din Djarin acumulo mas creditos galacticos')

# if (captura):
#     print ('Boba Fett capturo a han solo en la mision ' + str(mision_captura))




#ejercicio 24
#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

class Personaje (object):
        nombre, cant_peliculas = '' , int
        
        def __init__(self, nombre, cant_peliculas):
            self.nombre = nombre
            self.cant_peliculas = cant_peliculas
        
        def __str__(self):
            return self.nombre + '-' +self.cant_peliculas

personaje = Pila()

dato = Personaje ('iron man', 6)
personaje.apilar(dato)
dato = Personaje ('capitan america', 5)
personaje.apilar(dato)
dato = Personaje ('hulk', 9)
personaje.apilar(dato)
dato = Personaje ('hormiga', 3)
personaje.apilar(dato)
dato = Personaje ('black widow', 4)
personaje.apilar(dato)
dato = Personaje ('groot', 5)
personaje.apilar(dato)
dato = Personaje ('rocket raccoonn', 5)
personaje.apilar(dato)
dato = Personaje ('thor', 6)
personaje.apilar(dato)
dato = Personaje ('pantera', 3)
personaje.apilar(dato)
dato = Personaje ('fury', 20)
personaje.apilar(dato)
dato = Personaje ('thanos', 2)
personaje.apilar(dato)
dato = Personaje ('ford falcon', 1)
personaje.apilar(dato)


cont_posicion = 0  

while (not personaje.pila_vacia()):
    x = personaje.desapilar()
    cont_posicion = cont_posicion + 1

    if (x.nombre == 'rocket raccoonn'):
        print ('rocket raccoonn esta en la posicion ' + str(cont_posicion))
    if (x.nombre == 'groot'):
        print ('groot esta en la posicion ' + str(cont_posicion)) 

    if (x.cant_peliculas >= 5):
        print (x.nombre + ', participo en mas de 5 peliculas. En total: ' + str(x.cant_peliculas))   

    if (x.nombre == 'black widow'):
        print ('black widow participo en ' + str(x.cant_peliculas) + ' peliculas' )

    if (x.nombre[0] == 'c' or x.nombre[0] == 'd' or x.nombre[0] == 'g'):
        print ('personaje comenzado con letra c,d o g ')
        