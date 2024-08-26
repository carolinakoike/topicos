senha = input("Digite uma senha: ")

tem_minuscula = False
tem_maiuscula = False
tem_digito = False
tem_simbolo = False
simbolos_permitidos = "$#@!.?&*"

for char in senha:
    if char.islower():
        tem_minuscula = True
    elif char.isupper():
        tem_maiuscula = True
    elif char.isdigit():
        tem_digito = True
    elif char in simbolos_permitidos:
        tem_simbolo = True

if len(senha) < 6 or len(senha) > 12:
    print("Senha inválida: o tamanho deve ser entre 6 e 12 caracteres.")
elif not tem_minuscula:
    print("Senha inválida: deve conter pelo menos uma letra minúscula.")
elif not tem_maiuscula:
    print("Senha inválida: deve conter pelo menos uma letra maiúscula.")
elif not tem_digito:
    print("Senha inválida: deve conter pelo menos um dígito.")
elif not tem_simbolo:
    print(f"Senha inválida: deve conter pelo menos um símbolo ({simbolos_permitidos}).")
else:
    print("Senha válida!")