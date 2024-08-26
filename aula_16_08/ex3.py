def exibir_tabuada(numero):
    """
    Função para exibir a tabuada de um número específico.
    """
    for i in range(1, 11):  # Loop de 1 a 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    # Solicitando ao usuário o número desejado
    try:
        numero = int(input("Digite o número para ver a tabuada: "))
        
        # Validando se o número é positivo
        if numero > 0:
            exibir_tabuada(numero)
        else:
            print("Número inválido. Por favor, digite um número inteiro positivo.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
