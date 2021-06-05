# 11. Dada una cola con personajes de la saga Star Wars,
# de los cuales se conoce su nombre y planeta 
# de origen. Desarrollar las funciones necesarias para resolver las siguientes
# actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks.
# from cola import Cola
# personaje = Cola()
# cola_aux = Cola()

# class informacion(object):
#     nombre, planeta = '', ''

#     def __init__(self, planeta, nombre):
#             self.nombre = nombre
#             self.planeta = planeta
          

#     def __str__(self):
#           return self.nombre+ '-. Planeta: '+ self.planeta



# dato = informacion ('alderaan','jar jar binks')
# personaje.arribo(dato)
# dato = informacion ('endor','nick fury sinparche' )
# personaje.arribo(dato)
# dato = informacion ('tierra','luke skywalker')
# personaje.arribo(dato)
# dato = informacion ('alderaan', 'arturo')
# personaje.arribo(dato)
# dato = informacion ('desconocido','maestro yoda')
# personaje.arribo(dato)
# dato = informacion ('tatooine', 'droide')
# personaje.arribo(dato)
# dato = informacion ('tatooine','chiwi')
# personaje.arribo(dato)
# dato = informacion ( 'alderaan', 'el tenebroso')
# personaje.arribo(dato)
# dato = informacion ('tierra', 'han solo')
# personaje.arribo(dato)

# cantidad_elemento = 0
# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.mover_final ()
#     print (dato)
#     cantidad_elemento += 1

# print()

###Punto D
# cantidad_elemento = 0

# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.mover_final()
   
#     if (dato.nombre == 'jar jar binks'):
#         dato = personaje.atencion ()
#         print ('personaje ',dato,' eliminado')
#     cantidad_elemento += 1

# print()

# cantidad_elemento = 0
# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.mover_final ()
#     print (dato)
#     cantidad_elemento += 1

###Punto C
# cantidad_elemento = 0
# nuevo_personaje = informacion ( 'marte', 'E-T')
# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.atencion ()
   
#     if (dato.nombre == 'maestro yoda'):
#         personaje.arribo(nuevo_personaje)
    

#     personaje.arribo(dato)
#     cantidad_elemento += 1

# ###Punto A
# cantidad_elemento = 0
# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.mover_final()
#     if ((dato.planeta == 'alderaan') or (dato.planeta == 'endor') or (dato.planeta == 'tatooine')):

#         print ('Personaje ', dato.nombre ,' del planeta ', dato.planeta)
   
#     cantidad_elemento += 1

# print()

# ####Punto B
# cantidad_elemento = 0
# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.mover_final()
#     if ((dato.nombre == 'han solo') or (dato.nombre == 'luke skywalker')):

#         print ('El planeta natal de ', dato.nombre ,' es ', dato.planeta)
#     # else:
#     #     print (dato)

#     cantidad_elemento += 1








# 12.Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una 
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, 
# ni métodos de ordenamiento.

# from cola import Cola
# from random import randint
# cola1 = Cola()
# cola2 = Cola()
# cola_final = Cola()

# lista1 = [1, 6, 10, 25, 34]
# lista2 = [7, 11, 16, 21, 32]

# print ('Para cola 1, agregamos: ')
# for i in (lista1):
#     cola1.arribo(i)
#     print (i)


# print ()

# print ('Para cola 2, agregamos: ')
# for i in (lista2):
#     cola2.arribo(i)
#     print (i)

# print()

# while (not cola1.cola_vacia() and not cola2.cola_vacia()):
# ### comparamos elemento a elemento desde el frente de cada cola con la otra
#     if (cola1.en_frente() < cola2.en_frente()):
#         cola_final.arribo(cola1.atencion())
#     else:
#         cola_final.arribo(cola2.atencion())
# ####si una de las dos colas esta vacia, cargaremos el elemento restante de la otra cola ,a la cola final
#     if (cola1.cola_vacia()):
#         cola_final.arribo(cola2.atencion())
#     if (cola2.cola_vacia()):
#         cola_final.arribo(cola1.atencion())
        
# print ('Cola final')
# cantidad_elemento = 0
# while (cantidad_elemento < cola_final.tamanio()):
#     dato = cola_final.mover_final ()
#     print (dato)
#     cantidad_elemento += 1







# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU),
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe y
# su género (Masculino M y Femenino F) –por ejemplo
# {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, 
# {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superheroes   

from cola import Cola
personaje = Cola()

class persona(object):
    nombre_personaje, nombre_super, genero = '', '', ''

    def __init__(self, nombre_personaje, nombre_super, genero):
            self.nombre_personaje = nombre_personaje
            self.nombre_super = nombre_super
            self.genero = genero
          

    def __str__(self):
          return self.nombre_personaje+': ' + self.nombre_super +'. '+ ' Genero: '+ self.genero

dato = persona ('tony stark', 'iron man', 'm') 
personaje.arribo(dato)
dato = persona ('steve rogers', 'capitan america', 'm')
personaje.arribo(dato)
dato = persona ('thor odinson', 'thor.', ' m')
personaje.arribo(dato)
dato = persona ('sam wilson', 'falcon verde', 'm')
personaje.arribo(dato)
dato = persona ('carol danvers', 'capitana marvel', 'f')
personaje.arribo(dato)
dato = persona ('nati romanoff', 'black widow', 'f')
personaje.arribo(dato)
dato = persona ('wanda maximoff', 'bruja escarlata', 'f')
personaje.arribo(dato)
dato = persona ('stephen strange', 'doctor strange', 'm')
personaje.arribo(dato)
dato = persona ('bruce banner', 'hulk', 'm')
personaje.arribo(dato)
dato = persona ('scott lang', 'ant-man', 'm')
personaje.arribo(dato)


cantidad_elemento = 0
# while (cantidad_elemento < personaje.tamanio()):
#     dato = personaje.mover_final ()
#     print (dato)
#     cantidad_elemento += 1

print ()

cantidad_elemento = 0
while ( cantidad_elemento < personaje.tamanio()):
    dato = personaje.atencion()
    ##punto A
    if (dato.nombre_super == 'capitana marvel'):
        print ('Dato pedido del punto A')
        print (dato.nombre_personaje)

    ##punto B
    if (dato.genero =='f'):
        print ('Dato pedido del punto B')
        print (dato.nombre_super)
    
    ##punto C
    if (dato.genero =='m'):
        print ('Dato pedido del punto C')
        print (dato.nombre_personaje)
    
    ##punto D
    if (dato.nombre_personaje == 'scott lang'):
        print ('Dato pedido del punto D')
        print (dato.nombre_super)
    
    ##Punto E
    if ((dato.nombre_personaje[0] == 's') or (dato.nombre_super[0] == 's')):
        print ('Dato pedido del punto E')
        print ('Nombre empezado por "s"')
        print (dato)
    
    ##punto F
    if (dato.nombre_personaje == 'carol danvers'):
        print ('Dato pedido del punto F')
        print (dato.nombre_super)
   

    personaje.arribo(dato)
    cantidad_elemento +=1