
# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, 
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar
#  las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.
from lista import Lista
# lista_super=Lista()

# datos = [
#         {'name':'Wolverine','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
#         {'name':'Linterna Verde','aparicion': 1970, 'casa de comic' : 'MARVEL', 'biografia': 'linterna'},
#         {'name':'Dr. Strange','aparicion': 1978, 'casa de comic' : 'DC', 'biografia': 'traje'},
#         {'name': 'Black Panther','aparicion':1970, 'casa de comic' : 'MARVEL', 'biografia': 'armadura'},
#         {'name':'Capitana Marvel','aparicion': 1976, 'casa de comic' : 'MARVEL', 'biografia': 'traje'},
#         {'name':'Mujer Maravilla','aparicion': 1998, 'casa de comic' : 'DC', 'biografia': 'capa'},
#         {'name':'Flash','aparicion': 1999, 'casa de comic' : 'MARVEL', 'biografia': 'rapidez'},
#         {'name':'Star-Lord','aparicion': 1991, 'casa de comic' : 'MARVEL', 'biografia': 'lord'},
#         {'name': 'Iron man','aparicion':1940, 'casa de comic' : 'MARVEL', 'biografia': 'armadura'},
#      ]

# for personas in datos:
#     lista_super.insertar(personas,'name')

# lista_super.barrido()
# print()
##punto a
# print('elemento eliminado', lista_super.eliminar('Linterna Verde', 'name'))
# print()

##punto b
# pos = lista_super.busqueda('Wolverine','name')
# if (pos != -1):
#    print('Wolverine aparecio en el año: ', lista_super.obtener_elemento(pos)['aparicion'])

##puntoc
# pos2 = lista_super.busqueda('Dr. Strange','name')
# if (pos2 != -1):
#     lista_super.obtener_elemento(pos2)['casa de comic'] = 'Marvel'
# print()
# lista_super.barrido()

 ##punto d
# for i in range(lista_super.tamanio()):
#     aux = lista_super.obtener_elemento(i)
#     bus_traje = aux['biografia']
#     if (('traje' in bus_traje) or ('armadura' in bus_traje)):
#         print ('El personaje ',aux['name'],' tiene ', aux['biografia'])

##punto e
# print ('personajes que aparecieron antes el año 1963')
# for i in range (lista_super.tamanio()):
#     aux = lista_super.obtener_elemento(i)
#     if (aux['aparicion'] < 1963):
#         print (aux['name'],'--',aux['casa de comic'])

###punto f
# for i in range (lista_super.tamanio()):
#     aux = lista_super.obtener_elemento(i)
#     if ((aux['name'] == 'Capitana Marvel') or (aux['name'] == 'Mujer Maravilla')):
#         print ('El personaje ',aux['name'],', pertenece a la casa de ', aux['casa de comic'])
   
##punto g

# for i in range (lista_super.tamanio()):
#     aux = lista_super.obtener_elemento(i)
#     if ((aux['name'] == 'Flash') or (aux['name'] == 'Star-Lord')):
#         print (aux)

#punto h 
# for i in range (lista_super.tamanio()):
#     aux = lista_super.obtener_elemento(i)
#     if (((aux['name'])[0] == 'B') or ((aux['name'])[0] == 'M') or ((aux['name'])[0] == 'S')):
#         print (aux['name'])

##punto I
# cont_marvel = 0
# cont_dc = 0
# for i in range(lista_super.tamanio()):

#     aux = lista_super.obtener_elemento(i)
#     if (aux['casa de comic'] == 'MARVEL'):
#         cont_marvel += 1
#     if (aux['casa de comic'] == 'DC'):
#         cont_dc += 1

# print (cont_marvel, ' personaje/s de marvel')
# print (cont_dc, ' personaje/s de DC')














#7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;[113]
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido


# lista1 = Lista()
# lista2 = Lista()
# lista_concatenada= Lista()

# for i in range (0,10):
#     lista1.insertar(i)

# for i in range (0,10):
#     lista2.insertar(i*2)

# for i in range (lista1.tamanio()):
#     lista_concatenada.insertar(lista1.obtener_elemento(i))

# for i in range (lista2.tamanio()):
#     lista_concatenada.insertar(lista2.obtener_elemento(i))

# # print ('Listas concatenadas: ')
# # lista_concatenada.barrido()
# # print()

