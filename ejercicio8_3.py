
import tkinter as tk
from tkinter import messagebox
import math


class Figura:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0


class Cilindro(Figura):
    def __init__(self, radio, altura):
        super().__init__()
        self.volumen = math.pi * radio ** 2 * altura
        self.superficie = 2 * math.pi * radio * (radio + altura)


class Esfera(Figura):
    def __init__(self, radio):
        super().__init__()
        self.volumen = (4 / 3) * math.pi * radio ** 3
        self.superficie = 4 * math.pi * radio ** 2


class Piramide(Figura):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.volumen = base ** 2 * altura / 3
        self.superficie = base ** 2 + 2 * base * apotema


class Cubo(Figura):
    def __init__(self, lado):
        super().__init__()
        self.volumen = lado ** 3
        self.superficie = 6 * lado ** 2


class Prisma(Figura):
    def __init__(self, base, altura, profundidad):
        super().__init__()
        self.volumen = base * altura * profundidad
        self.superficie = 2 * (
            base * altura + base * profundidad + altura * profundidad
        )


class VentanaFigura:
    def __init__(self, ventana, titulo, campos, figura):
        self.ventana = tk.Toplevel(ventana)
        self.ventana.title(titulo)
        self.ventana.geometry("300x280")

        self.tipo_figura = figura
        self.entradas = []

        for i, campo in enumerate(campos):
            tk.Label(self.ventana, text=campo + ":").place(
                x=20, y=20 + i * 30
            )

            entrada = tk.Entry(self.ventana)
            entrada.place(x=130, y=20 + i * 30, width=100)
            self.entradas.append(entrada)

        tk.Button(
            self.ventana, text="Calcular", command=self.calcular
        ).place(x=100, y=30 + len(campos) * 30)

        self.resultado_volumen = tk.Label(
            self.ventana, text="Volumen = "
        )
        self.resultado_volumen.place(x=20, y=180)

        self.resultado_superficie = tk.Label(
            self.ventana, text="Superficie = "
        )
        self.resultado_superficie.place(x=20, y=210)

    def calcular(self):
        try:
            valores = []

            for entrada in self.entradas:
                dato = entrada.get()

                if dato == "":
                    messagebox.showwarning(
                        "Aviso", "Completa todos los campos."
                    )
                    return

                numero = float(dato)

                if numero <= 0:
                    messagebox.showwarning(
                        "Aviso", "Los valores deben ser mayores que cero."
                    )
                    return

                valores.append(numero)

            figura = self.tipo_figura(*valores)

            self.resultado_volumen.config(
                text=f"Volumen = {figura.volumen:.2f} cm³"
            )
            self.resultado_superficie.config(
                text=f"Superficie = {figura.superficie:.2f} cm²"
            )

        except ValueError:
            messagebox.showerror(
                "Error", "Ingresa solamente números válidos."
            )


class MenuPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cálculo de Figuras")
        self.ventana.geometry("360x180")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana, text="Selecciona una figura"
        ).pack(pady=15)

        tk.Button(
            ventana, text="Cilindro",
            command=lambda: self.abrir(
                "Cilindro", ["Radio", "Altura"], Cilindro
            )
        ).place(x=20, y=55, width=90)

        tk.Button(
            ventana, text="Esfera",
            command=lambda: self.abrir(
                "Esfera", ["Radio"], Esfera
            )
        ).place(x=135, y=55, width=90)

        tk.Button(
            ventana, text="Pirámide",
            command=lambda: self.abrir(
                "Pirámide", ["Base", "Altura", "Apotema"], Piramide
            )
        ).place(x=250, y=55, width=90)

        tk.Button(
            ventana, text="Cubo",
            command=lambda: self.abrir(
                "Cubo", ["Lado"], Cubo
            )
        ).place(x=75, y=105, width=90)

        tk.Button(
            ventana, text="Prisma",
            command=lambda: self.abrir(
                "Prisma", ["Base", "Altura", "Profundidad"], Prisma
            )
        ).place(x=195, y=105, width=90)

    def abrir(self, titulo, campos, figura):
        VentanaFigura(self.ventana, titulo, campos, figura)


ventana = tk.Tk()
app = MenuPrincipal(ventana)
ventana.mainloop()

