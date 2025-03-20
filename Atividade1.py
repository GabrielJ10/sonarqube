def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "r")
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo
    except:
        print("Erro ao ler arquivo") 
print(ler_arquivo("dados.txt"))