# cont_repetido = 0
# for i in range (lista2.tamanio()):
#     elemento = lista2.obtener_elemento(i)
#     pos = lista1.busqueda(elemento)
#     if pos == -1:
#         lista1.insertar(elemento)
#     else:
#         cont_repetido +=1

# print ('Listas concatenadas sin valores repetidos: ')
# lista1.barrido()
# print()

# print('Cantidad de calores repetidos en ambas listas: ', cont_repetido)

# for i in range (lista1.tamanio()):
#     while i < lista1.tamanio():
#         print (lista1.eliminar(lista1.obtener_elemento(i)))




# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;[115]
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
# deberán mostrar los datos de ambos


# entrenadores = Lista()
# pokemones = Lista()
# entrenadores_79 = Lista() #punto e
# lista_tipos = Lista() #punto f 

# file = open('entrenadores.txt')
# file2 = open('pokemones.txt')


# lineas = file.readlines()
# lineas.pop(0)

# for linea in lineas:
#     entrenador = linea.split(';')
#     entrenador_data = {}
#     entrenador_data['Nombre'] = entrenador[0]
#     entrenador_data['Torneos'] = int(entrenador[1])
#     entrenador_data['Perdidas'] = int(entrenador[2])
#     entrenador_data['Ganadas'] = int(entrenador[3])
#     entrenador_data['ID'] = int(entrenador[4].split('\n')[0])
#     entrenador_data['Pokemones'] = Lista()
#     entrenadores.insertar(entrenador_data, 'Nombre')

# lineas = file2.readlines()
# lineas.pop(0)

# for linea in lineas:
#     pokemon = linea.split(';')
#     pokemon_data = {}
#     pokemon_data['Nombre'] = pokemon[0]
#     pokemon_data['Nivel'] = int(pokemon[1])
#     pokemon_data['Tipo'] = pokemon[2]
#     pokemon_data['Subtipo'] = pokemon[3]
#     pokemon_data['ID'] = int(pokemon[4].split('\n')[0])
#     pokemones.insertar(pokemon_data, 'ID')

# for i in range (entrenadores.tamanio()):
#     id_entrenador = entrenadores.obtener_elemento(i)['ID']
#     for j in range (pokemones.tamanio()):
#         id_pokemon = pokemones.obtener_elemento(j)['ID']
#         if (id_entrenador == id_pokemon):
#             entrenadores.obtener_elemento(i)['Pokemones'].insertar(pokemones.obtener_elemento(j), 'Nombre')

# def mostrar_datos (lista, pos): #Muestra datos de entrenadoras y sus pokemones
#     entrenador = lista.obtener_elemento(pos)
#     print ('°', entrenador ['Nombre'])
#     print ('Torneos ganados:',entrenador['Torneos'], ' -Batallas perdidas:',entrenador['Perdidas'], ' -Batallas ganadas: ', entrenador['Ganadas'])
#     print ('Pokemones:')
#     for j in range (0, entrenador['Pokemones'].tamanio()):
#         pokemones = lista.obtener_elemento(pos)['Pokemones']
#         print (pokemones.obtener_elemento(j)['Nombre'], '-Nivel: ', pokemones.obtener_elemento(j)['Nivel'], '- Tipo: ', pokemones.obtener_elemento(j)['Tipo'], '-Subtipo: ', pokemones.obtener_elemento(j)['Subtipo'])

# for i in range (entrenadores.tamanio()):
#     mostrar_datos(entrenadores, i)
#     print ()


# #Punto A
# nombre = input ('Ingrese el nombre del entrenador para saber la cantidad de pokemon que posee: ').capitalize() #Hace mayusculas la primer letra de la palabra
# pos = entrenadores.busqueda(nombre, 'Nombre')
# if pos != -1:
#     print (nombre, ' posee', entrenadores.obtener_elemento(pos)['Pokemones'].tamanio())
# print()

# #Punto B
# mas_torneos = entrenadores.obtener_elemento(0)
# print ('Entrenadores que ganaron mas de tres torneos: ')

# for i in range (entrenadores.tamanio()):
#     entrenador= entrenadores.obtener_elemento(i)
#     lista_pokem = entrenador['Pokemons']
#     if (entrenador['Torneos'] > 3):
#         print (entrenador['Nombre'],' ganó', entrenador ['Torneos'], ' torneos')

