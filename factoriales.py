def factoreal(n):
        """Calcula el factorial de n.

        n int >0
        return n!
        """
        #print(n)
        if n == 1:
            return 1
        return n * factoreal(n - 1)
valor = int(input('Dame un numero del cual quieras saber la factoreal: '))
respuesta = factoreal(valor)
print(f'El factoreal de {valor} es: {respuesta}')