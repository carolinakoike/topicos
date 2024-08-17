import os
os.system('cls')

product = input("Digite o nome do produto: ")
value = float(input("Digite o valor do produto: "))

if value <= 0:
    result = "Valor invalido"
if value < 50:
    result = "Sem desconto"
elif value >= 50 and value < 200:
    result = value * 0.05
elif value >= 200 and value < 500:
    result = value * 0.06
elif value >= 500 and value < 1000:
    result = value * 0.07
elif value >= 500 and value < 1000:
    result = value * 0.07
else:
    result = value * 0.08

print(f"Nome do Produto: {product}")
print(f"Valor Original: R${value:.2f}")
print(f"Desconto: R${result:.2f}")
print(f"Novo valor: R${value - result:.2f}")