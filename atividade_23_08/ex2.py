i = int(input("Digite o número de linhas (i): "))
j = int(input("Digite o número de colunas (j): "))

array_2d = [[linha * coluna for coluna in range(j)] for linha in range(i)]

print("Array 2D:")
for linha in array_2d:
    print(linha)