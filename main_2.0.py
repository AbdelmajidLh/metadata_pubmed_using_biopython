"""Automatiser l'extraction de méta-données PubMed avec BioPython
@author: Abdelmajid EL HOU - Data  SCientist/ingénieur
Ce tutoriel est uniquement à des fins éducatives
"""

# Import des bibliothèques
from Bio import Medline
import pandas as pd
from tqdm import tqdm

# Initialisation de la liste des données
data = []

# Lecture et analyse du fichier
with open('pubmed-machinelea-set.txt', encoding='utf-8') as file:
    # Utilisation de tqdm pour suivre la progression
    pmids = Medline.parse(file)
    for pmid in tqdm(pmids, desc="Processing PubMed entries"):
        try:
            pid = pmid['PMID']
        except KeyError:
            pid = ''
        try:
            title = pmid['TI']
        except KeyError:
            title = ''
        try:
            abstract = pmid['AB']
        except KeyError:
            abstract = ''
        # Sauvegarde des données dans un dictionnaire
        entry_dict = {
            'PMID': pid,
            'TI': title,
            'AB': abstract
        }
        data.append(entry_dict)

# Conversion des données en un DataFrame
df = pd.DataFrame(data)

# Exportation vers un fichier Excel
df.to_excel('meta_data_pubmed.xlsx', index=False)

print("Extraction des méta-données PubMed terminée et enregistrée dans 'meta_data_pubmed.xlsx'")
