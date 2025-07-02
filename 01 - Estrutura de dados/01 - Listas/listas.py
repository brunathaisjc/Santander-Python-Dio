# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação. 

frutas = ["laranja", "maçã", "uva"] # lista com valores (objeto python)
frutas = [] # lista vazia
frutas = list('Python') # este construtor pede um argumento iterável. Uma string é um elemento iterável. 
numeros = list(range(10)) # esta função built-in vai criar um elemento para cada número retornado pela função range.
carros = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] # lista com valores de alguns atributos. 

# Acesso direto

#A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero. 

frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[0]) # maçã
print(frutas[2]) # uva

# Índices negativos
# Sequêcias suportam indexação negativa. A contagem começa em -1.
#            -4     -3       -2      -1
frutas = ["maçã", "laranja","uva","pera"]
print(frutas[-1])
print(frutas[-1])

# Listas Aninhadas
# Linhas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna. 
# É mais usado para representação de matriz. 
# Bidimensional ou com mais dimensões

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])
print(matriz[1])
print(matriz[1][2])
print(matriz[-1][-3])
print(matriz[-3])

# Fatiamento 
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso. 

lista = ["P", "y", "t", "h", "o", "n"]

print(lista[0])
print(lista[:4:2])
print(lista[:5])
print(lista[::])
print(lista[0:3:2])
print(lista[::-1])

# Iterar listas
# A forma mais comum para percorrer os dados de uma lista é utilizando o comando for. 

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


# Função enumerate 

# Às vezes é necessário saber qual é índice do objeto dentro do laço for. Para isso podemos usar a função enumarate. 

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros): # indice - é o contador; carro - é o item da iteração
    print(f"{indice}: {carro}")
