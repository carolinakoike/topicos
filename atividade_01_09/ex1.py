import os

def limpar_tela():
    os.system('cls')

def obter_numeros():
    numeros = []
    while True:
        try:
            numero = float(input("Digite um número (ou 's' para finalizar): "))
            numeros.append(numero)
        except ValueError:
            opcao = input("Deseja finalizar a entrada de números? (s/n): ").strip().lower()
            if opcao == 's':
                break
    return numeros

def contar_pares(numeros):
    return sum(1 for numero in numeros if numero % 2 == 0)

def encontrar_impares(numeros):
    return [numero for numero in numeros if numero % 2 != 0]

def encontrar_maior(numeros):
    return max(numeros)

def encontrar_menor(numeros):
    return min(numeros)

def calcular_media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

def main():
    limpar_tela()
    numeros = obter_numeros()

    if numeros:
        print(f"Números digitados: {numeros}")
        print(f"Quantidade de números pares: {contar_pares(numeros)}")
        print(f"Números ímpares: {encontrar_impares(numeros)}")
        print(f"O maior número é: {encontrar_maior(numeros)}")
        print(f"O menor número é: {encontrar_menor(numeros)}")
        print(f"A média dos números é: {calcular_media(numeros):.2f}")
    else:
        print("Nenhum número foi informado.")

if __name__ == "__main__":
    main()