#     if entrenador['Torneos'] > mas_torneos['Torneos']:
#         mas_torneos = entrenador

#     if (entrenador ['Ganadas'] * 100 // (entrenador['Perdidas'] + entrenador['Ganadas']) > 79):
#         entrenadores_79.insertar(entrenador, 'Nombre') 

#     for j in range (lista_pokem.tamanio()):
#         pokemon = lista_pokem.obtener_elemento(j)
#         if ((pokemon['Tipo'] == 'Fuego' and pokemon['Subtipo'] == 'Planta') or (pokemon['Tipo'] == 'Agua' and pokemon['Subtipo']== 'Volador')):
#             lista_tipos.insertar(entrenador, 'Nombre')  

# print()

# #Punto C
# lista_pokem = mas_torneos['Pokemones']
# mayor_nivel = lista_pokem.obtener_elemento(0)
# for i in range(lista_pokem.tamanio()):
#     if (lista_pokem.obtener_elemento(i)['Nivel'] > mayor_nivel['Nivel']):
#         mayor_nivel = lista_pokem.obtener_elemento(i)

# #Punto D
# entr = input ('Ingrese el nombre de entrenador para conocer sus datos y sus pokemon').capitalize()
# pos = entrenadores.busqueda(entr, 'Nombre')
# if (pos != -1):
#     mostrar_datos(entrenadores, pos)
#     print()

# #Punto E
# print('Entrenadores con win rate mayor a 79%: ')
# for i in range (entrenadores_79.tamanio()):
#     print (entrenadores_79.obtener_elemento(i)['Nombre'])

# print()

# #Punto F
# print('Entrenadores que tienen Pokemon de tipo fuego/planta o agua/volador:')
# for i in range(lista_tipos.tamanio()):
#     print(lista_tipos.obtener_elemento(i)['Nombre'])

# print()

# #Punto G
# def promedio_nivel (lista_pokemon):
#     """Calcula el promedio de nivel de los pokemones en una lista"""
#     total_niveles = 0
#     for i in range (lista_pokemon.tamanio()):
#         total_niveles += lista_pokemon.obtener_elemento(i)['Nivel']
#     return total_niveles/lista_pokemon.tamanio()

# nombre = input('Ingrese el nombre del entrenador para calcular el promedio de nivel de sus Pokemon: ').capitalize()
# pos = entrenadores.busqueda(nombre, 'Nombre')
# if (pos != -1):
#     """round redondea un numero"""
#     promedio = round(promedio_nivel(entrenadores.obtener_elemento(pos)['Pokemones'],2))
#     print('El promedio de nivel de los Pokemon de', entr, 'es:', promedio)

# print()

# #Punto H
# def entrenadores_pokemon (pokemon, lista):
#     """Determina cuantos entrenadores tienen a un determinado pokemon."""
#     cantidad_entrenadores = 0
#     for i in range (lista.tamanio()):
#         pos = lista.obtener_elemento(i)['Pokemones'].busqueda(pokemon, 'Nombre')
#         if (pos != -1):
#             cantidad_entrenadores += 1
#     return cantidad_entrenadores

# poke = input('Ingrese el nombre del Pokemon para determinar cuantos entrenadores lo tienen: ').capitalize()
# print (entrenadores_pokemon(poke, entrenadores), 'entrenador(es) tiene(n) a', poke)

# print()

# #Punto I
# def Entrenador_pokemon_repetido(Lista):
#     ocurrencias = None

#     for i in range(0, Lista.tamanio()):
#         entrenador = Lista.obtener_elemento(i)
        
#         for i in range(0, entrenador['pokemons'].tamanio()):
#             ocurrencias = 0

#             for j in range(0, entrenador['pokemons'].tamanio()):
#                 if entrenador['pokemons'].obtener_elemento(i)['nombre'].lower() == entrenador['pokemons'].obtener_elemento(j)['nombre'].lower():
#                     ocurrencias += 1

#                     if ocurrencias > 1:
#                         break
            
#             if ocurrencias > 1:
#                 print(entrenador)
#                 break

# print ('Entrenadores con pokemon repetidos: ')
# Entrenador_pokemon_repetido(entrenadores)



