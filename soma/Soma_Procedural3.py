#Definindo objetos

def leitora_numeros(): ###Função, a função tem um escopo local
    numeros = []
    i = 0
    while i < 2:
        numeros.append(float(input(f"Digite o {i + 1}º número: ")))
        i += 1
    return numeros

##Processamento de dados

def adicao(x,y): ###Função
    return x+y

##Saida de dados

def escritora_numeros(x,y,z): ###Função
    print(f" A soma dos números {x} e {y} é igual a {z}.")
    
    
def main(): 
    #Atribuição de variáveis
    numeros = []
    soma = 0
    
    #Entrada de dados
    numeros = leitora_numeros()
    
    #Processamento de dados
    soma = adicao(numeros[0],numeros[1])
    
    #Saida de dados
    escritora_numeros(numeros[0], numeros[1], soma)
    
#Invocando main
main()