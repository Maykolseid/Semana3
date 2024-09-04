import tkinter as tk
from tkinter import messagebox
import math


class SquareRootCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Raíz Cuadrada")

        # Etiqueta y entrada para el número
        self.label_number = tk.Label(root, text="Ingresa un número:")
        self.label_number.grid(row=0, column=0)
        self.entry_number = tk.Entry(root)
        self.entry_number.grid(row=0, column=1)

        # Botón para calcular la raíz cuadrada
        self.calculate_button = tk.Button(root, text="Calcular Raíz Cuadrada", command=self.calculate_square_root)
        self.calculate_button.grid(row=1, column=0, columnspan=2)

    def calculate_square_root(self):
        try:
            number = float(self.entry_number.get())
            calculator = SquareRootCalculator(number)
            result = calculator.calculate_square_root()
            messagebox.showinfo("Resultado", f"La raíz cuadrada de {number} es {result:.5f}.")

        except ValueError as e:
            messagebox.showerror("Error", str(e))


class SquareRootCalculator:
    def __init__(self, number):
        self.number = number

    def calculate_square_root(self):
        if self.number < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(self.number)


if __name__ == "__main__":
    root = tk.Tk()
    app = SquareRootCalculatorApp(root)
    root.mainloop()
