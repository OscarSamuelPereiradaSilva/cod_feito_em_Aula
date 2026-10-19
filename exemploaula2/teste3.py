idade = int(input("Digite sua idade: "))
matricula = str(input("Sua matricula esta ativada? (s/n)")).lower

if idade >= 18 and matricula == "s":
    print("Acesso liberado")

else:
    print("Acesso negado!")