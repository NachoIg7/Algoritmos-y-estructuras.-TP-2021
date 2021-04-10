def suma(numero1, numero2):
    """ esta funcion suma dos numeros y devuelve....."""
    print('la suma es', numero1 + numero2)
    numero1 = 0
    numero2 = numero1 + numero2
    return numero1, numero2





    #! FUNCIONES DE CONVERSION int(valor) float(valor) str(valor) bool(valor)
#! OPERAODRES ARITMETICOS +, -, *, /, //, **, % 
#! ASIGNACION =
#! OPERADORES DE CONTROL >, < >=, <=, ==, !=
#! OPERADORES LOGICOS and or
#! CONDICIONALES
#! CICLOS
#! FUNCIONES
#! MODULO

numero = int(input('ingrese su numero '))

# if(numero > 0 or numero < 10):
#     print('es positivo')
# elif(numero < 0):
#         print('es negativo')
# else:
#     print('es neutro')


# while(numero > 0):
#     print(numero)
#     numero -= 1 # numero += 1


# for i in range(1, 11):
#     print('iteracion', i)


print('fin del codigo')


from funciones import suma


numero, total = suma(numero, 5)

print(numero, total)

# print(numero ** 5)








