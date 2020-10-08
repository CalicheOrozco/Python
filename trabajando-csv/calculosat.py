f = open("names.txt","r")

# Creamos una lista con cada una de sus lineas
correog = f.readline()
correog = correog.replace("¿","")
correog = correog.replace("»","")
correog = correog.replace("ï","")
correog = correog.replace(",","")
# correog = correog.replace("\n","")

lineas = f.readlines()

for i in range(len(lineas)):

	nombre = str(lineas[i])
	#Verificamos que si existe un espacio en el nombre
	if " " in nombre:
		#si existe no lo guardamos
		print('NO')
	else:
		#Si  no existe lo guarddamos en un txt que se llame NombresSinEspacios
		print (nombre)
		save = open('NombresSinEspacios.txt', 'a')
		save.write(nombre)
		save.close()
        	

		
		
		
		

		
