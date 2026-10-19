#Esse código é um programa desenvolvido em Python que realiza o cadastro de frutas em uma lista. Ele permite que o usuário digite novas frutas, verifica se elas já estão cadastradas, evita duplicações e exibe a lista final com a quantidade total de frutas.
#O código utiliza conceitos fundamentais da programação, como listas, variáveis, estruturas condicionais, laços de repetição, métodos e funções. Esses recursos permitem organizar os dados e controlar a execução do programa.


# O código cria uma lista chamada frutas e armazena quatro frutas nela.
frutas = ["Maçã", "Banana", "Uva", "Laranja"]

# A variável continuar controla a repetição do cadastro.
continuar = "sim"

# O while repete o cadastro enquanto a resposta for "sim" ou "s".
# O operador or permite que uma das condições seja verdadeira.
while continuar == "sim" or continuar == 's':

    # O input() recebe o nome da fruta digitada pelo usuário.
    # O strip() remove os espaços do início e do final do texto.
    # O title() coloca a primeira letra de cada palavra em maiúscula.
    novo_item = input("Digite o nome da fruta: ").strip().title()

    # O if verifica se o usuário deixou o campo vazio.
    if novo_item == "":
        print("Digite o nome de uma fruta para realizar o cadastro")

    # O elif usa o operador in para verificar se a fruta já existe na lista.
    elif novo_item in frutas:

        # O index() localiza o índice da fruta na lista.
        # Os índices começam em 0, portanto a primeira fruta ocupa o índice 0.
        posicao = frutas.index(novo_item)

        # A f-string permite inserir o valor da variável posicao na mensagem.
        print(f"O item informado ja existe na lista na posição {posicao}ª !")

    else:
        # O append() adiciona a nova fruta ao final da lista.
        frutas.append(novo_item)

        # O índice -1 permite acessar o último elemento da lista.
        print(f"A fruta {frutas[-1]} foi cadastrada com sucesso")

        # O print() exibe a lista atualizada no terminal.
        print(frutas)

    # O input() pergunta se o usuário deseja continuar o cadastro.
    # O strip() remove os espaços das extremidades do texto.
    # O lower() transforma todas as letras em minúsculas.
    continuar = input("Deseja continuar 'sim' ou 'não': ").strip().lower()

# O print() exibe o título da lista final de frutas.
print("Lista das frutas: ")

# O for percorre todos os elementos da lista.
# O enumerate() fornece o índice e o nome de cada fruta.
for i, fruta in enumerate(frutas):

    # A soma i+1 faz a numeração exibida começar em 1, em vez de 0.
    print(f"{i+1}-{fruta}")

# O len() conta a quantidade de elementos existentes na lista.
print(f"A lista contem {len(frutas)}  tipos de frutas")
