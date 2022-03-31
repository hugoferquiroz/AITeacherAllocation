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

def carga_resultados_sira(filename):
    if filename.suffix == '.xlsx':
        siraweb = pd.read_excel(filename, sheet_name = 'Global', skiprows = 5)
    elif filename.suffix == '.dta':
        siraweb = pd.read_stata(filename)
    return siraweb

racio_2020 = pd.read_stata(work/r'Raw Data\Racio 2020.dta')
padron_gg1 = pd.read_stata(work/r'Raw Data\Padron GG1.dta')

# lista de las mastriculas
all_columns = padron_gg1.columns.values.tolist()

matricula = []
for x in all_columns:
    if x.startswith('cant'):
        matricula.append(x)

matricula_new = [ if x.startswith('cant_total_') matricula.remove(x) for x in matricula]


# labels_matricula = []
# for i in matricula:
#     my_string = 'Matricula'
#     for anio in [2015,2016,2017,2018,2019,2020,2021,2022]:
#         if i == 'cant_inclusivo_{anio}': 
#             my_string = my_string + ' inclusivo total' + f'-{anio}'
#             labels_matricula.append(my_string)
                
#         elif i == 'cant_total_{anio}': 
#             my_string = my_string + ' regular total' + f'-{anio}'
#             labels_matricula.append(my_string)

#         for grado in [0,1,2,3,4,5,6]:
            
#             if (f'cant{grado}' in i) and ('alum' in i) and i.endswith(f'{anio}'):
#                 my_string = my_string + ' regular' + f' {grado} grado/año' + f'-{anio}'
#                 labels_matricula.append(my_string)
                
#             elif (f'cant{grado}' in i) and ('inclusivo' in i) and i.endswith(f'{anio}'): 
#                 my_string = my_string + ' inclusivo' + f' {grado} grado' + f'-{anio}'
#                 labels_matricula.append(my_string)

'bolsa_s', 'bolsa_n', 'secciones_necesarias_2019'

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