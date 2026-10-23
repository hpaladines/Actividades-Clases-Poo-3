import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0.0
        for nota in self.lista_notas:
            suma += math.pow(nota - prom, 2)
        return math.sqrt(suma / len(self.lista_notas))

    def nota_mayor(self):
        return max(self.lista_notas)

    def nota_menor(self):
        return min(self.lista_notas)

class VentanaNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Notas")
        self.geometry("320x400")
        self.resizable(False, False)

        self.entradas_notas = []
        
        for i in range(5):
            etiqueta = tk.Label(self, text=f"Ingrese Nota {i+1}:")
            etiqueta.place(x=20, y=20 + (i*30))
            
            caja_texto = tk.Entry(self)
            caja_texto.place(x=130, y=20 + (i*30), width=120)
            self.entradas_notas.append(caja_texto)

        boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        boton_calcular.place(x=60, y=180, width=80)
        
        boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        boton_limpiar.place(x=160, y=180, width=80)

        self.texto_promedio = tk.Label(self, text="Promedio = ")
        self.texto_promedio.place(x=20, y=230)
        
        self.texto_desviacion = tk.Label(self, text="Desviación = ")
        self.texto_desviacion.place(x=20, y=260)
        
        self.texto_mayor = tk.Label(self, text="Nota mayor = ")
        self.texto_mayor.place(x=20, y=290)
        
        self.texto_menor = tk.Label(self, text="Nota menor = ")
        self.texto_menor.place(x=20, y=320)

    def calcular(self):
        registro_notas = Notas()
        try:
            for i in range(5):
                valor = self.entradas_notas[i].get()
                if valor == "":
                    messagebox.showwarning("Alerta", f"Falta ingresar la nota {i+1}.")
                    return
                registro_notas.lista_notas[i] = float(valor)

            self.texto_promedio.config(text=f"Promedio = {registro_notas.calcular_promedio():.2f}")
            self.texto_desviacion.config(text=f"Desviación = {registro_notas.calcular_desviacion():.2f}")
            self.texto_mayor.config(text=f"Nota mayor = {registro_notas.nota_mayor():.2f}")
            self.texto_menor.config(text=f"Nota menor = {registro_notas.nota_menor():.2f}")

        except ValueError:
            messagebox.showerror("Error", "Debe ingresar solo números.")

    def limpiar(self):
        for caja in self.entradas_notas:
            caja.delete(0, tk.END)
        self.texto_promedio.config(text="Promedio = ")
        self.texto_desviacion.config(text="Desviación = ")
        self.texto_mayor.config(text="Nota mayor = ")
        self.texto_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    programa = VentanaNotas()
    programa.mainloop()