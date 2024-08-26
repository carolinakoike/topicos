import os
os.system('cls')

res1 = float(input("Digite o valor da resistencia 1: "))
res2 = float(input("Digite o valor da resistencia 2: "))
res3 = float(input("Digite o valor da resistencia 3: "))
res4 = float(input("Digite o valor da resistencia 4: "))

soma = res1 + res2 + res3 + res4

maior_resistencia = max(res1, res2, res3, res4)
menor_resistencia = min(res1, res2, res3, res4)

print(f"A resistência equivalente do circuito é: {soma} ohms")
print(f"A maior resistência é: {maior_resistencia} ohms")
print(f"A menor resistência é: {menor_resistencia} ohms")