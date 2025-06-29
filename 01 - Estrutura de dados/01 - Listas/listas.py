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
# Linhas podem arma

