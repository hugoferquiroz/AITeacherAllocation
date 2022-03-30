# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:36:02 2022

@author: Hugoferq y CarlosRV0803
"""

#Importar librerías necesarias
import pandas as pd
from pathlib import Path
pd.options.mode.chained_assignment = None


#Set de rutas
work =  Path(r'D:\Trabajo\AITeacherAllocation')

# def carga_resultados_sira(filename):
#     siraweb = pd.read_excel(filename, sheet_name = 'Global', skiprows = 5)
#     return siraweb

# df_siraweb_2019 = carga_resultados_sira(work / r"Racio 2019.xlsx")

# df_siraweb_2019 = df_siraweb_2019[['cod_mod', 'doc_e', 'doc_e_n', 'doc_e_c',
#                                    'doc_req', 'bolsa_s', 'bolsa_n', 'nsecc_mod2']]
# df_siraweb_2019.rename(columns={'nsecc_mod2':'secciones_necesarias_2019'},inplace=True)

# print(df_siraweb_2019.columns.values.tolist())
# df_siraweb_2019.to_csv(r'C:\Users\crami\OneDrive\Hugo - MINEDU\AI teacher allocation data\df_siraweb_2019.csv')


racio_2020 = pd.read_stata(work/r'Raw Data\Racio 2020.dta')
# lista de las mastriculas
all_columns = racio_2020.columns.values.tolist()

matricula = []
for x in all_columns:
    if x.startswith('cant'):
        matricula.append(x)


'', 'bolsa_s', 'bolsa_n', 'secciones_necesarias_2019
cant0_alum_2015 
cant0_inclusivo_2015 

my_string = ''
if '0' in 'cant0_alum_2015':
    my_string = 'Inicial cuna'
elif 'alum' in 'cant0_alum_2015'



# Crear un diccionario de manera eficiente
    # Defino la lista de variables (divide y venceras)
        # 
        
        # Tokens para asignar label a las variables
        # 
    # La lista de etiquetas



# Diccionario
    #Resultados de la evaluacion
data_dictionary ={'doc_e':'Excedente - Numero de plazas de docente de aula',
                  'doc_e_n': 'Excedente - Numero de plazas de docente de aula nombrado',
                  'doc_e_c' : 'Excedente - Numero de plazas de docente de aula vacante o contratado',
                  'doc_req': 'Requerimiento - Numero de plazas de docente de aula',
                  'secciones_necesarias': 'Secciones necesarias',