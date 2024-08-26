sequencia = input("Digite uma sequência de caracteres: ")

maiusculas = 0
minusculas = 0

for char in sequencia:
    if char.isupper():
        maiusculas += 1
    elif char.islower():
        minusculas += 1

print(f"Maiúsculas: {maiusculas}")
print(f"Minúsculas: {minusculas}")
