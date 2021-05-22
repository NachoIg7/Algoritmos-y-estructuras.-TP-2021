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



pila1 = Pila()
pila2 = Pila()
pila_repetido = Pila()
pila1_aux = Pila()
pila2_aux = Pila()

for i in range (0,5):
    personaje = str(input ('Ingrese personaje del episodio v de star wars: '))
    pila1.apilar(personaje)



for p in range (0,5):
    personaje = str(input ('Ingrese personaje del episodio vii de star wars: '))
    pila2.apilar(personaje)


while(not pila1.pila_vacia):
    if (pila1.elemento_cima() == pila2.elemento_cima()):
        pila_repetido.apilar(pila1.desapilar)
    else:
        pila1_aux.apilar(pila1.desapilar)

while(not pila2.pila_vacia):
    if (pila2.elemento_cima() == pila1_aux.elemento_cima()):
        pila_repetido.apilar(pila2.desapilar)
    else:
        pila2_aux.apilar(pila2.desapilar)

while (not pila_repetido.pila_vacia()):
    print (pila_repetido.desapilar())


















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







#ejercicio 24
#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;[86]
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.