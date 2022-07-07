# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:36:02 2022

@author: hugoferq y carlosRV0803
"""

#Importar las librerias
import pandas as pd
from pathlib import Path
pd.options.mode.chained_assignment = None

#Configuro la direccion de trabajo
work =  Path(r'D:\Trabajo\AITeacherAllocation')

#Cargo las bases de insumos
racio_2019 = pd.read_csv(work/r'Raw Data\Base 2019.csv')
racio_2020 = pd.read_stata(work/r'Raw Data\\Racio 2020.dta')
racio_2021 = pd.read_stata(work/r'Raw Data\\Racio 2021.dta')
padron_gg1 = pd.read_stata(work/r'Raw Data\\Padron GG1.dta')
#Renombro alguans variables
racio_2021.rename(columns={'numeroseccion':'secciones_necesarias'}, inplace=True)


#Funcion para limpiar y homogenizar las bases de datos
def cargar_base(df,anio):
    """
    Esta funcion limpia y homogeniza los resultados de racionalizacion

    Parameters
    ----------
    df :   TYPE: DataFrame para limpiar y homogenizar
           DataFrame para limpiar y homogenizar.
    anio : TYPE. Int
           Año de la base de datos

    Returns
    -------
    df_ok : TYPE. DataFrame
            DataFrame limpio y homogenizada

    """
    #Variables a usar
    all_columns = df.columns.tolist()
    
    #Datos de identificacion (salen del padron gg1)
    identificacion_padron = ['cod_mod','niv_mod', 'd_niv_mod','gestion','d_gestion','ges_dep','d_ges_dep','ubigeo',
                         'd_dpto','d_prov','d_dist','d_region','codooii','d_dreugel','nlat_ie','nlong_ie',
                         'estado','d_estado','region','tipo_entidad',f'jec_{anio}'] 
    asignaciones_temporales=[f'rural_upp_{anio}',f'vraem_upp_{anio}',f'fron_upp_{anio}',f'bilin_upp_{anio}',f'tipie_upp_{anio}']
    identificacion = ['cod_mod','codlocal']
    padron_gg1_short = padron_gg1.loc[padron_gg1['anexo']=='0' ,identificacion_padron+asignaciones_temporales]
    padron_gg1_short.rename(columns={f'rural_upp_{anio}':'ruralidad',
                                     f'vraem_upp_{anio}':'vraem',
                                     f'fron_upp_{anio}':'frontera',
                                     f'bilin_upp_{anio}':'bilingue',
                                     f'tipie_upp_{anio}':'caracteristica',
                                     f'jec_{anio}':'jec'},inplace=True)
    
    #PEA evaluada
    for cargo in ['dir','sub_dir']:
        df[f'{cargo}_nom'] = df[f'{cargo}_des_org']+df[f'{cargo}_des_ev']
        df[f'{cargo}_vac'] = df[f'{cargo}_des_ev']+df[f'{cargo}_enc_ev']+df[f'{cargo}_vac_ev']
	
    for cargo in ['jer','doc','otro_doc','aux']:
        df[f'{cargo}_n']=df[f'{cargo}_nom_org']+df[f'{cargo}_nom_ev']
        df[f'{cargo}_c']=df[f'{cargo}_con_org']+df[f'{cargo}_con_ev']+df[f'{cargo}_vac_org']+df[f'{cargo}_vac_ev']

    pea_evaluada = []
    for cargo in ['dir','sub_dir','jer','doc','otro_doc','aux']:
        for sit in ['nom','vac']:
            pea_evaluada.append(f'{cargo}_{sit}')    
    
    #Matricula     
        # Cambiando el nombre de la matricula para que todas los anios tengan la misma extension
    df = df.rename(columns={f'cant0_alum_{anio}':'cant0 (t)',
                            f'cant1_alum_{anio}': 'cant1 (t)', 
                            f'cant2_alum_{anio}': 'cant2 (t)', 
                            f'cant3_alum_{anio}': 'cant3 (t)', 
                            f'cant4_alum_{anio}': 'cant4 (t)', 
                            f'cant5_alum_{anio}': 'cant5 (t)',
                            f'cant6_alum_{anio}': 'cant6 (t)'})

    df = df.rename(columns={f'cant0_inclusivo_{anio}': 'inclu0 (t)',
                            f'cant1_inclusivo_{anio}': 'inclu1 (t)', 
                            f'cant2_inclusivo_{anio}': 'inclu2 (t)', 
                            f'cant3_inclusivo_{anio}': 'inclu3 (t)', 
                            f'cant4_inclusivo_{anio}': 'inclu4 (t)', 
                            f'cant5_inclusivo_{anio}': 'inclu5 (t)',
                            f'cant6_inclusivo_{anio}': 'inclu6 (t)'})

    lag = 0
    anios = [anio - i for i in [1,2,3,4]]
    for lapso in anios:
      lag = lag + 1
      df = df.rename(columns={f'cant0_alum_{lapso}': f'cant0 (t-{lag})', 
                              f'cant1_alum_{lapso}': f'cant1 (t-{lag})',
                              f'cant2_alum_{lapso}': f'cant2 (t-{lag})', 
                              f'cant3_alum_{lapso}': f'cant3 (t-{lag})',
                              f'cant4_alum_{lapso}': f'cant4 (t-{lag})', 
                              f'cant5_alum_{lapso}': f'cant5 (t-{lag})', 
                              f'cant6_alum_{lapso}': f'cant6 (t-{lag})'})
      
      df = df.rename(columns={f'cant0_inclusivo_{lapso}': f'inclu0 (t-{lag})', 
                              f'cant1_inclusivo_{lapso}': f'inclu1 (t-{lag})',
                              f'cant2_inclusivo_{lapso}': f'inclu2 (t-{lag})', 
                              f'cant3_inclusivo_{lapso}': f'inclu3 (t-{lag})',
                              f'cant4_inclusivo_{lapso}': f'inclu4 (t-{lag})', 
                              f'cant5_inclusivo_{lapso}': f'inclu5 (t-{lag})', 
                              f'cant6_inclusivo_{lapso}': f'inclu6 (t-{lag})'})
    
    matricula_rename = [x for x in df.columns.to_list() if x.find(' (t')!=-1]
    
    #Datos de la evaluacion
    datos_evaluacion = ['usuario_minedu','bolsa_nexus','bolsa_sira','secciones_necesarias']
    #Resultados
    requerimientos = [x for x in all_columns if x.startswith('req') and not x.find('req_exd')!=-1]
    excedentes = [x for x in all_columns if x.find('exd')!=-1 and x.endswith(f'{anio}') and not x.find('tot_')!=-1 ]
    #Agrego datos del padron
    racio_short = df[identificacion+pea_evaluada+matricula_rename+datos_evaluacion+requerimientos+excedentes] 
    #Base consolidada   
    df_ok = pd.merge(racio_short,padron_gg1_short,on=['cod_mod'],how='left',validate='1:1')
    #Homogenizo las variables
    for col in df_ok.columns:
        df_ok.rename(columns={col:col.replace(f'_{anio}','')},inplace=True)
    df_ok['year'] = anio
    return df_ok


#Consolido la base
racio_2020_ok = cargar_base(racio_2020,2020)
racio_2021_ok = cargar_base(racio_2021,2021)
df = racio_2020_ok.append(racio_2021_ok)
df = df.append(racio_2019)
#Exporto la base
df.to_csv(work/r'Results\Base consolidada.csv')
df.to_csv('D:\OneDrive\Trabajo\Minedu\AI teacher allocation data\Results\Base consolidada.csv')




# Build a data dictionary
all_columns = df.columns.to_list()
    # Excedentes
excedentes = [x for x in df.columns.to_list() if x.find('exd')!=-1 and not x.find('tot_')!=-1]
exd = ['']*len(excedentes)
df_dd_exd = pd.DataFrame(list(zip(excedentes, exd)),columns =['Variable', 'Descripcion'])



df_dd_exd['cargo']='docente de aula' if df_dd_exd['variable'].str.find('doc_aula')

data_dictionary ={'doc_e_n': 'Numero de plazas de docente de aula excedentes nombrado',
                  'doc_e_c' : 'Numero de plazas de docente de aula excedentes vacante o contratado',
                  }


df_dd_exd.loc[df_dd_exd['Variable'].str.find('doc_aula')!=-1,'Descripcion']='docente de aula'
df_dd_exd.loc[df_dd_exd['Variable'].str.find('dir')!=-1,'Descripcion']='director'
df_dd_exd.loc[df_dd_exd['Variable'].str.find('sub_dir')!=-1,'Descripcion']='subdirector'
    
dict_cargos={'director':'director', 'doc_aula':'docente de aula'}
dict_sit_lab={'_n':'nombrado', '_c':'contratado'}

for k,v in dict_cargos.items():
    print(k,'->',v)
    df_dd_exd.loc[df_dd_exd['Variable'].str.find(f'{k}')!=-1,'Descripcion']=f'{v}'

df_dd_exd

'auxiliar':'auxiliar'
'jerarquico':'jerarquico'
'subdirector':'subdirector'
'director':'director'
'doc_aula':'docente de aula'

'exd':'excedente'
'_c':'contratado'
'_n':'nombrado'}
    
# orden de llenado: cargo, excedente, contratado/nombrado

exd_dic
len(all_columns)


# for x in ['dir','sub_dir','jer','doc','otro_doc','aux']:
#     for y in ['2020','2021']:
#         if x.starswith(f'{x}') and x.endswith(f'y'):
#             print('docente de aula')




def lista_exd(df, anio):
    exd = [x for x in df.columns.to_list() if x.find('exd')!=-1 and x.endswith(f'{anio}') and not x.find('tot_')!=-1]
    x = anio
    return exd, x

exd_2020, muermo = lista_exd(racio_2020,2020)
exd_2020
muermo

    # Matricula
    
matricula = [x for x in columnas_dict if x.startswith('cant') | x.startswith('inclu')]
labels_matricula = []
for mat in matricula:
    if (mat.find(f't{0}')!=-1) & (mat.find('cant')!=-1):
        my_string = 'Alumno regulares - cuna menor a 12 meses'
        labels_matricula.append(my_string)
        
cant6 (t)
inclu0 (t)
# Inicial
    # 0-> <1 anio
    # 1-> <2 anio
    # 2-> <3 anio
    # 3-> 3 anios inicial
    # 4-> 4 anios inicial
    # 5-> 5 anios inicial

# Primaria
    # 1 -> Primero de primaria
    # 2 -> Segundo de primaria   
    # 3 -> Tercero de primaria   
    # 4 -> Cuarto de primaria   
    # 5 -> Quinto de primaria   
    # 6 -> Sexto de primaria   

# Secundaria
    # 1 -> Primero de secundaria
    # 2 -> Segundo de secundaria
    # 3 -> Tercero de secundaria
    # 4 -> Cuarto de secundaria
    # 5 -> Quinto de secundaria

    # Resultados del proceso de racionalizacion


    
# Diccionario
    #Resultados de la evaluacion
# data_dictionary ={'doc_e':'Excedente - Numero de plazas de docente de aula',
#                   'doc_e_n': 'Excedente - Numero de plazas de docente de aula nombrado',
#                   'doc_e_c' : 'Excedente - Numero de plazas de docente de aula vacante o contratado',
#                   'doc_req': 'Requerimiento - Numero de plazas de docente de aula',
#                   'secciones_necesarias': 'Secciones necesarias',