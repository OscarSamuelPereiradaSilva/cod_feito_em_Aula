continuar = True
while continuar:
    numero = int(input("Digite um número para ver a tabuada: "))
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
    continuar = input("Deseja continuar? (s/n) ").lower().strip()
    continuar = True if continuar == "s" else print("Valor invalido, digite letras!")
    