# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente 
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la 
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con 
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión
from cola import Cola
from heap import HeapMax

cola_prioridad = HeapMax()

# Punto A
cola_prioridad.arribo('DocumentoEmpleado1', 1)
cola_prioridad.arribo('DocumentoEmpleado2', 1)
cola_prioridad.arribo('DocumentoEmpleado3', 1)


# Punto B
print(cola_prioridad.atencion()[1])
print()


# Punto C
cola_prioridad.arribo('DocumentoTI1', 2)
cola_prioridad.arribo('DocumentoTI2', 2)


# Punto D
cola_prioridad.arribo('DocumentoGerente1', 3)

# Punto E
print(cola_prioridad.atencion()[1])
print(cola_prioridad.atencion()[1])
print()

# Punto F
cola_prioridad.arribo('DocumentoEmpleado4', 1)
cola_prioridad.arribo('DocumentoEmpleado5', 1)
cola_prioridad.arribo('DocumentoGerente2', 3)

# Punto G
while (not cola_prioridad.vacio()):
    print(cola_prioridad.atencion()[1])

print()
