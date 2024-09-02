import os

def limpar_tela():
    os.system('cls')

def obter_altura():
    while True:
        try:
            altura = float(input("Digite a altura em centímetros: "))
            if altura > 0:
                return altura
            else:
                print("A altura deve ser um número positivo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

def obter_peso():
    while True:
        try:
            peso = float(input("Digite o peso em quilogramas: "))
            if peso > 0:
                return peso
            else:
                print("O peso deve ser um número positivo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

def calcular_imc(peso, altura):
    return peso / ((altura/100) ** 2)

def main():
    limpar_tela()
    while True:
        altura = obter_altura()
        peso = obter_peso()
        imc = calcular_imc(peso, altura)
        print(f"O IMC calculado é: {imc:.2f}")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
