# 1. Dado un vector con personaje de las películas de la saga de Star Wars resolver las
# siguientes actividades:
# a. Realizar un barrido recursivo del vector. 
# b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
# vector y en que posición.

personajes = ['Luke','Chewe','Yoda','Leia','Anakin','Han solo']
pos = 0
def barrido(personajes, pos):
    if(pos < len(personajes)):
       print (personajes[pos])
       barrido(personajes,pos+1)

barrido (personajes,0)

def encontrar_personaje(personajes,pos):
    if(pos< len(personajes)):
        
        if(personajes[pos] == 'Yoda'): 
            return pos
        else:
            return encontrar_personaje(personajes, pos+1)
    else:
        print ('Yoda no esta en el vector')
        return -1

encontrar_personaje (personajes,0)

print ('Yoda se encuentra en la posicion: ',(encontrar_personaje(personajes, 0)))


       
    