    """_Automatiser l'extraction de meta données PubMed avec BioPython_
    @author : Abdelmajid EL HOU - Data analyst
    This tutorial is only for education purpose
    """

# import libraries
from Bio import Medline
import pandas as pd
from tqdm import tqdm

# read and parse file
with open('pubmed-machinelea-set.txt', encoding='utf-8') as file:
    pmids = Medline.parse(file)
    # use list comprehension to create list of dictionaries
    data = [{'PMID': pmid.get('PMID', ''), 'TI': pmid.get('TI', ''), 'AB': pmid.get('AB', '')} for pmid in tqdm(pmids)]
    
# save data in a dataframe
df = pd.DataFrame(data)

# Export to excel file
df.to_excel(r'meta_data_pubmed.xlsx', index=False)