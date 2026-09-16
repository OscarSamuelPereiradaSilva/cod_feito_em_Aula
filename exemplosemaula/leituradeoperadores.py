operadores = int(input("qual operador vc deseja ultilizar? \n1 = / \n2 = * \n3 = + \n4 = - \n informe o numero: "))


match operadores:   
    case 1:
        A = int(input("Digite o valor A: "))
        B = int(input("Digite o valor B: ")) 
        if B != 0:
            resultado = A / B
            print(f"O resultado é: {resultado}")
        else: 
            print(f"Não é possivel dividir {A} por 0.")
    case 2 :
        A = int(input("Digite o valor A: "))
        B = int(input("Digite o valor B: "))
        resultado = A * B
        print(f"{A} x {B } = {resultado}")
    case 3 :
        A = int(input("Digite o valor A: "))
        B = int(input("Digite o valor B: "))
        resultado = A + B
        print(f"O resultado é: {resultado}")
    case 4:
        A = int(input("Digite o valor A: "))
        B = int(input("Digite o valor B: "))
        resultado = A - B
        print(f"O resultado é: {resultado}")
    case _: 
        print('Valor invalido.')