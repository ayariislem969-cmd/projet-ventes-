import matplotlib
matplotlib.use('Agg')  # ← OBLIGATOIRE pour VS Code
import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# 1. Lire le fichier CSV
# ============================================================
df = pd.read_csv('ventes.csv', sep=';')

# ============================================================
# 2. Calculs
# ============================================================
df['CA_Brut'] = df['Prix'] * df['Quantite']
df['CA_Net']  = df['CA_Brut'] * (1 - df['Remise'] / 100)
df['TVA']     = df['CA_Net'] * 0.20
df = df.round(2)

# Trier du meilleur CA au pire
df = df.sort_values(by='CA_Net', ascending=False)

# ============================================================
# 3. Affichage
# ============================================================
total_ca      = df['CA_Net'].sum()
top_product   = df.iloc[0]['ID']

print("\n===== RÉSULTATS =====")
print(df.to_string(index=False))
print(f"\n💰 CA Total   : {total_ca:.2f} €")
print(f"🏆 Meilleur produit ID : {top_product}")

# ============================================================
# 4. Export CSV + Excel
# ============================================================
df.to_csv('resultats_final.csv', index=False)
df.to_excel('resultats_final.xlsx', index=False)
print("\n✅ Fichiers exportés (CSV + Excel)")

# ============================================================
# 5. Graphique — sauvegardé en PNG
# ============================================================
plt.figure(figsize=(9, 5))
bars = plt.bar(df['ID'].astype(str), df['CA_Net'], color='skyblue', edgecolor='white')
plt.title("Chiffre d'Affaires Net par Produit", fontsize=14, fontweight='bold')
plt.xlabel("ID Produit")
plt.ylabel("CA Net (€)")
plt.bar_label(bars, fmt='%.2f', fontsize=9)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

plt.savefig('graphique.png', dpi=150)  # ← sauvegarde en image
print("📊 Graphique sauvegardé : graphique.png")
plt.close()