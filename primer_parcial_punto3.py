# 3. Dada una lista con nombres de personajes de la saga de Avengers, resolver las
# siguientes tareas:
# a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
# misma;
# b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
# c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
# ‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
# cargados. 
# d. Realizar un barrido ascendente y descendente de la lista. 
# e. Mostrar la información del personaje en la posición 7. 
# f. Mostrar todos los personajes que comienzan con C o S. 
# g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
# booleano que indica si es héroe True villano False), luego realizar un barrido
# ordenado por nombre y otro por año de aparición. Deberá cargar toda la
# información de nuevo.



from lista import Lista
lista_personaje=Lista()



lista1 = [
        {'name': 'Dr. Strange','Año de aparicion': 1945, 'Heroe': True},
        {'name': 'Black Panther','Año de aparicion': 1946, 'Heroe': True},
        {'name': 'Capitana Marvel','Año de aparicion': 1970, 'Heroe': True},
        {'name': 'Star-Lord','Año de aparicion': 1970, 'Heroe': True},
        {'name': 'Iron man','Año de aparicion': 1929, 'Heroe': True},
        {'name': 'Thor','Año de aparicion': 500, 'Heroe': True},
        {'name': 'Thanos','Año de aparicion': 845, 'Heroe': False},
        {'name': 'Scalet Witch','Año de aparicion': 1960, 'Heroe': True},
     ]
for personaje in lista1:
    lista_personaje.insertar(personaje,'name')


lista_auxiliar = [
        {'name': 'Black Widow','Año de aparicion': 1989, 'Heroe': True},
        {'name': 'Hulk','Año de aparicion': 1939, 'Heroe': True},
        {'name': 'Rocket Racoonn','Año de aparicion': 1950, 'Heroe': True},
        {'name': 'Loki','Año de aparicion': 500, 'Heroe': False},
     ]

for personaje in lista_auxiliar:
    lista_personaje.insertar(personaje,'name')

lista_personaje.barrido()
print()

# #punto a
# pos = lista_personaje.busqueda('Thor','name')
# if (pos != -1):
#    print('Thor esta en la posicion: ', pos,' de la lista')
# print()

###punto b
# pos2 = lista_personaje.busqueda('Scalet Witch','name')
# if (pos2 != -1):
#     lista_personaje.obtener_elemento(pos2)['name'] = 'Scarlet Witch'
# print()

###punto d 
# print ('Barrido ascendente')
# lista_personaje.barrido()
# print ()
# print ('Barrido descendente')
# for i in range(lista_personaje.tamanio()-1, -1 ,-1):
#     aux = lista_personaje.obtener_elemento(i)
#     print (aux)


###punto e
# for i in range(lista_personaje.tamanio()):
#     aux = lista_personaje.obtener_elemento(i)
#     if (i == 7):
#         print ('Personaje en la posicion 7')
#         print (aux['name'])
# print()

###punto f
# print ('Personajes que comiencen con la letra "C" o "S"')
# for i in range(lista_personaje.tamanio()):
#     aux = lista_personaje.obtener_elemento(i)

#     if (((aux['name'])[0] == 'C') or ((aux['name'])[0] == 'S')):
#         print (aux['name'])

###punto g
# print ('Lista ordenada por nombre')
# lista_personaje.barrido()
# print ()

# print ('Lista ordenada por año de aparicion')
# lista_personaje.ordenar('Año de aparicion')
# lista_personaje.barrido()

