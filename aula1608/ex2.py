import os
os.system('cls')

res1 = float(input("Digite o valor da resistencia 1: "))
res2 = float(input("Digite o valor da resistencia 2: "))
res3 = float(input("Digite o valor da resistencia 3: "))
res4 = float(input("Digite o valor da resistencia 4: "))


def calcular_resistencia_equivalente(resistencias):
    """
    Função para calcular a resistência equivalente de um circuito em série.
    Retorna a soma de todas as resistências fornecidas.
    """
    return sum(resistencias)

def main():
    # Valores das resistências fornecidas
    resistencias = [200, 300, 400, 700]
    
    # Calculando a resistência equivalente
    resistencia_equivalente = calcular_resistencia_equivalente(resistencias)
    
    # Identificando a maior e a menor resistência
    maior_resistencia = max(resistencias)
    menor_resistencia = min(resistencias)
    
    # Exibindo os resultados
    print(f"A resistência equivalente do circuito é: {resistencia_equivalente} ohms")
    print(f"A maior resistência é: {maior_resistencia} ohms")
    print(f"A menor resistência é: {menor_resistencia} ohms")

if __name__ == "__main__":
    main()
