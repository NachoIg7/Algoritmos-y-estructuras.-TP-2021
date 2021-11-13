# 6. Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio 
# 20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:
# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que 
# representa, no más de 20 palabras;
# b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano, 
# pareja, la etiquetas de dichas aristas son estos nombre de relación.
# c. dado el nombre de un dios mostrar los hijos de este;
# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación entre ambos;
# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como 
# camino más corto el que tenga menor número de aristas;
# g. realizar un barrido en profundidad y amplitud de dicho grafo;
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
# i. mostrar todos los ancestros de un determinado dios;
# j. mostrar todos los nietos de Cronos;
# k. mostrar todos los hijos de Tea;
# l. persista los datos del grafo en archivos, uno para los vértices y otro para las aristas.
from grafo import Grafo

# dioses = Grafo()

# file = open ('Datos_dioses.txt', encoding = "utf8")
# lineas = file.readlines()
# lineas.pop(0)
# #primero cargamos los dioses con su genero y descripcion
# for linea in lineas: 
#     dios = linea.split(';')
#     dios_data = {}
#     nombre = dios[0]
#     dios_data['descripcion'] = dios[5]
#     dios_data['genero'] = dios[6]
#     dioses.insertar_vertice(nombre, data = dios_data)

# #cargamos relaciones
# for linea in lineas:
#     dios = linea.split(';')
#     nombre= dios [0]
#     padre = dios [1]
#     madre = dios [2]
#     hermanos = dios [3].split('/')
#     hijos =dios [4].split('/')
#     genero = dios[6]
#     pareja = dios[7].split('/n')[0]

#     if (madre != '-'):
#         dioses.insertar_arista(1, nombre, madre, data = 'hijo/a')
    
#     if (padre != '-'):
#         dioses.insertar_arista(1, nombre, padre, data = 'hijo/a')
    
#     if (hijos[0] != '-'): ### si hay '-' no tiene hijos. Si tiene hijos evaluamos si el dios es hombre o mujer para cargar el genero en su relacion
#         for hijo in hijos:
#             if (genero =='F'):
#                 dioses.insertar_arista(1, nombre, hijo, data = 'madre')
#             else:
#                 dioses.insertar_arista(1, nombre, hijo, data = 'padre')

#     if (hermanos[0] != '-'):
#         for hermano in hermanos:
#             dioses.insertar_arista(1, nombre, hermano, data = 'hermano/a')
    
#     if (pareja != '-'):
#         dioses.insertar_arista(1, nombre, pareja, data = 'pareja')

### Punto C... Hijos de un dios
# nombre_dios = input ('Ingrese el nombre de un dios para conocer sus hijos').capitalize()
# hijos = dioses.hijos_dios(nombre_dios)
# if (hijos == None):
#     print ('dios no cargado')
# elif (not hijos == []):
#         print ('Los hijos de del dios', nombre_dios, ('son: '))
#         for hijo in hijos:
#             print ('°', hijo)
# else:
#     print (nombre_dios, ' no tiene hijos')
# print()  

### Punto D datos de un dios
# nombre_dios = input ('Ingrese el nombre de un dios para conocer su familia: ').capitalize()
# padres, hijos, hermanos = dioses.familia_dios(nombre_dios)
# if (nombre_dios == None):
#     print ('El dios no se encuentra cargado')
# else:
#     print ('La familia de',nombre_dios,':')
#     if (not padres ==[]):
#         print ('Padres:')
#         for padre in padres:
#             print ('°',padre)
#     if (not hermanos == []):
#         print ('Hermanos:')
#         for hermano in hermanos:
#             print ('°',hermano)
#     if (not hijos == []):
#         print ('Hijos:')
#         for hijo in hijos:
#             print ('°',hijo)
# print ()


### Punto E... Realcion entre dos vertices
# print ('Ingrese el nombre de dos dioses para conocer su relacion')
# vertice_origen = input('Nombre del primer dios:').capitalize()
# vertice_destino = input ('Nombre del segundo dios:').capitalize()
# relaciones = dioses.relacion_dioses(vertice_origen, vertice_destino)
# if (not relaciones ==[]):
#     print ('Relacion entre', vertice_origen, 'y', vertice_destino, ':')
#     for relacion in relaciones:
#         print(' - ', vertice_origen, 'es', relacion, 'de', vertice_destino)
# else:
#     print('No existe relacion directa entre los dioses mencionados')

# print()

### Punto F ... Camino mas corto enre dos dioses
# print ('Ingrese el nombre de dos dioses para conocer el camino mas corto')
# dios1 = input('Nombre del primer dios:').capitalize()
# dios2 = input ('Nombre del segundo dios:').capitalize()
# print ()
# ver_origen = dioses.buscar_vertice(dios2)
# ver_destino = dioses.buscar_vertice(dios1)

# camino_corto = dioses.dijkstra(ver_origen, ver_destino)

# destino = dios1
# costo = None

# print ('El camino mas corto es:')
# while(not camino_corto.pila_vacia()):
#     dato = camino_corto.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(' - ', dato[1][0])
#         destino = dato[1][1]

# print('El costo total del camino es', costo)
# print()


###Punto G . Barrido en profundidad y amplitud
# print ('Barrido en profundidad')
# dioses.barrido_profundidad(0)
# print()
# dioses.marcar_no_visitado()
# print ('Barrido en amplitud')
# dioses.barrido_amplitud(0)
# dioses.marcar_no_visitado()
# print()

