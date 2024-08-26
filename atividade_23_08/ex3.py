palavras = input("Digite uma sequência de palavras separadas por vírgula: ")

lista_palavras = [palavra.strip() for palavra in palavras.split(",")]
lista_palavras.sort()

print("Palavras ordenadas:", ", ".join(lista_palavras))