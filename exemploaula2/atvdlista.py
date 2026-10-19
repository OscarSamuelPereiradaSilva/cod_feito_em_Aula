'''frutas = ["maçã", "Banana", "Uva", "Laranja"]

#ALTERANDO ELEMENTOS    

frutas [1] = "abacaxi"

#INSERINDO ELEMENTOS 

frutas.append("Melancia")
frutas.insert(1, "pera")
frutas.extend(["Kiwi", "Manga"])

#ACESSANDO OS ELEMENTSO

print(frutas[0])
print(frutas[2])
print(frutas[-1])
print("IMPRIMINDO TODOS OS ELEMENTOS\n")

#PECORRENDO A LISTA

for fruta in frutas:
    print(f"A fruta é: {fruta}")'''

    
#ADICIONANDO ELEMENTOS 


#adiciona um elemento a ultima posição da lista
frutas.append("Melancia")

#adiciona um elementos em uma posição da lista
frutas.insert(1, "Pera")

#adicionando varios do elementos na lista
frutas.extend(["Kiwi", "Manga"])

#Verificando a existencia do elementos na lista
verificar = "Maça" in frutas 
print(verificar)

#verifca a quantidade de elementos na lista
quantidade_de_elementos = len(frutas)
print(quantidade_de_elementos)

#Contando os elementos 
contador = frutas.count("Pera")
print(contador)

#retorna o indice do valor 
indice = frutas.index("Pera")
print(f"A fruta do indice {indice}, corresponde ao elemento {frutas[indice]}")

#fazendo um copia da lista
listas = frutas.copy()
listas = frutas.append("Melancia")
print(listas)
contador = listas.count("Melancia")
print(contador)

#percorrendo todos elementos da lista
print("Pecorrendo a lista")
for fruta in frutas:
    print(fruta)