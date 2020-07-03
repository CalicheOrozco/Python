def fibonacci(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)    

semestre = fibonacci(3)
print(f'en 6 meses se tendrian {semestre} conejos')