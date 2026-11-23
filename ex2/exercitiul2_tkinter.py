import tkinter as tk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# 1. Calculul parametrilor (Valeanu Stefan-Marian)
X = len("Stefan-Marian")  # 13 -> X % 6 == 1
Y = len("Valeanu")        # 7

# 2. Citirea datelor din CSV cu pandas
df = pd.read_csv("data.csv")


def afiseaza_grafic(optiune):
    """Sterge graficul curent si deseneaza graficul ales in aceeasi fereastra."""
    ax.clear()

    if optiune == 1:
        df.plot(ax=ax)
        ax.set_title("Toate valorile (Durata, Puls, MaxPuls, Calorii)")
    elif optiune == 2:
        df_primele_X = df[["Durata", "Puls", "Calorii"]].head(X)
        df_primele_X.plot(ax=ax)
        ax.set_title(f"Primele {X} valori (Durata, Puls, Calorii)")
    elif optiune == 3:
        df_ultimele_Y = df[["Durata", "Puls"]].tail(Y)
        df_ultimele_Y.plot(ax=ax, color=["blue", "yellow"], marker="^")
        ax.set_title(f"Ultimele {Y} valori (Durata si Puls) - X%6 == 1")

    ax.set_xlabel("Index")
    ax.set_ylabel("Valoare")
    ax.grid(True)
    canvas.draw()


# 3. Crearea ferestrei principale Tkinter
root = tk.Tk()
root.title("Problema 2 | Interfata nativa Tkinter")
root.geometry("900x620")

# 4. Bara superioara cu cele 3 butoane de selectie
frame_butoane = tk.Frame(root, pady=10)
frame_butoane.pack(side=tk.TOP, fill=tk.X)

btn1 = tk.Button(
    frame_butoane,
    text="1. Toate valorile",
    width=22,
    command=lambda: afiseaza_grafic(1)
)
btn1.pack(side=tk.LEFT, padx=10, expand=True)

btn2 = tk.Button(
    frame_butoane,
    text=f"2. Primele {X} valori",
    width=22,
    command=lambda: afiseaza_grafic(2)
)
btn2.pack(side=tk.LEFT, padx=10, expand=True)

btn3 = tk.Button(
    frame_butoane,
    text=f"3. Ultimele {Y} valori (X%6==1)",
    width=26,
    command=lambda: afiseaza_grafic(3)
)
btn3.pack(side=tk.LEFT, padx=10, expand=True)

# 5. Zona grafica Matplotlib integrata in fereastra Tkinter
fig = Figure(figsize=(8.5, 5), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# 6. Bara interactiva Matplotlib (Zoom, Pan, Reset, Salvare PNG)
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X)

# 7. Afisarea implicita a primului grafic la deschidere
afiseaza_grafic(1)

# 8. Pornirea buclei de evenimente a interfetei grafice
root.mainloop()
