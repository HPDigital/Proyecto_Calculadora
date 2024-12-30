import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        # Variable para almacenar la expresión
        self.expresion = ""
        
        # Crear entrada
        self.entrada = ttk.Entry(root, justify="right", font=('Arial', 15))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Definir botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Crear y posicionar botones
        row = 1
        col = 0
        for boton in botones:
            comando = lambda x=boton: self.click_boton(x)
            ttk.Button(root, text=boton, command=comando).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Agregar botón de limpiar
        ttk.Button(root, text="C", command=self.limpiar).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        # Configurar el peso de las filas y columnas
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def click_boton(self, caracter):
        if caracter == '=':
            try:
                # Evaluar la expresión y mostrar el resultado
                resultado = eval(self.expresion)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
                self.expresion = str(resultado)
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
                self.expresion = ""
        else:
            # Agregar el caracter a la expresión
            self.expresion += caracter
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, self.expresion)
    
    def limpiar(self):
        self.expresion = ""
        self.entrada.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("300x400")
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main() 