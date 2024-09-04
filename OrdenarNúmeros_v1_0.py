import tkinter as tk
from tkinter import messagebox


class NumberSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenar Números")

        # Etiquetas y entradas para los números
        self.label1 = tk.Label(root, text="Número 1:")
        self.label1.grid(row=0, column=0)
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(root, text="Número 2:")
        self.label2.grid(row=1, column=0)
        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=1, column=1)

        self.label3 = tk.Label(root, text="Número 3:")
        self.label3.grid(row=2, column=0)
        self.entry3 = tk.Entry(root)
        self.entry3.grid(row=2, column=1)

        # Botón para ordenar los números
        self.sort_button = tk.Button(root, text="Ordenar", command=self.sort_numbers)
        self.sort_button.grid(row=3, column=0, columnspan=2)

    def sort_numbers(self):
        try:
            # Leer los números de las entradas
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            num3 = float(self.entry3.get())

            # Crear una lista con los números y ordenarla
            numbers = [num1, num2, num3]
            numbers.sort()

            # Mostrar los números ordenados
            messagebox.showinfo("Números Ordenados", f"Orden Ascendente: {numbers}")

        except ValueError:
            # Mostrar un mensaje de error si la entrada no es un número válido
            messagebox.showerror("Error", "Por favor, ingrese solo números válidos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSorterApp(root)
    root.mainloop()
