import math

def calcular_seculo(ano):
    """
    Função para calcular o século de um ano específico.
    Retorna o século correspondente ao ano fornecido.
    """
    return math.ceil(ano / 100)

def main():
    # Solicitando ao usuário o ano desejado
    try:
        ano = int(input("Digite o ano para descobrir o século: "))
        
        # Validando se o ano é positivo
        if ano > 0:
            seculo = calcular_seculo(ano)
            print(f"O ano {ano} está no século {seculo}.")
        else:
            print("Ano inválido. Por favor, digite um ano inteiro positivo.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
