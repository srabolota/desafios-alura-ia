# ==============================================================
# LISTA DE TAREFAS EM PYTHON COM TKINTER (INTERFACE GRÁFICA DESKTOP)
# ==============================================================
# O Tkinter é a biblioteca padrão do Python para criar janelas desktop.
# Para rodar este arquivo: python lista_tarefas_tkinter.py
# ==============================================================

import tkinter as tk
from tkinter import messagebox

# 1. FUNÇÕES COM A LÓGICA DO PROGRAMA

def adicionar_tarefa():
    """Lê o texto digitado e adiciona à lista."""
    texto = entrada_tarefa.get().strip()
    
    if texto == "":
        messagebox.showwarning("Aviso", "Por favor, digite o nome de uma tarefa!")
        return
        
    lista_tarefas.insert(tk.END, f"[ ] {texto}")
    entrada_tarefa.delete(0, tk.END)  # Limpa o campo de entrada

def concluir_tarefa():
    """Marca ou desmarca a tarefa selecionada como concluída."""
    selecao = lista_tarefas.curselection()
    
    if not selecao:
        messagebox.showinfo("Aviso", "Selecione uma tarefa para concluir!")
        return
        
    indice = selecao[0]
    tarefa_atual = lista_tarefas.get(indice)
    
    # Alterna o marcador entre pendente [ ] e concluído [✓]
    if tarefa_atual.startswith("[ ]"):
        nova_tarefa = tarefa_atual.replace("[ ]", "[✓]", 1)
    elif tarefa_atual.startswith("[✓]"):
        nova_tarefa = tarefa_atual.replace("[✓]", "[ ]", 1)
    else:
        nova_tarefa = f"[✓] {tarefa_atual}"
        
    lista_tarefas.delete(indice)
    lista_tarefas.insert(indice, nova_tarefa)

def remover_tarefa():
    """Remove da lista a tarefa selecionada."""
    selecao = lista_tarefas.curselection()
    
    if not selecao:
        messagebox.showinfo("Aviso", "Selecione uma tarefa para remover!")
        return
        
    indice = selecao[0]
    lista_tarefas.delete(indice)


# 2. CONSTRUÇÃO DA INTERFACE VISUAL (JANELA E COMPONENTES)

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Lista de Tarefas (Tkinter)")
janela.geometry("400x480")
janela.configure(bg="#f1f5f9")

# Título no topo
rotulo_titulo = tk.Label(
    janela, 
    text="📝 Minha Lista de Tarefas", 
    font=("Arial", 16, "bold"), 
    bg="#f1f5f9", 
    fg="#1e293b"
)
rotulo_titulo.pack(pady=12)

# Campo de texto para digitar
entrada_tarefa = tk.Entry(janela, font=("Arial", 12), width=32)
entrada_tarefa.pack(pady=6, ipady=4)
# Permite adicionar também pressionando 'Enter' no teclado
entrada_tarefa.bind("<Return>", lambda event: adicionar_tarefa())

# Botão Adicionar
btn_adicionar = tk.Button(
    janela, 
    text="Adicionar Tarefa", 
    font=("Arial", 10, "bold"), 
    bg="#3b82f6", 
    fg="white", 
    padx=10, 
    pady=4, 
    command=adicionar_tarefa
)
btn_adicionar.pack(pady=6)

# Área da Lista (Listbox) com Barra de Rolagem (Scrollbar)
frame_lista = tk.Frame(janela, bg="#f1f5f9")
frame_lista.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tarefas = tk.Listbox(
    frame_lista, 
    font=("Arial", 11), 
    selectbackground="#cbd5e1", 
    selectforeground="#0f172a", 
    yscrollcommand=scrollbar.set, 
    bd=1, 
    relief=tk.SOLID
)
lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_tarefas.yview)

# Botões de Ação (Concluir e Remover)
frame_botoes = tk.Frame(janela, bg="#f1f5f9")
frame_botoes.pack(pady=14)

btn_concluir = tk.Button(
    frame_botoes, 
    text="Concluir / Desfazer", 
    font=("Arial", 10), 
    bg="#10b981", 
    fg="white", 
    padx=8, 
    pady=4, 
    command=concluir_tarefa
)
btn_concluir.pack(side=tk.LEFT, padx=6)

btn_remover = tk.Button(
    frame_botoes, 
    text="Remover", 
    font=("Arial", 10), 
    bg="#ef4444", 
    fg="white", 
    padx=8, 
    pady=4, 
    command=remover_tarefa
)
btn_remover.pack(side=tk.LEFT, padx=6)

# 3. LOOP PRINCIPAL
# Mantém a janela aberta e escutando cliques do mouse e teclado
if __name__ == "__main__":
    janela.mainloop()
