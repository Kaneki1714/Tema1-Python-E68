import pandas as pd
import matplotlib.pyplot as plt

# Parametrii calculati pentru Valeanu Stefan-Marian
X = len("Stefan-Marian")  # 13 (X % 6 == 1)
Y = len("Valeanu")        # 7

# 1. Importul datelor din fisierul CSV folosind pandas
df = pd.read_csv("data.csv")

# Graficul 1: Toate valorile (Durata, Puls, MaxPuls, Calorii)
df.plot(title="Toate valorile (Durata, Puls, MaxPuls, Calorii)")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.grid(True)

# Graficul 2: Primele X = 13 valori (Durata, Puls, Calorii)
df_primele_X = df[["Durata", "Puls", "Calorii"]].head(X)
df_primele_X.plot(title=f"Primele {X} valori (Durata, Puls, Calorii)")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.grid(True)

# Graficul 3: Ultimele Y = 7 valori (Durata si Puls)
# Pentru X % 6 == 1: culori albastru si galben, marker triunghi in sus ('^')
df_ultimele_Y = df[["Durata", "Puls"]].tail(Y)
df_ultimele_Y.plot(
    color=["blue", "yellow"],
    marker="^",
    title=f"Ultimele {Y} valori (Durata si Puls) - X%6 == 1"
)
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.grid(True)

# Afisarea tuturor celor 3 ferestre grafice
plt.show()
