#-----importation des librairies-----

import pandas as pd
import os
#-----définition des chemins des fichiers-----

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Remonte d'un niveau
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "Données-Projet-Pratique-Fiabilité-ISUP-DS_E-Remy_2024-2025.xlsx")  
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "data.xlsx") 

#-----fonction de chargement des données-----
def load_data(filepath=RAW_DATA_PATH):
    """
    Charge le fichier Excel des données historiques.
    Args:
        filepath (str): Chemin du fichier Excel.
    Returns:
        pd.DataFrame: Données nettoyées.
    """
    df = pd.read_excel(filepath) 
    df.columns = ["Annee", "Debit", "Hauteur"]  
    df = df.dropna()  
    df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce")
    df["Hauteur"] = pd.to_numeric(df["Hauteur"], errors="coerce")
    
    return df

def save_cleaned_data(df, output_path=PROCESSED_DATA_PATH):
    """
    Sauvegarde les données nettoyées dans le dossier processed.
    Args:
        df (pd.DataFrame): Données nettoyées.
        output_path (str): Chemin de sauvegarde.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  
    df.to_excel(output_path, index=False)
    print(f"Données nettoyées enregistrées : {output_path}")

#-----processing des données-----

df = load_data()
save_cleaned_data(df)