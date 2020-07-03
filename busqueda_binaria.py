objetivo = int(input('Dame un numero: '))
epsilon = 0.001
bajo = 0.0
alto = max(1.0, objetivo)

respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    #print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    valor = abs(respuesta**2 - objetivo)
    
    if respuesta**2 < objetivo:
        bajo = respuesta
        
    else:
        alto= respuesta
    respuesta = (alto + bajo) /2
print(f'La raiz cuadrade de {objetivo} es {respuesta}')