# #Punto J
# print('Los entrenadores que tienen un Tyrantrum, Terrakion o Wingull son:')
# for i in range(entrenadores.tamanio()):
#     entrenador =  entrenadores.obtener_elemento(i)
#     lista_pokemones = entrenador['Pokemones']
#     for j in range(lista_pokemones.tamanio()):
#         if (lista_pokemones.obtener_elemento(j)['Nombre'] == 'Tyrantrum' or 
#             lista_pokemones.obtener_elemento(j)['Nombre'] == 'Terrakion' or 
#             lista_pokemones.obtener_elemento(j)['Nombre'] == 'Wingull'):
#             print(entrenador['Nombre'])

# print()

# #Punto K
# ent = input('Ingrese el nombre del entrenador para saber si tiene a un Pokemon: ').capitalize()
# pos = entrenadores.busqueda(ent, 'Nombre')
# if pos != -1:
#     poke = input('Ingrese el nombre del pokemon: ').capitalize()
#     pos2 = entrenadores.obtener_elemento(pos)['Pokemones'].busqueda(poke, 'Nombre')
#     if pos2 != -1:
#         print(ent, 'tiene a', poke)
#         entrenador = entrenadores.obtener_elemento(pos)
#         print(ent, '| Torneos Ganados:', entrenador['Torneos'], '| Batallas perdidas:', entrenador['Perdidas'], '| Batallas ganadas:', entrenador['Ganadas'])
#         pokemon = entrenadores.obtener_elemento(pos)['Pokemones'].obtener_elemento(pos2)
#         print (poke, '| Nivel:', pokemon['Nivel'], '| Tipo:', pokemon['Tipo'], '| Subtipo:', pokemon['Subtipo'])
#     else:
#         print(ent, 'no tiene a', poke)
# else:
#     print ('No existe entrenador con ese nombre.')







# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, 
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las 
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron


lista_jedis = Lista()
lista_especie = Lista()

file = open('jedis.txt', encoding="utf8")
lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1].title()
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].title().split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5].title()
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if len(jedi) > 8:
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] =jedi[9]
    lista_jedis.insertar(jedi_data, 'name')
    lista_especie.insertar(jedi_data, 'species')

def mostrar_elemento (lista, pos):
    jedi = lista.obtener_elemento(pos)
    print('- Nombre:', jedi['name'], ' | Rango:', jedi['rank'], ' | Especie:', jedi['species'], ' | Maestro(s):', jedi['master'])
    print ('  Color de sable de luz:', jedi['lightsaber_color'], ' | Planeta natal:', jedi['homeworld'], ' | Año de nacimiento:', jedi['birth_year'], ' | Altura:', jedi['height'])


print() 

# Punto A 
print('Listado ordenado por nombre:')
for i in range(lista_jedis.tamanio()):
    mostrar_elemento(lista_jedis, i)

print()

print('Listado ordenado por especie:')
for i in range(lista_especie.tamanio()):
    mostrar_elemento(lista_especie, i)

# Punto B 
print('Información de Ahsoka Tano y Kit Fisto')
pos = lista_jedis.busqueda('Ahsoka Tano', 'name')
if pos != -1:
    mostrar_elemento(lista_jedis, pos)

pos = lista_jedis.busqueda('Kit Fisto', 'name')
if pos != -1:
    mostrar_elemento(lista_jedis, pos)

# Punto C
print('Padawans de Luke Skywalker y Yoda:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Luke Skywalker' in jedi['master'] or 'Yoda' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])

print()

# Punto D
print("Jedi de especie humana y twi'lek")
for i in range(lista_especie.tamanio()):
    jedi = lista_especie.obtener_elemento(i)
    if (jedi['species']=='human' or jedi['species'] == "twi'lek"):
        mostrar_elemento(lista_especie, i)

print()

# Punto E
print('Jedi que comienzan con A:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if jedi['name'][0]=='A':
        print(jedi['name'])
print()

# Punto F
print('Jedi que usaron sable de mas de un color:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if len(jedi['lightsaber_color'])>1:
        print(jedi['name'], ' - Colores:', jedi['lightsaber_color'])

print()

# Punto G
print('Jedis que usaron un sable de luz amarillo o violeta:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if 'yellow' in jedi['lightsaber_color'] or 'purple' in jedi['lightsaber_color']:
        print(jedi['name'])

print()

# Punto H.
print('Padawans de Qui-Gon Jin y Mace Windu:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Qui-Gon Jin' in jedi['master'] or 'Mace Windu' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()