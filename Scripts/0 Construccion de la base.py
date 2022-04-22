# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:36:02 2022

@author: Hugoferq y CarlosRV0803
"""

#Import libraries
import pandas as pd
from pathlib import Path
pd.options.mode.chained_assignment = None

#Set files path
work =  Path(r'D:\Trabajo\AITeacherAllocation')

# Import data
# def carga_resultados_sira(filename):
#     if filename.suffix == '.xlsx':
#         siraweb = pd.read_excel(filename, sheet_name = 'Global', skiprows = 5)
#     elif filename.suffix == '.dta':
#         siraweb = pd.read_stata(filename)
#     return siraweb

racio_2019 = pd.read_stata(work/r'Raw Data\Racio 2019.dta')
racio_2020 = pd.read_stata(work/r'Raw Data\Racio 2020.dta')
racio_2021 = pd.read_stata(work/r'Raw Data\Racio 2021.dta')

#Variables a usar
all_columns = racio_2020.columns.values.tolist()
    #Datos de identificacion (salen del padron gg1)
identificacion = ['cod_mod'] 

    #PEA evaluada
for cargo in ['dir','sub_dir']:
    racio_2020[f'{cargo}_nom'] = racio_2020[f'{cargo}_des_org']+racio_2020[f'{cargo}_des_ev']
    racio_2020[f'{cargo}_vac'] = racio_2020[f'{cargo}_des_ev']+racio_2020[f'{cargo}_enc_ev']+racio_2020[f'{cargo}_vac_ev']
	
for cargo in ['jer','doc','otro_doc','aux']:
    racio_2020[f'{cargo}_nom']=racio_2020[f'{cargo}_nom_org']+racio_2020[f'{cargo}_nom_ev']
    racio_2020[f'{cargo}_vac']=racio_2020[f'{cargo}_con_org']+racio_2020[f'{cargo}_con_ev']+racio_2020[f'{cargo}_vac_org']+racio_2020[f'{cargo}_vac_ev']

pea_evaluada = []
for cargo in ['dir','sub_dir','jer','doc','otro_doc','aux']:
    for sit in ['nom','vac']:
        pea_evaluada.append(f'{cargo}_{sit}')

    #Matricula 
matricula_evaluacion = [ x for x in all_columns if x.startswith('cant') and not x.startswith('cant_total_') and not 
                 x.startswith('cant_inclusivo') and not x.find('cant_alum_')!=-1 and not
                 x.find('bolsa_horas')!=-1 ]
    
        # Cambiando el nombre de la matricula para que todas los anios tengan la misma extension
racio_2020 = racio_2020.rename(columns={'cant1_alum': 'cant1 (t)', 
                                        'cant2_alum': 'cant2 (t)', 
                                        'cant3_alum': 'cant3 (t)', 
                                        'cant4_alum': 'cant4 (t)', 
                                        'cant5_alum': 'cant5 (t)',
                                        'cant6_alum': 'cant6 (t)'})

racio_2020 = racio_2020.rename(columns={'cant1_inclusivo_2020': 'cant1 (t)', 
                                        'cant2_inclusivo_2020': 'cant2 (t)', 
                                        'cant3_inclusivo_2020': 'cant3 (t)', 
                                        'cant4_inclusivo_2020': 'cant4 (t)', 
                                        'cant5_inclusivo_2020': 'cant5 (t)',
                                        'cant6_inclusivo_2020': 'cant6 (t)'})

racio_2020[matricula_evaluacion]
racio_2020['cant0_inclusivo_2020']
racio_2020['cant1_alum']
# cant1_inclusivo_2020


lag = 0
for anio in ['2019','2018','2017','2016']:
  lag = lag + 1
  racio_2020 = racio_2020.rename(columns={f'cant0_alum_{anio}': f'cant0 (t-{lag})', 
                                          f'cant1_alum_{anio}': f'cant1 (t-{lag})',
                                          f'cant2_alum_{anio}': f'cant2 (t-{lag})', 
                                          f'cant3_alum_{anio}': f'cant3 (t-{lag})',
                                          f'cant4_alum_{anio}': f'cant4 (t-{lag})', 
                                          f'cant5_alum_{anio}': f'cant5 (t-{lag})', 
                                          f'cant6_alum_{anio}': f'cant6 (t-{lag})'})



    
    #Datos de la evaluacion
datos_evaluacion = ['usuario_minedu','bolsa_nexus','bolsa_sira']
    #Resultados
requerimientos = [x for x in all_columns if x.startswith('req') and not x.find('req_exd')!=-1]
excedentes = [x for x in all_columns if x.find('exd')!=-1 and x.endswith('2020') and not x.find('tot_')!=-1 ]
           

 


for i in [racio_2019,racio_2020,racio_2021]:
    print('jec_2019' in i)

# Base consolidada   
muermo = racio_2020[identificacion+pea_evaluada+matricula_evaluacion+
                    datos_evaluacion+requerimientos+excedentes]
    
muermo.describe 
 
for i in matricula_evaluacion:
    print(i in racio_2020)
    
    
for x in all_columns:
    if x.find('usuario')!=-1:
        print(f'{x}')


'usuario_minedu' in all_columns
racio_2021['nivel'].value_counts()

racio_2021['niv_mod'].value_counts()
racio_2021[racio_2021['niv_mod']!='A2']







# Build a data dictionary
padron_gg1 = pd.read_stata(work/r'Raw Data\Padron GG1.dta')
all_columns = padron_gg1.columns.values.tolist()
matricula = []
for x in all_columns:
    if x.startswith('cant'):
        matricula.append(x)
        
matricula_short = [ x for x in matricula if not x.startswith('cant_total_') and not x.startswith('cant_inclusivo')]
labels_matricula = []
for i in matricula_short :
    my_string = 'Matricula'
    for anio in [2015,2016,2017,2018,2019,2020,2021,2022]:
        if i == 'cant_inclusivo_{anio}': 
            my_string = my_string + ' inclusivo total' + f'-{anio}'
            labels_matricula.append(my_string)
                
        elif i == 'cant_total_{anio}': 
            my_string = my_string + ' regular total' + f'-{anio}'
            labels_matricula.append(my_string)

        for grado in [0,1,2,3,4,5,6]:
            
            if (f'cant{grado}' in i) and ('alum' in i) and i.endswith(f'{anio}'):
                my_string = my_string + ' regular' + f' {grado} grado/año' + f'-{anio}'
                labels_matricula.append(my_string)
                
            elif (f'cant{grado}' in i) and ('inclusivo' in i) and i.endswith(f'{anio}'): 
                my_string = my_string + ' inclusivo' + f' {grado} grado/año' + f'-{anio}'
                labels_matricula.append(my_string)

dict_matricula = dict(zip(matricula_short , labels_matricula))
matricula_dd = pd.DataFrame(dict_matricula.items(), columns=['Variable', 'Etiqueta'] )


# 'bolsa_s', 'bolsa_n', 'secciones_necesarias_2019'




# Crear un diccionario de manera eficiente
    # Defino la lista de variables (divide y venceras)
        # Matricula (x)
        # Docentes ()
        # Identificacion ()
        
    
# Diccionario
    #Resultados de la evaluacion
# data_dictionary ={'doc_e':'Excedente - Numero de plazas de docente de aula',
#                   'doc_e_n': 'Excedente - Numero de plazas de docente de aula nombrado',
#                   'doc_e_c' : 'Excedente - Numero de plazas de docente de aula vacante o contratado',
#                   'doc_req': 'Requerimiento - Numero de plazas de docente de aula',
#                   'secciones_necesarias': 'Secciones necesarias',