import tkinter as tk
from tkinter import simpledialog, messagebox

def calcular_pontos_para_passar():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    
    try:
        mtpp = float(simpledialog.askstring("Média", "Qual é a média necessária para passar?"))
        qtd_materias = int(simpledialog.askstring("Quantidade", "Quantos elementos você deseja adicionar?"))
        materias = []

        for i in range(qtd_materias):
            nome = simpledialog.askstring("Matéria", f"Digite o nome do {i+1}º elemento:")
            materias.append(nome)

        resultado = ""
        for materia in materias:
            qbjt = int(simpledialog.askstring("Bimestres", f"Quantos bimestres você já tem nota para {materia}?"))
            notas = []

            for i in range(1, qbjt + 1):
                nota = float(simpledialog.askstring("Nota", f"Digite a nota do {i}º bimestre:"))
                notas.append(nota)

            total_notas = sum(notas)
            pontos_faltantes = max(0, mtpp - total_notas)
            
            resultado += f"\nMatéria: {materia}\n"
            resultado += f"Notas informadas: {notas}\n"
            resultado += f"Soma das notas: {total_notas:.1f}\n"
            if pontos_faltantes > 0:
                resultado += f"Faltam {pontos_faltantes:.1f} pontos para atingir a média de {mtpp}.\n"
            else:
                resultado += "Parabéns! Você já atingiu ou superou a média necessária.\n"

        messagebox.showinfo("Resultado", resultado)

    except ValueError as ve:
        messagebox.showerror("Erro", f"Erro de valor: {ve}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

calcular_pontos_para_passar()
