    """_Automatiser l'extraction de meta données PubMed avec BioPython_
    @author : Abdelmajid EL HOU - Data analyst
    This tutorial is only for education purpose
    """

# import libraries
from Bio import Medline
import pandas as pd
from tqdm import tqdm

data = []

# read and parse file
with open('pubmed-machinelea-set.txt', encoding='utf-8') as file:
    pmids = Medline.parse(file)
    for pmid in pmids:
        try:
            pid = pmid['PMID']
        except:
            pid = ''
        try:
            title = pmid['TI']
        except:
            title=''
        try:
            abstract = pmid['AB']
        except:
            abstract = ''
        # save data to a dictionnary
        dict = {
            'PMID' : pid,
            'TI' : title,
            'AB' : abstract
        }
        data.append(dict)
# save data in a dataframe
df = pd.DataFrame(data)

# Export to excel file
df.to_excel(r'meta_data_pubmed.xlsx', index=False)
