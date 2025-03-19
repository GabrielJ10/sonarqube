import json
import random
import time

class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.id = random.randint(1000, 9999)

    def exibir_info(self):
        print(f"ID: {self.id} - Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}")

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def vender(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        return False

    def exibir_info(self):
        print(f"Produto: {self.nome}, Preço: {self.preco}, Estoque: {self.estoque}")

class Sistema:
    def __init__(self):
        self.usuarios = {}
        self.produtos = {}

    def adicionar_usuario(self, nome, idade, email):
        usuario = Usuario(nome, idade, email)
        self.usuarios[usuario.id] = usuario

    def adicionar_produto(self, nome, preco, estoque):
        produto = Produto(nome, preco, estoque)
        self.produtos[nome] = produto

    def listar_usuarios(self):
        for usuario in self.usuarios.values():
            usuario.exibir_info()

    def listar_produtos(self):
        for produto in self.produtos.values():
            produto.exibir_info()

    def processar_compra(self, user_id, produto_nome, quantidade):
        usuario = self.usuarios.get(user_id)
        produto = self.produtos.get(produto_nome)
        
        if not usuario or not produto:
            print("Usuário ou produto não encontrado!")
            return
        
        if produto.vender(quantidade):
            print(f"Compra realizada com sucesso para {usuario.nome}")
        else:
            print("Estoque insuficiente!")

    def salvar_dados(self):
        dados = {
            "usuarios": {uid: vars(usr) for uid, usr in self.usuarios.items()},
            "produtos": {p: vars(prod) for p, prod in self.produtos.items()}
        }
        try:
            with open("dados.json", "w") as f:
                json.dump(dados, f)
        except:
            print("Erro ao salvar os dados!")

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as f:
                dados = json.load(f)
                for uid, info in dados["usuarios"].items():
                    self.usuarios[int(uid)] = Usuario(info["nome"], info["idade"], info["email"])
                for nome, info in dados["produtos"].items():
                    self.produtos[nome] = Produto(info["nome"], info["preco"], info["estoque"])
        except:
            print("Erro ao carregar os dados!")

# Criando um sistema e adicionando usuários e produtos
sistema = Sistema()
sistema.adicionar_usuario("Alice", 25, "alice@email.com")
sistema.adicionar_usuario("Bob", 30, "bob@email.com")
sistema.adicionar_produto("Laptop", 3000, 10)
sistema.adicionar_produto("Mouse", 50, 200)

# Erros propositais:
sistema.adicionar_usuario("Charlie", "vinte", "charlie@email")  # Tipo incorreto para idade e email
sistema.processar_compra(9999, "Laptop", 2)  # ID de usuário inexistente
sistema.processar_compra(1000, "Teclado", 1)  # Produto inexistente

sistema.listar_usuarios()
sistema.listar_produtos()

# Salvar e carregar dados
sistema.salvar_dados()
sistema.carregar_dados()

# Loop infinito acidental (erro proposital)
while True:
    print("Executando operação de manutenção...")
    time.sleep(1)  # Pode causar travamento sem uma condição de saída
import json
import random
import time

class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.id = random.randint(1000, 9999)

    def exibir_info(self):
        print(f"ID: {self.id} - Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}")

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def vender(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        return False

    def exibir_info(self):
        print(f"Produto: {self.nome}, Preço: {self.preco}, Estoque: {self.estoque}")

class Sistema:
    def __init__(self):
        self.usuarios = {}
        self.produtos = {}

    def adicionar_usuario(self, nome, idade, email):
        usuario = Usuario(nome, idade, email)
        self.usuarios[usuario.id] = usuario

    def adicionar_produto(self, nome, preco, estoque):
        produto = Produto(nome, preco, estoque)
        self.produtos[nome] = produto

    def listar_usuarios(self):
        for usuario in self.usuarios.values():
            usuario.exibir_info()

    def listar_produtos(self):
        for produto in self.produtos.values():
            produto.exibir_info()

    def processar_compra(self, user_id, produto_nome, quantidade):
        usuario = self.usuarios.get(user_id)
        produto = self.produtos.get(produto_nome)
        
        if not usuario or not produto:
            print("Usuário ou produto não encontrado!")
            return
        
        if produto.vender(quantidade):
            print(f"Compra realizada com sucesso para {usuario.nome}")
        else:
            print("Estoque insuficiente!")

    def salvar_dados(self):
        dados = {
            "usuarios": {uid: vars(usr) for uid, usr in self.usuarios.items()},
            "produtos": {p: vars(prod) for p, prod in self.produtos.items()}
        }
        try:
            with open("dados.json", "w") as f:
                json.dump(dados, f)
        except:
            print("Erro ao salvar os dados!")

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as f:
                dados = json.load(f)
                for uid, info in dados["usuarios"].items():
                    self.usuarios[int(uid)] = Usuario(info["nome"], info["idade"], info["email"])
                for nome, info in dados["produtos"].items():
                    self.produtos[nome] = Produto(info["nome"], info["preco"], info["estoque"])
        except:
            print("Erro ao carregar os dados!")

# Criando um sistema e adicionando usuários e produtos
sistema = Sistema()
sistema.adicionar_usuario("Alice", 25, "alice@email.com")
sistema.adicionar_usuario("Bob", 30, "bob@email.com")
sistema.adicionar_produto("Laptop", 3000, 10)
sistema.adicionar_produto("Mouse", 50, 200)

# Erros propositais:
sistema.adicionar_usuario("Charlie", "vinte", "charlie@email")  # Tipo incorreto para idade e email
sistema.processar_compra(9999, "Laptop", 2)  # ID de usuário inexistente
sistema.processar_compra(1000, "Teclado", 1)  # Produto inexistente

sistema.listar_usuarios()
sistema.listar_produtos()

# Salvar e carregar dados
sistema.salvar_dados()
sistema.carregar_dados()

# Loop infinito acidental (erro proposital)
while True:
    print("Executando operação de manutenção...")
    time.sleep(1)  # Pode causar travamento sem uma condição de saída
