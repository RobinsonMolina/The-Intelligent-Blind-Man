import tkinter as tk
from tkinter import messagebox

def validate_selection():
    black_count = 0
    
    if normal_beret_var.get() == "Negra":
        black_count += 1
    if one_eye_beret_var.get() == "Negra":
        black_count += 1
    if blind_beret_var.get() == "Negra":
        black_count += 1

    if black_count > 2:
        messagebox.showwarning("Error", "No pueden haber más de dos boinas negras.")
    else:
        solve_puzzle()

def solve_puzzle():
    one_eye_beret = one_eye_beret_var.get()
    blind_beret = blind_beret_var.get()

    if one_eye_beret == "Negra" and blind_beret == "Negra":
        result = "El prisionero con vista normal gana al deducir que lleva una boina blanca."
    else:
        if blind_beret == "Negra":
            result = "El prisionero tuerto gana al deducir que lleva una boina blanca."
        else:
            result = "El ciego gana al deducir que lleva una boina blanca."

    messagebox.showinfo("Resultado", result)

window = tk.Tk()
window.title("El Ciego Inteligente")
window.geometry("400x400")

title = tk.Label(window, text="Enigma: El Ciego Inteligente", font=("Helvetica", 16))
title.pack(pady=10)

instruction = tk.Label(window, text="Introduce los colores de las boinas de los prisioneros:", font=("Helvetica", 12))
instruction.pack(pady=10)

tk.Label(window, text="Prisionero con vista normal:").pack()
normal_beret_var = tk.StringVar()
normal_beret_var.set("Blanca")
option_normal_1 = tk.Radiobutton(window, text="Blanca", variable=normal_beret_var, value="Blanca")
option_normal_1.pack()
option_normal_2 = tk.Radiobutton(window, text="Negra", variable=normal_beret_var, value="Negra")
option_normal_2.pack()

tk.Label(window, text="Prisionero tuerto:").pack()
one_eye_beret_var = tk.StringVar()
one_eye_beret_var.set("Blanca")
option_one_eye_1 = tk.Radiobutton(window, text="Blanca", variable=one_eye_beret_var, value="Blanca")
option_one_eye_1.pack()
option_one_eye_2 = tk.Radiobutton(window, text="Negra", variable=one_eye_beret_var, value="Negra")
option_one_eye_2.pack()

tk.Label(window, text="Prisionero ciego:").pack()
blind_beret_var = tk.StringVar()
blind_beret_var.set("Blanca")
option_blind_1 = tk.Radiobutton(window, text="Blanca", variable=blind_beret_var, value="Blanca")
option_blind_1.pack()
option_blind_2 = tk.Radiobutton(window, text="Negra", variable=blind_beret_var, value="Negra")
option_blind_2.pack()

solve_button = tk.Button(window, text="Resolver", command=validate_selection)
solve_button.pack(pady=20)

window.mainloop()
