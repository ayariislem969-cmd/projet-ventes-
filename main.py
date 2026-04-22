import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import os

# ============================================================
# LECTURE DYNAMIQUE — détecte séparateur et taille
# ============================================================

def lire_csv_dynamique(nom_fichier):
    """Lit n'importe quel fichier CSV quelle que soit sa taille."""

    # Vérifier que le fichier existe
    if not os.path.exists(nom_fichier):
        print(f"❌ Fichier '{nom_fichier}' introuvable !")
        return None

    # Détecter automatiquement le séparateur (; ou ,)
    with open(nom_fichier, "r", encoding="utf-8") as f:
        premiere_ligne = f.readline()
        separateur = ';' if ';' in premiere_ligne else ','

    # Lire le fichier avec pandas
    df = pd.read_csv(nom_fichier, sep=separateur)

    # Infos sur le fichier
    taille = os.path.getsize(nom_fichier)
    print(f"\n📂 Fichier      : {nom_fichier}")
    print(f"📏 Taille       : {taille} octets")
    print(f"🔍 Séparateur   : '{separateur}'")
    print(f"📋 Colonnes     : {list(df.columns)}")
    print(f"🔢 Nb de lignes : {len(df)}")

    return df

# ============================================================
# 1. Lire le fichier CSV (dynamique)
# ============================================================
df = lire_csv_dynamique('ventes.csv')

if df is None:
    exit()  # Arrêter si fichier introuvable

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
total_ca    = df['CA_Net'].sum()
top_product = df.iloc[0]['ID']

print("\n===== RÉSULTATS =====")
print(df.to_string(index=False))
print(f"\n💰 CA Total            : {total_ca:.2f} €")
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

plt.savefig('graphique.png', dpi=150)
print("📊 Graphique sauvegardé : graphique.png")
plt.close()