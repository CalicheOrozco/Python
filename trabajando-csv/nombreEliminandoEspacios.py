f = open("names.txt","r")

# Creamos una lista con cada una de sus lineas
correog = f.readline()
correog = correog.replace("¿","")
correog = correog.replace("»","")
correog = correog.replace("ï","")
correog = correog.replace(",","")
correog = correog.replace(" ", "")
# correog = correog.replace("\n","")

lineas = f.readlines()
for i in range(len(lineas)):

	nombre = str(lineas[i])
	#Verificamos si tiene espacios el nombre
	if " " in nombre:
		#Si tiene espacio no lo guarddamos
		print('NO')
	else:
		#Si no tiene espacios lo guardamos en un TXT que se llama nombreSinEspacios
		print (nombre)
		save = open('nombreSinEspacios.txt', 'a')
		save.write(nombre)
		save.close()
        	

		
		
		
		

		
