import os #Librería que se encarga de importar el sistema

import subprocess

os.system("ls")

# No es un comando/ podemos generar directorios por medio de código 
#sys-admin.py README.md 

# Para ver los subprocesos
subprocess.run(["ls", "-l"])

#Revisar los procesos del archivo
subprocess.run(["ls","-l","README.md"])

#Intentar capturar los comandos hechos por un usuario
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Subprocesos- espacio del disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])