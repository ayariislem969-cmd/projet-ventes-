import pandas as pd
import matplotlib.pyplot as plt

# 1. Lire le fichier CSV
df = pd.read_csv('ventes.csv', sep=';')

# 2. Calculs
df['CA_Brut'] = df['Prix'] * df['Quantite']
df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)
df['TVA'] = df['CA_Net'] * 0.20

# 🔥 BONUS 1: Arrondi
df = df.round(2)

# 🔥 BONUS 2: Trier du meilleur CA au pire
df = df.sort_values(by='CA_Net', ascending=False)

# 3. CA Total
total_ca = df['CA_Net'].sum()

# 4. Meilleur produit
top_product_id = df.iloc[0]['ID']

# 🔥 BONUS 3: Affichage propre
print("\n===== RÉSULTATS =====")
print(df)
print("\n💰 CA Total:", total_ca)
print("🏆 Meilleur produit ID:", top_product_id)

# 5. Export CSV
df.to_csv('resultats_final.csv', index=False)

# 🔥 BONUS 4: Export Excel
df.to_excel('resultats_final.xlsx', index=False)

print("\n✅ Fichiers exportés (CSV + Excel)")

# 🔥 BONUS 5: Graphique amélioré
plt.figure()
plt.bar(df['ID'].astype(str), df['CA_Net'])
plt.xlabel('Produit ID')
plt.ylabel('CA Net')
plt.title('Chiffre d\'affaires par produit')
plt.grid()
plt.show()