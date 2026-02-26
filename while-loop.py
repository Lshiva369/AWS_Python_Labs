#Siempre que importemos una libreria debe ir al principio del código
import random

# Un ciclo while es un bucle que va a recorrer hasta que no se cumpla la condición
# Se crea la variable número y se le pide al usuario que escriba el número 0
numero = input("Escriba el número 0: ")

#Convertimos la variable número de str a int
numero = int(numero)

# Se verifica que lo que hay en la variable número sea menor que 10
while numero < 10:
    # Se incrementa el valor de número
    numero = numero + 1 
    
    # Si número es menor que 10 se imprime su valor 
    print(numero)
    

# ---------------------------------------------------------------
# Vamos a construir tablas de multiplicar de un número
# Se crea la variable número y se le pide al usuario que escriba el número 0
numero = input("Escriba un número: ")

#Convertimos la variable número de str a int
numero = int(numero)

# Multiplicador
multiplicador = 0

# Se verifica que lo que hay en la variable número sea menor que 10
while multiplicador < 10:

    # Se incrementa el valor de multiplicador
    multiplicador = multiplicador + 1 
    #Valor de multiplicación
    multiplicacion = numero * multiplicador

    # Si número es menor que 10 se imprime su valor 
    #print(numero, " * ", multiplicador, " = ", multiplicacion)
    print(f"{numero} * {multiplicador} = {multiplicacion}" )


#-------------------------------- Laboratorio --------------------------------
#Se realizan 2 impresiones
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
 
# La librería random genera númernumber = random.randit(1, 10)
number = random.randint(1,10)

#Se crea la variable isGueddRight y se guarda un valor booleano (False)
isGuessRight = False

#Mientras la variable isGuessRight sea diferente de verdadero se ejecuta el codigo
while isGuessRight != True:
    #Se crea la variable guess y se guarda dento de ella lo que escriba el usuario
    guess = input("Guess a number between 1 and 10: ")
    # Mientras el valor de la variable guess sea un entero exactamente igual al valor de la variable number 
    if int(guess) == number:
        # Imprime que ganamos 
        print("You guessed {}. That is correct! You win!".format(guess))
        # La variable  isGuessRight  se pasa a verdadero para terminar el ciclo while
        isGuessRight = True
    # Si la variable guess no es exactamente igual a la variable  isGuessRight  imprime 
    else:
        #Intentalo de nuevo
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))