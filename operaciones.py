def multiplicar_por_dos(n):
    """Multiplica por 2 a n.

        n int >0
        return n * 2
        """
    return n * 2

def sumar_dos(n):
    """suma 2 a n.

        n int >0
        return n + 2
        """
    return n + 2

def aplicar_operacion(f, numeros):
    """Aplica una operacion.

        f una de las funciones: multiplicar_por_dos o sumar_dos
        numeros recibe una lista de numeros
        guarda los resultaldos en una lista
        """
    resultados=[]
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    print(resultados)

    
nums = [1,2,3]
aplicar_operacion(multiplicar_por_dos,nums)
print('')
aplicar_operacion(sumar_dos,nums)
