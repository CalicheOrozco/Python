import csv
from random import randrange, randint


def NombreRandom(i):
	#Crea la lista vacia
	nombre = []
	#Abre el csv donde estan los nombres
	with open('names.csv') as File:
	    reader = csv.DictReader(File)
	    #Recorre cada columna y la agrega a la lista
	    for row in reader:
	        nombre.append(row)

	    #retorna el nombre del numero porporcionado
	    return nombre[i]['name']

	    
def ApellidoRandom(i):
	#Crea la lista vacia
	apellido = []
	#Abre el csv dondde estan los apellidos
	with open('apellidos.csv') as File:
	    reader = csv.DictReader(File)
	    #Recorre cada columna y la agrega a la lista
	    for row in reader:
	        apellido.append(row)
	    #retorna el apellido del numero porporcionado
	    return apellido[i]['Lastname']

#apellido = []

# with open('apellidos.csv') as File:
#     reader = csv.DictReader(File)
#     for row in reader:
#         apellido.append(row)
#     print (apellido[1]['Lastname'])


# print(NombreRandom(randrange(0, 884)))
# print(ApellidoRandom(randrange(0, 884)))
#     
nombre = NombreRandom(randrange(0, 17324))
apellido = ApellidoRandom(randrange(0, 23683))

print(nombre, apellido)