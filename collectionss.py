# Para crear una lista se usan [] o {} 
# Creamos la lista myFruitList y dentro de lla guardamos las siguientes frutas "apple", "banana", "cherry"
myFruitList = ["apple", "banana", "cherry"]

#Imprimimos la lista de frutas completa
print(myFruitList)

#Imprimimos el tipo de dato que es myFruitsList
print(type(myFruitList))

#Imprimimos el valor que esta en la primer posición de la lista myFruitList (Este valor es "apple")
print(myFruitList[0])

#Imprimimos el valor que esta en la segunda posición de la lista myFruitList (Este valor es "banana")
print(myFruitList[1])

#Imprimimos el valor que esta en la tercer posición de la lista myFruitList (Este valor es "cherry")
print(myFruitList[2])

#Vamos a cambiar el valor de la lista en la posición 2, antes era "cherry" y ahora es "orange"
myFruitList[2] = "orange"

#Imprimimos la lista completa con el cambio
print(myFruitList)

#Para crear una tuppla se usan ()
#Creamos la tupla llamada myFinalAnswerTuple() y dentro de ella guardamos las siguientes frutas "apple", "banana", "cherry"
myFinalAnswerTuple = ("apple", "banana", "pineapple")

#Imprimimos la tupla completa
print(myFinalAnswerTuple)

#Imprimimos el tipo de dato de myFinalAnswerTuple
print(type(myFinalAnswerTuple))

#Imprimimos el primer valor de la tupla que es "apple"
print(myFinalAnswerTuple[0])

#Imprimimos el segundo valor de la tupla que es "banana"
print(myFinalAnswerTuple[1])

#Imprimimos el tercer valor de la tupla que es "pineapple"
print(myFinalAnswerTuple[2])

#Para crear un diccionario se utilizan {} y dentro de ellas se va a crear una clave y un valor. La clave y el valor van separados por : y luego de cada clave:valor se separa usando ,
# Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves "Akua, Saanvi y Paulo" con sus respectivos valores "apple, banana y pineapple"
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

#Imprimimos el diccionario completo
print(myFavoriteFruitDictionary)

#Imprimimos el tipo de variable de myFavoriteFruitDictionary 
print(type(myFavoriteFruitDictionary))

# Imprimimos el valor de la clave "Akua"
print(myFavoriteFruitDictionary["Akua"])

## Imprimimos el valor de la clave "Saanvi"
print(myFavoriteFruitDictionary["Saanvi"])

# Imprimimos el valor de la clave "Paulo"
print(myFavoriteFruitDictionary["Paulo"])
