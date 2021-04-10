#! 2)Implementar una función que calcule la suma de todos los números enteros comprendidos 
#! entre cero y un número entero positivo dado

#!def func_suma (numero):
#!    if(numero == 0 ):
#!       return (0)
#!    else:
#!        return numero + func_suma(numero-1)



#!print (func_suma (3)) 


#! 3)Implementar una función para calcular el producto de dos números enteros dados.


#!def func_prod (num1,num2):
#!    if (num2 == 1) :
 #!       return (num1)
 #!   else:
#!       return num1 + func_prod (num1,num2-1)

#!print (func_prod(3, 4))

#!4)Implementar una función para calcular la potencia dado dos números enteros,
#! el primero representa la base y segundo el exponente.


def func_pot(numero1,numero2):
    if (numero2 == 0):
        return (1)
    else:
         return numero1 ** numero2

print (func_pot(4, 2))