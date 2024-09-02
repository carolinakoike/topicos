import os

def limpar_tela():
    os.system('cls')

def salvar_html(html, nome_pessoa):
    nome_arquivo = f"curriculo_{nome_pessoa.replace(' ', '_')}.html"
    caminho_do_script = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(caminho_do_script, nome_arquivo)
    
    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        arquivo.write(html)
    
    print(f"Currículo salvo como {caminho_completo}")

def gerar_html(nome, endereco, telefone, email, escolaridade, experiencia):
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo de {nome}</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
            h1 {{ text-align: center; }}
            .section {{ margin-bottom: 20px; }}
            .section h2 {{ border-bottom: 2px solid #333; padding-bottom: 5px; }}
        </style>
    </head>
    <body>
        <h1>Currículo de {nome}</h1>
        <div class="section">
            <h2>Dados Pessoais</h2>
            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>Endereço:</strong> {endereco}</p>
            <p><strong>Telefone:</strong> {telefone}</p>
            <p><strong>Email:</strong> {email}</p>
        </div>
        <div class="section">
            <h2>Escolaridade</h2>
            <p>{escolaridade}</p>
        </div>
        <div class="section">
            <h2>Experiência Profissional</h2>
            <p>{experiencia}</p>
        </div>
    </body>
    </html>
    """
    return html

def obter_dados_curriculo():
    nome = input("Digite o seu nome: ")
    endereco = input("Digite o seu endereço: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu email: ")
    escolaridade = input("Digite a sua escolaridade: ")
    experiencia = input("Digite a sua experiência profissional: ")
    return nome, endereco, telefone, email, escolaridade, experiencia

def main():
    limpar_tela()
    nome, endereco, telefone, email, escolaridade, experiencia = obter_dados_curriculo()
    html = gerar_html(nome, endereco, telefone, email, escolaridade, experiencia)
    salvar_html(html, nome)

if __name__ == "__main__":
    main()