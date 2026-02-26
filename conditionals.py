# Se va a crear u  validador para saber si podemos o no podemos entrar a una fiesta, es importante agregar que para entrar a la fiesta debes ser mayor de edad 
# Se crea la variable edad y en ella se va a guardar lo que escriba el usuario
edad = input("Escriba su edad: ")

#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto 
edad = int(edad)

# Vamos a comparar si la edad es mayor o igual a 18 años
if edad >= 18:
    #Imprime que lo dejen entrar
    print("Puede entrar")

else:
    # Si no se cumplela condición de ser mayor de 18 años, imprime "no puede entrar"
    print("No puede entrar")
    
# Ahora se va a validar si la persona es mayor de edad, y además tiene más de 600 pesos
# Se crea la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Escriba su edad: ")

#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto 
edad = int(edad)

# Se crea la variable dinero  y en ella se guarda lo que escriba el usuario
dinero = input("Escriba su dinero: ")

#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto 
dinero = int(dinero)

# Vamos a comparar si la edad es mayor o igual a 18 años
if edad >= 18:
    # Verificamos si cuenta con el dinero 
    if dinero >= 600:
        #Imprime que lo dejen entrar
        print("Puede entrar")
        
    else: 
        #Como no tiene el dinero no puede entrar
        print("No puede entrar")
        
else:
        # Como no tiene el dinero no puede entrar
        print("No puede entrar")
        
#VERSIÓN 2
# Vamos a comparar si la edad es mayor o igual a 18 años
if edad >= 18 and dinero >= 600: 
    
    #Imprime que lo dejen entrar
    print("v2 Puede entrar")
        
else:
    # Como no tiene el dinero no puede entrar
    print(" v2 No puede entrar")
    

# ------------------------------------------------------    
# Condicional con multiples separaciones
# Creamos la variable llamado dinero

dinero = input("Escriba el dinero con el que cuenta: ")

#Convertimos la variable string a entero
dinero = int(dinero)

if dinero < 100 :
    print("Le compro unas galletas")
elif dinero >= 100 and dinero <= 200 :
    print("Le compro unos chocolates")
elif dinero > 200 and dinero <= 300: 
    print("Le compro unas 300 picafresas")
else:
    print("Le compro un peluche")
    
   
#---------------------LABORATORIO--------------------
#Creamos la variable userReaply y en ella guardamos lo que escriba el usuario
userReaply = input("Do you need to ship a package? (Enter yer or no) ")

#Si lo que hay dentro de la variable userReply es exactamente igual a "yes"
if userReaply == "yes":
    #Imprime que nos puede ayudar
    print("We can help you ship that package!")
    
#De lo contrario dice que vuelva pronto
else: 
    print("Please come back when you need to ship a package. Thank you.")


#En la variable userReaply vamos a guardar una de estas opciones (Enter stamps, envelope, or copy), que deben ser escritas en la consola. Si no se escribe ninguna de ellas se  imprime un mensaje de despedida
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# Si la variable es exactamente igual a "stamps" imprime el mensaje con stamps
if userReply == "stamps":
    print("We have many stamp designs to choose from.")

# Si la variable es exactamente igual a "envelope" imprime el mensaje con envelope
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
    
# Si la variable es exactamente igual a "copy" imprime el mensaje con copy
elif userReply == "copy":
    # Se crea la variable copies y se almacena el numero de copias que desea sacar el usuario
    copies = input("How many copies would you like? (Enter a number) ")
    # Imprime el numero de copias
    print("Here are {} copies.".format(copies))
else:
    #Se imprime el mensaje de despedida
    print("Thank you, please come again.")
        
