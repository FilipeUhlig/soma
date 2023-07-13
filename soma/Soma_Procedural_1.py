# Atribuição de variáveis
numeros = []
soma = 0
i = 0

def adicao(x,y): #Função
    return x+y


# Entrada de dados

while i < 2:
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))
    i += 1
    
    
# Processamento de dados

soma = adicao(numeros[0], numeros[1])

# Saida de dados
print(f" A soma dos números {numeros[0]} e {numeros[1]} é igual a {soma}.")