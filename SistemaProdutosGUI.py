import tkinter as tk

class SistemaProdutos:
    def __init__(self):
        self.produtos = {}
        # Adicione mais produtos conforme necessário
        self.criar_produto("Banana", 1.50)
        self.criar_produto("Maçã", 1.20)
        self.criar_produto("Pêra", 1.75)
        self.criar_produto("Laranja", 2.00)
        self.criar_produto("Abacate", 3.50)

        self.produtos_selecionados = {}

    def criar_produto(self, nome, valor):
        self.produtos[nome] = {'valor': valor, 'quantidade': 0}

    def escolher_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos_selecionados[nome] = {'valor': self.produtos[nome]['valor'], 'quantidade': quantidade}
            total = self.produtos_selecionados[nome]['valor'] * quantidade
            return total
        else:
            return "Produto não encontrado."

    def apagar_produto(self, nome):
        if nome in self.produtos_selecionados:
            del self.produtos_selecionados[nome]

    def calcular_valor_total(self):
        total = sum(self.produtos_selecionados[nome]['valor'] * self.produtos_selecionados[nome]['quantidade'] for nome in self.produtos_selecionados)
        return total

class SistemaProdutosGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Produtos")

        self.sistema = SistemaProdutos()

        self.create_widgets()

    def create_widgets(self):
        # Rótulo e entrada para o nome do produto
        self.produto_label = tk.Label(self.master, text="Nome do Produto:")
        self.produto_label.grid(row=0, column=0, sticky="w")

        self.produto_entry = tk.Entry(self.master)
        self.produto_entry.grid(row=0, column=1, padx=10, pady=10)

        # Rótulo e entrada para a quantidade
        self.quantidade_label = tk.Label(self.master, text="Quantidade:")
        self.quantidade_label.grid(row=1, column=0, sticky="w")

        self.quantidade_entry = tk.Entry(self.master)
        self.quantidade_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botão para escolher o produto
        self.escolher_button = tk.Button(self.master, text="Escolher Produto", command=self.escolher_produto)
        self.escolher_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Botão para apagar produto
        self.apagar_button = tk.Button(self.master, text="Apagar Produto", command=self.apagar_produto)
        self.apagar_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Rótulo para exibir o total da compra
        self.total_label = tk.Label(self.master, text="Total da Compra: R$ 0.00")
        self.total_label.grid(row=4, column=0, columnspan=2, pady=10)

    def escolher_produto(self):
        produto = self.produto_entry.get()
        quantidade = int(self.quantidade_entry.get())

        total_compra = self.sistema.escolher_produto(produto, quantidade)

        if isinstance(total_compra, str):
            # Se o produto não foi encontrado
            self.total_label.config(text=total_compra)
        else:
            # Atualiza o rótulo com o total da compra
            self.atualizar_valor_total()

    def apagar_produto(self):
        produto = self.produto_entry.get()
        self.sistema.apagar_produto(produto)
        self.atualizar_valor_total()

    def atualizar_valor_total(self):
        valor_total_compra = self.sistema.calcular_valor_total()
        self.total_label.config(text=f"Total da Compra: R$ {valor_total_compra:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaProdutosGUI(root)
    root.mainloop()
