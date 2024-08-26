sequencia = input("Digite uma sequência de caracteres: ")

letras = 0
digitos = 0

for char in sequencia:
    if char.isalpha():
        letras += 1
    elif char.isdigit():
        digitos += 1

print(f"Letras: {letras}")
print(f"Dígitos: {digitos}")