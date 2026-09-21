'''try:
    numero = int(input("Digite um numero: "))
    print(numero)
    
except ValueError:
    print("Valor invalido! (-_-)")'''
    
try:
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    
    resultado = n1/n2
    print(f"O resultado da divisão é {resultado}")
except ValueError:
    print(f"Favor digitar somente números")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
else: 
    print("O programa foi executado corretamente!")
    
finally:
    print("Programa finalizado")
    
#
    