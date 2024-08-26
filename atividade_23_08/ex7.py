from datetime import datetime

data_atual = datetime.now()

print(f"Data atual: {data_atual}")
print(f"Ano atual: {data_atual.year}")
print(f"Mês atual: {data_atual.month}")
print(f"Dia atual: {data_atual.day}")

data_formatada = data_atual.strftime("%d/%m/%Y")
print(f"Data atual formatada: {data_formatada}")

data_formatada_extenso = data_atual.strftime("%d de %B de %Y")
print(f"Data atual no formato dia e mês por extenso e ano: {data_formatada_extenso}")
