#----Librairies----
import pandas as pd
import plotly.express as px
import os
import yaml


#----Chemins des fichiers----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "data.xlsx")
CONFIG_PATH = os.path.join(BASE_DIR, "config", "hydraulic_params.yaml")

#----Fonctions----
def load_cleaned_data(filepath=PROCESSED_DATA_PATH):
    """
    Charge le fichier Excel nettoyé des données historiques.
    Args:
        filepath (str): Chemin du fichier Excel nettoyé.
    Returns:
        pd.DataFrame: Données nettoyées.
    """
    return pd.read_excel(filepath)

def visualize_distribution(df):
    """
    Affiche l'histogramme interactif des hauteurs de crues.
    Args:
        df (pd.DataFrame): Données nettoyées.
    """
    fig = px.histogram(df, x="Hauteur", nbins=20, title="Distribution des hauteurs de crue", 
                       labels={"Hauteur": "Hauteur de crue (m)"}, opacity=0.7)
    fig.update_layout(bargap=0.1)
    fig.show()

def get_optimal_digue_height(df, percentile=0.95):
    """
    Calcule la hauteur de digue protégeant contre un pourcentage donné des crues.
    Args:
        df (pd.DataFrame): Données nettoyées.
        percentile (float): Seuil de protection (ex: 0.95 pour 95%).
    Returns:
        float: Hauteur optimale de la digue.
    """
    return df["Hauteur"].quantile(percentile)

def visualize_distribution_with_threshold(df, hauteur_opt):
    """
    Affiche l'histogramme des hauteurs de crues et indique la hauteur optimale de la digue.
    Args:
        df (pd.DataFrame): Données nettoyées.
        hauteur_opt (float): Hauteur optimale de la digue.
    """
    fig = px.histogram(df, x="Hauteur", nbins=20, title="Distribution des hauteurs de crue avec seuil optimal",
                       labels={"Hauteur": "Hauteur de crue (m)"}, opacity=0.7)
    
    # Ajouter la ligne verticale pour la hauteur optimale
    fig.add_vline(x=hauteur_opt, line_dash="dash", line_color="red",
                  annotation_text=f"Hauteur optimale: {hauteur_opt:.2f} m", annotation_position="top right")

    fig.update_layout(bargap=0.1)
    fig.show()

def visualize_boxplot(df):
    """
    Affiche un boxplot des hauteurs de crue pour détecter les valeurs extrêmes.
    Args:
        df (pd.DataFrame): Données nettoyées.
    """
    fig = px.box(df, y="Hauteur", title="Boxplot des hauteurs de crue",
                 labels={"Hauteur": "Hauteur de crue (m)"})
    fig.show()

def visualize_time_series(df):
    """
    Affiche l'évolution des hauteurs de crues dans le temps.
    Args:
        df (pd.DataFrame): Données nettoyées.
    """
    fig = px.line(df, x="Annee", y="Hauteur", title="Évolution des hauteurs de crue au fil du temps",
                  labels={"Annee": "Année", "Hauteur": "Hauteur de crue (m)"})
    fig.show()


def load_hydraulic_params():
    """
    Charge les paramètres hydrauliques depuis le fichier YAML.
    Returns:
        dict: Paramètres du modèle hydraulique.
    """
    with open(CONFIG_PATH, "r") as file:
        params = yaml.safe_load(file)
    return params["hydraulic_model"]