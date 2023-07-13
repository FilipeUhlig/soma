# Definindo os objetos
numeros = []
soma = 0
i = 0

##Função para entrada de dados

def leitora_numeros(): ###Função, a função tem um escopo local
    i = 0
    while i < 2:
        numeros.append(float(input(f"Digite o {i + 1}º número: ")))
        i += 1
    return numeros




##Função para o processamento de dados

def adicao(x,y): ###Função
    return x+y

##Função para a saida de dados

def escritora_numeros(x,y,z): ###Função
    print(f" A soma dos números {x} e {y} é igual a {z}.")
    
# Entrada de dados

numeros = leitora_numeros() #Resultado da execução leitora_numeros é guardado na lista numeros.

# Processamento de dados

soma = adicao(numeros[0],numeros[1]) #Resultado da execução da função soma

# Saida de dados
escritora_numeros(numeros[0], numeros[1], soma) #Resultado da função de escritora de numeros