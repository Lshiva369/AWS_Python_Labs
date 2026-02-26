#Creamos una variable myString y dentro de ella guardamos el comentario "tHIS IS A STRING"
myString = "This is a string"

#Imprimimos el valor de la variable myString
print(myString)

#Imprimimos el tipo de dato de la variable myString
print(type(myString))

#Imprimimos el valor de la variable myString, un texto y el tipo de dato de myString
print(myString + " is of the data type " + str(type(myString)))

# Creamos la variable firtString y dentro de ella guardamos el valor de water
firtString = "water"

#Creamos la variable secondString y guardamos el valor de "fall"
secondString = "fall"

#Creamos la variable thirdString y dentro de ella guardamos el valor concatenado (unido) de las variables fisrtString y secondString
thirdString = firtString + secondString

#Imprimimos el valor de la variable thirdString
print(thirdString)

#Creamos la variable name y usando la función input() vamos a almacenar lo que escriba el usuario por consola
name = input("What is your name?")

#Imprimimos el valor de la variable name
print(name)

#Creamos la variable color y usando la función input() vamos a almacenar lo que escriba el usuario por consola
color = input("What is you favorite color?")

#Creamos la variable color y usando la función input() vamos a almacenar lo que escriba el usuario por consola
animal = input("What is you favorite animal?")

#Para imprimir usando format vamos a poner un corchete por cada variable y el format va a poner el valor de las variables en el orden que las estamos usando
print("{}, you like a {} {}!".format(name, color, animal))