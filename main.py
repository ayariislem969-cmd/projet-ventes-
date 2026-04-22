import pandas as pd

# 1. Lire fichier CSV
df = pd.read_csv("ventes.csv")

# 2. Calculs
df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.20

# 3. Export final EXACT comme GitHub
df.to_csv("resultats_final.csv", index=False)

print("✅ Fichier resultats_final.csv créé !")