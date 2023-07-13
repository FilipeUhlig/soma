# Atribuição de variáveis
numeros = []
soma = 0
i = 0

# Entrada de dados

while i < 2:
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))
    i += 1
    


# Processamento de dados 2

for numero in numeros:
    soma += numero
    
    

# Saida de dados
print(f" A soma dos números {numeros[0]} e {numeros[1]} é igual a {soma}.")