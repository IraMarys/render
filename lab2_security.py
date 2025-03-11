import tkinter as tk
from tkinter import filedialog, messagebox
import string
from math import gcd


def affine_encrypt(text, a, b, alphabet):
    m = len(alphabet)
    if gcd(a, m) != 1:
        raise ValueError("a повинно бути взаємно простим з довжиною алфавіту")

    encrypted_text = ""
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (a * idx + b) % m
            encrypted_text += alphabet[new_idx]
        else:
            encrypted_text += char
    return encrypted_text


alphabet = string.ascii_uppercase + string.ascii_lowercase + " ,.!"
a = 5
b = 8


def open_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            entry.delete("1.0", tk.END)
            entry.insert(tk.END, f.read())

def save_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Успіх", "Файл успішно збережено!")

def encrypt_text():
    global a, b
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        text = input_text.get("1.0", tk.END).strip()
        encrypted = affine_encrypt(text, a, b, alphabet)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))


root = tk.Tk()
root.title("Афінний шифр - Шифрування")
root.geometry("600x400")

# Верхній блок
frame_top = tk.Frame(root)
frame_top.pack(pady=5)

tk.Label(frame_top, text="Параметри шифрування").grid(row=0, column=0, columnspan=4)
tk.Label(frame_top, text="a=").grid(row=1, column=0)
entry_a = tk.Entry(frame_top, width=5, justify="center")
entry_a.grid(row=1, column=1)
entry_a.insert(0, str(a))

tk.Label(frame_top, text="b=").grid(row=1, column=2)
entry_b = tk.Entry(frame_top, width=5, justify="center")
entry_b.grid(row=1, column=3)
entry_b.insert(0, str(b))


frame_text = tk.Frame(root)
frame_text.pack(pady=10)

tk.Label(frame_text, text="Вхідний текст").grid(row=0, column=0)
tk.Label(frame_text, text="Зашифрований текст").grid(row=0, column=1)

input_text = tk.Text(frame_text, width=30, height=10)
input_text.grid(row=1, column=0, padx=5, pady=5)
output_text = tk.Text(frame_text, width=30, height=10)
output_text.grid(row=1, column=1, padx=5, pady=5)


frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_open = tk.Button(frame_buttons, text="Відкрити файл", command=lambda: open_file(input_text))
btn_open.grid(row=0, column=0, padx=5, pady=5)

btn_encrypt = tk.Button(frame_buttons, text="Зашифрувати", command=encrypt_text)
btn_encrypt.grid(row=0, column=1, padx=5, pady=5)

btn_save = tk.Button(frame_buttons, text="Зберегти", command=lambda: save_file(output_text.get("1.0", tk.END)))
btn_save.grid(row=0, column=2, padx=5, pady=5)


root.mainloop()