### Punto H 
# print ('barrido de los dioses y sus madres.')
# dioses.barrido_profundidad_dioses_madres(0)
# dioses.marcar_no_visitado()
# print()

### Punto I .. Ancentros de un dios
# ancestros = []
# nombre_dios = input('Ingrese el nombre de un dios para ver a sus ancestros: ').capitalize()
# dioses.ancestros_dios(nombre_dios, ancestros)
# if (not ancestros == []):
#     print('Ancestros de', nombre_dios)
#     for ancestro in ancestros:
#         print(' - ', ancestro)
# else:
#     print ('No hay informacion sobre los ancestros de', nombre_dios)
# print()

### Punto J.. Nieos de cronos
# print ('Nietos de Cronos:')
# nietos = dioses.nietos_dios('Kronos')
# for nieto in nietos:
#     print (' - ', nieto)
# print()

### Punto K... Hijos de Tea
# print ('Los hijos de Tea son:')
# hijos = dioses.hijos_dios('Theia')
# for hijo in hijos:
#     print (' - ', hijo)
# print()






#16-# Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determinado
# país teniendo en cuenta los siguientes requerimientos:
# a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;
# b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Atenas
# (Partenón), Zeus (Olimpia), Hera (Olimpia), Apollo (Delfos),Poseidón (Sunión), Artemisa
# (Éfeso) y Teatro de Dionisio (Acrópolis)
# c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
# d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
# el templo de Apollo, en Delfos.

templos = Grafo(dirigido=False)

datos_templos = [{'nombre': 'Atenea (Partenon)', 'coordenadas' : {'latitud': '37°58′17″N', 'longitud': '23°43′36″E'}},
                 {'nombre': 'Zeus (Olimpia)', 'coordenadas' : {'latitud': '37°38′16″N', 'longitud': '21°37′48″E'}},
                 {'nombre': 'Hera (Olimpia)', 'coordenadas' : {'latitud': '37°38′20″N', 'longitud': '21°37′47″E'}},
                 {'nombre': 'Apollo (Delfos)', 'coordenadas' : {'latitud': '38°28′56″N', 'longitud': '22°30′05″E'}},
                 {'nombre': 'Poseidón (Sunión)', 'coordenadas' : {'latitud': '37°39′01″N', 'longitud': '24°01′28″E'}},
                 {'nombre': 'Artemisa (Éfeso)', 'coordenadas' : {'latitud': '37°56′59″N', 'longitud': '27°21′50″E'}},
                 {'nombre': 'Dionisio (Acrópolis)', 'coordenadas' : {'latitud': '37°58′13″N', 'longitud': '23°43′40″E'}},
]

for templo in datos_templos:
    templos.insertar_vertice(templo['nombre'], data = templo['coordenadas'])

def cargar_aristas ():
    templos.insertar_arista(303, 'Atenea (Partenon)', 'Zeus (Olimpia)')
    templos.insertar_arista(303, 'Atenea (Partenon)', 'Hera (Olimpia)')
    templos.insertar_arista(164, 'Atenea (Partenon)', 'Apollo (Delfos)')
    templos.insertar_arista(65, 'Atenea (Partenon)', 'Poseidón (Sunión)')
    templos.insertar_arista(482, 'Atenea (Partenon)', 'Artemisa (Éfeso)')
    templos.insertar_arista(0, 'Atenea (Partenon)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(0, 'Zeus (Olimpia)', 'Hera (Olimpia)')
    templos.insertar_arista(242, 'Zeus (Olimpia)', 'Apollo (Delfos)')
    templos.insertar_arista(355, 'Zeus (Olimpia)', 'Poseidón (Sunión)')
    templos.insertar_arista(769, 'Zeus (Olimpia)', 'Artemisa (Éfeso)')
    templos.insertar_arista(294, 'Zeus (Olimpia)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(242, 'Hera (Olimpia)', 'Apollo (Delfos)')
    templos.insertar_arista(355, 'Hera (Olimpia)', 'Poseidón (Sunión)')
    templos.insertar_arista(769, 'Hera (Olimpia)', 'Artemisa (Éfeso)')
    templos.insertar_arista(294, 'Hera (Olimpia)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(224, 'Apollo (Delfos)', 'Poseidón (Sunión)')
    templos.insertar_arista(648, 'Apollo (Delfos)', 'Artemisa (Éfeso)')
    templos.insertar_arista(163, 'Apollo (Delfos)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(432, 'Poseidón (Sunión)', 'Artemisa (Éfeso)')
    templos.insertar_arista(65, 'Poseidón (Sunión)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(484, 'Artemisa (Éfeso)', 'Dionisio (Acrópolis)')

cargar_aristas()

### Punto C.. 
# bosque = templos.prim()
# peso = 0
# print ('Arbol de expansion minimo:')
# for elemento in bosque:
#     print (elemento[1][0], '-', elemento [1][1])
#     peso += elemento [0]
# print ('El costo toal es', peso, 'km')

# print()

### Punto D
lugar1 = 'Atenea (Partenon)'
lugar2 = 'Apollo (Delfos)'
ver_origen = templos.buscar_vertice(lugar1)
ver_destino = templos.buscar_vertice(lugar2)

pila_camino = templos.dijkstra (ver_origen, ver_destino)

destino = lugar2
distancia = None
print ('El camino mas corto es:')
while (not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if (dato[1][0] == destino):
        if (distancia is None):
            distancia = dato[0]
        print (' - ', dato[1][0])
        destino= dato [1][1]

print('La distancia total del camino es de', distancia, 'km.')

