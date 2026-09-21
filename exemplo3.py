#Fazendo calculos
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

s = n1+n2 
m = n1 * n2
d = n1 / n2 
di = n1 // n2 
e = n1 ** n2 

print(f"Soma ou total: {n1} + {n2} = {s}, Produto: {n1} * {n2} = {m}, Razão: {n1} / {n2} = {d:.2f}", end = ' >>> ') #Não quebra a Linha
print(f"Divisão interia {di} e potencia {e}")
