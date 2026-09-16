#Programa para calcular a hipotenusa ou um cateto de um triangulo retangulo
print("=== Cálculo em Triângulo Retângulo ===")
print("1 - Calcular a Hipotenusa")
print("2 - Calcular a Cateto ")


opcao = int(input("Escolha uma opção: "))

if opcao ==1:
    cateto1 = float(input("Digite o valor de primeiro cateto: "))
    cateto2 = float(input("Digite o valor de segundo cateto: "))    

    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

    print(f"\n A hipotenusa é: {hipotenusa: .2f}")

elif opcao == 2:
    hipotenusa = float(input("Digite o valor da hipotenusa: "))
    cateto = float(input("Digite o valor do outro cateto: "))

    if hipotenusa > cateto:
        outro_cateto = (hipotenusa ** 2 - cateto ** 2) ** 0.5
        print(f"\nO cateto é: {outro_cateto: .2f}")

    else: 
        print("\nValores invalidos. A hipotenusa deve ser maior que o cateto.")
     
else:
    print("\nOpção invalida.")


