# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:29:40 2022

@author: crami
"""

#Importar librerías necesarias
import pandas as pd
from pathlib import Path

pd.options.mode.chained_assignment = None
#Set de rutas
work =  Path(r'C:\Users\crami\OneDrive\Hugo - MINEDU\AI teacher allocation data')

def carga_resultados_sira(filename):
    siraweb = pd.read_excel(filename, sheet_name = 'Global', skiprows = 5)
    return siraweb

df_siraweb_2019 = carga_resultados_sira(work / r"Racio 2019.xlsx")

df_siraweb_2019 = df_siraweb_2019[['cod_mod', 'doc_e', 'doc_e_n', 'doc_e_c',
                                   'doc_req', 'bolsa_s', 'bolsa_n', 'nsecc_mod2']]
df_siraweb_2019.rename(columns={'nsecc_mod2':'secciones_necesarias_2019'},inplace=True)

print(df_siraweb_2019.columns.values.tolist())

df_siraweb_2019.to_csv(r'C:\Users\crami\OneDrive\Hugo - MINEDU\AI teacher allocation data\df_siraweb_2019.csv')