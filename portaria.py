import tkinter as tk
from tkinter import messagebox
import json
import tkinter.font as tkFont

class CondominioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Condomínio")
        self.root.geometry("800x600")  # Tamanho inicial da janela
        self.root.configure(bg="#f0f0f0")  # Cor de fundo geral

        self.usuarios = {}
        self.moradores = []
        self.mercadorias = {}

        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_font = tkFont.Font(family="Arial", size=10)

        menubar = tk.Menu(self.root, bg="#3498db", fg="white", font=menu_font)  # Menu azul
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0, bg="white", font=menu_font)
        file_menu.add_command(label="Salvar", command=self.salvar_dados)
        file_menu.add_command(label="Carregar", command=self.carregar_dados)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        menubar.add_cascade(label="Arquivo", menu=file_menu)

    def criar_widgets(self):
        frame = tk.Frame(self.root, bg="#ecf0f1")  # Cinza claro para o frame principal
        frame.pack(expand=True, fill='both', padx=20, pady=20)  # Mais espaço ao redor

        # Configurar pesos para as linhas e colunas para o frame se expandir corretamente
        for i in range(17):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Estilo para os labels
        label_style = {'bg': '#ecf0f1', 'font': ('Arial', 10)}

        # Estilo para as entradas
        entry_style = {'bg': 'white', 'font': ('Arial', 10)}

        # Estilo para os botões
        button_style = {'bg': '#3498db', 'fg': 'white', 'font': ('Arial', 10, 'bold'), 'relief': 'raised', 'borderwidth': 2}

        # Usuários
        tk.Label(frame, text="Usuário:", **label_style).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.usuario_entry = tk.Entry(frame, **entry_style)
        self.usuario_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(frame, text="Senha:", **label_style).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.senha_entry = tk.Entry(frame, show="*", **entry_style)
        self.senha_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        tk.Button(frame, text="Cadastrar Usuário:", command=self.cadastrar_usuario, **button_style).grid(row=2, column=0, columnspan=2, pady=5, sticky="ew", padx=5)
        tk.Button(frame, text="Autenticar Usuário:", command=self.autenticar_usuario, **button_style).grid(row=3, column=0, columnspan=2, pady=5, sticky="ew", padx=5)

        # Moradores
        tk.Label(frame, text="Nome do Morador:", **label_style).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.morador_nome_entry = tk.Entry(frame, **entry_style)
        self.morador_nome_entry.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(frame, text="Bloco/Apartamento:", **label_style).grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.morador_apartamento_entry = tk.Entry(frame, **entry_style)
        self.morador_apartamento_entry.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(frame, text="Telefone:", **label_style).grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.morador_telefone_entry = tk.Entry(frame, **entry_style)
        self.morador_telefone_entry.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(frame, text="WhatsApp:", **label_style).grid(row=7, column=0, sticky="ew", padx=5, pady=5)
        self.morador_whatsapp_entry = tk.Entry(frame, **entry_style)
        self.morador_whatsapp_entry.grid(row=7, column=1, sticky="ew", padx=5, pady=5)

        tk.Button(frame, text="Adicionar Morador:", command=self.adicionar_morador, **button_style).grid(row=8, column=0, columnspan=2, pady=5, sticky="ew", padx=5)
        tk.Button(frame, text="Listar Moradores:", command=self.listar_moradores, **button_style).grid(row=9, column=0, columnspan=2, pady=5, sticky="ew", padx=5)

        # Mercadorias
        tk.Label(frame, text="Número da Nota Fiscal:", **label_style).grid(row=10, column=0, sticky="ew", padx=5, pady=5)
        self.mercadoria_nota_fiscal_entry = tk.Entry(frame, **entry_style)
        self.mercadoria_nota_fiscal_entry.grid(row=10, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(frame, text="Descrição da Mercadoria:", **label_style).grid(row=11, column=0, sticky="ew", padx=5, pady=5)
        self.mercadoria_descricao_entry = tk.Entry(frame, **entry_style)
        self.mercadoria_descricao_entry.grid(row=11, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(frame, text="Entregue Para o morador:", **label_style).grid(row=12, column=0, sticky="ew", padx=5, pady=5)
        self.mercadoria_morador_entry = tk.Entry(frame, **entry_style)
        self.mercadoria_morador_entry.grid(row=12, column=1, sticky="ew", padx=5, pady=5)

        tk.Button(frame, text="Registrar Mercadoria:", command=self.registrar_mercadoria, **button_style).grid(row=13, column=0, columnspan=2, pady=5, sticky="ew", padx=5)
        tk.Button(frame, text="Marcar como Entregue:", command=self.entregue_para, **button_style).grid(row=14, column=0, columnspan=2, pady=5, sticky="ew", padx=5)
        tk.Button(frame, text="Listar Mercadorias:", command=self.listar_mercadorias, **button_style).grid(row=15, column=0, columnspan=2, pady=5, sticky="ew", padx=5)

        # Text area para exibir informações
        self.output_text = tk.Text(frame, height=10, width=50, bg="white")
        self.output_text.grid(row=16, column=0, columnspan=2, pady=10, sticky="ew", padx=5)

    def cadastrar_usuario(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        if usuario and senha:
            if usuario not in self.usuarios:
                self.usuarios[usuario] = senha
                messagebox.showinfo("Sucesso", f"Usuário '{usuario}' cadastrado!")
            else:
                messagebox.showerror("Erro", f"Usuário '{usuario}' já existe.")
        else:
            messagebox.showerror("Erro", "Preencha usuário e senha.")

    def autenticar_usuario(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        if usuario and senha:
            if usuario in self.usuarios and self.usuarios[usuario] == senha:
                messagebox.showinfo("Sucesso", "Autenticação bem-sucedida!")
            else:
                messagebox.showerror("Erro", "Falha na autenticação.")
        else:
            messagebox.showerror("Erro", "Preencha usuário e senha.")

    def adicionar_morador(self):
        nome = self.morador_nome_entry.get()
        apartamento = self.morador_apartamento_entry.get()
        telefone = self.morador_telefone_entry.get()
        whatsapp = self.morador_whatsapp_entry.get()

        if nome and apartamento:
            morador_info = {
                "nome": nome,
                "apartamento": apartamento,
                "telefone": telefone,
                "whatsapp": whatsapp
            }
            self.moradores.append(morador_info)
            messagebox.showinfo("Sucesso", f"Morador '{nome}' adicionado!")
            # Limpa os campos após adicionar
            self.morador_nome_entry.delete(0, tk.END)
            self.morador_apartamento_entry.delete(0, tk.END)
            self.morador_telefone_entry.delete(0, tk.END)
            self.morador_whatsapp_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Nome e Apartamento são obrigatórios.")

    def listar_moradores(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Lista de Moradores:\n")
        for morador in self.moradores:
            self.output_text.insert(tk.END, f"- Nome: {morador['nome']}, Apartamento: {morador['apartamento']}, Telefone: {morador['telefone']}, WhatsApp: {morador['whatsapp']}\n")

    def registrar_mercadoria(self):
        nota_fiscal = self.mercadoria_nota_fiscal_entry.get()
        descricao = self.mercadoria_descricao_entry.get()
        morador_nome = self.mercadoria_morador_entry.get()

        if nota_fiscal and descricao and morador_nome:
            # Encontra o morador na lista de moradores
            morador = next((m for m in self.moradores if m['nome'] == morador_nome), None)
            if morador:
                mercadoria = {
                    "nota_fiscal": nota_fiscal,
                    "descricao": descricao,
                    "entregue": False
                }
                if morador['nome'] not in self.mercadorias:
                    self.mercadorias[morador['nome']] = []
                self.mercadorias[morador['nome']].append(mercadoria)
                messagebox.showinfo("Sucesso", f"Mercadoria '{descricao}' registrada para {morador['nome']}.")
                # Limpa os campos após registrar
                self.mercadoria_nota_fiscal_entry.delete(0, tk.END)
                self.mercadoria_descricao_entry.delete(0, tk.END)
                self.mercadoria_morador_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", f"Morador '{morador_nome}' não encontrado.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos de mercadoria.")

    def entregue_para(self):
        morador_nome = self.mercadoria_morador_entry.get()
        nota_fiscal = self.mercadoria_nota_fiscal_entry.get()

        if morador_nome and nota_fiscal:
            if morador_nome in self.mercadorias:
                for mercadoria in self.mercadorias[morador_nome]:
                    if mercadoria['nota_fiscal'] == nota_fiscal:
                        mercadoria['entregue'] = True
                        messagebox.showinfo("Sucesso", f"Mercadoria com nota fiscal '{nota_fiscal}' marcada como entregue para {morador_nome}.")
                        self.mercadoria_nota_fiscal_entry.delete(0, tk.END)
                        return
                messagebox.showerror("Erro", f"Mercadoria com nota fiscal '{nota_fiscal}' não encontrada para {morador_nome}.")
            else:
                messagebox.showerror("Erro", f"Não há mercadorias registradas para {morador_nome}.")
        else:
            messagebox.showerror("Erro", "Preencha o nome do morador e o número da nota fiscal.")

    def listar_mercadorias(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Lista de Mercadorias:\n")
        for morador, mercadorias in self.mercadorias.items():
            self.output_text.insert(tk.END, f"\nMorador: {morador}\n")
            for mercadoria in mercadorias:
                status = "Entregue" if mercadoria['entregue'] else "Pendente"
                self.output_text.insert(tk.END, f"- Nota Fiscal: {mercadoria['nota_fiscal']}, Descrição: {mercadoria['descricao']}, Status: {status}\n")

    def salvar_dados(self):
        dados = {
            "usuarios": self.usuarios,
            "moradores": self.moradores,
            "mercadorias": self.mercadorias
        }
        try:
            with open("dados_condominio.json", "w") as arquivo:
                json.dump(dados, arquivo, indent=4) # Adicionado indentação para facilitar a leitura
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {e}")

    def carregar_dados(self):
        try:
            with open("dados_condominio.json", "r") as arquivo:
                dados = json.load(arquivo)
                self.usuarios = dados.get("usuarios", {})
                self.moradores = dados.get("moradores", [])
                self.mercadorias = dados.get("mercadorias", {})
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
        except FileNotFoundError:
            messagebox.showinfo("Info", "Arquivo de dados não encontrado. Iniciando com dados padrão.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CondominioGUI(root)
    root.mainloop()