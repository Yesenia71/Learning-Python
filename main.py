# print("Hello World")

# declaracion de variable, podemos colocar un nombre y le ponemos un igual y cuando queramos imprimir podemos llamar la variable. se pueden reutilizar.
# mivariable = 3
# print(mivariable)
# print(mivariable)
# mivariable = 9
# print(mivariable)


#la variabe se almacena en una posicion de memoria!
# x=10
# y=10
# z= x+y
# print(x)
# print(y)
# print(z)
# print(id(x))
# print(id(y))
# print(id(z))
# print(type(x))

# x='Hola Mundo'
# print(x)
# print(type(x))
# # para definir los valores de tipo boolean debemos respetar las mayuculas al inicio del True o False 
# # tipos de datos ej:

# # int, entero 
# x = 128
# print(x)
# print (type(x))

# #float 
# y= 12.3
# print(y)
# print (type(y))

# #String 
# z = 'Holi'
# print(z)
# print(type(z))

# #boolean
# f = False
# print (type(f))
# g = True
# print (type(g))

#ejercicio que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
age = int(input("¿Cuál es tu edad? "))
if age < 18: 
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
    
    # ejercicio que que almacene la cadena de caracteres contraseña en una variable, 
    # pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
    # introducida por el usuario coincide con la guardada en la variable sin tener en
    # cuenta mayúsculas y minúsculas.
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")