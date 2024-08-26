numeros = input("Digite uma sequência de números separados por vírgula: ")

lista_numeros = numeros.split(",")
tupla_numeros = tuple(lista_numeros)

print("Lista:", lista_numeros)
print("Tupla:", tupla_numeros)