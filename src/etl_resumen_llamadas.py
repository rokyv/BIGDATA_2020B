# Pseudo código
# Se deben crear 3 funciones: 
# 1. Leer archivo .csv
# 2. Extraer el resumen
# 3. Guardar el resumen en formato .csv

#from asyncore import dispatcher

#from fileinput import filename

import pandas as pd
import os
from pathlib import Path




def main():
    filename = "llamadas123_julio_2022.csv"

    # leer archivo
    data = get_data(filename= "llamadas123_julio_2022.csv")
    # extraer resumen
    df_resumen = get_summary(data)
    # guardar el resumen
    save_data(df_resumen,filename)

def save_data(df, filename):
    out_name = "resumen_" + filename
    root_dir = Path(".").resolve()
    out_path = os.path.join(root_dir, "data", "processed", out_name)
    
    # print (out_path)
    df.to_csv(out_path)

def get_summary(data):
    # Crear un diccionario vacio
    dict_resumen = dict()
    
    for col in data.columns:
        valores_unicos = data[col].unique()
        n_valores = len(valores_unicos)
        
        dict_resumen[col]= n_valores
    
    df_resumen = pd.DataFrame.from_dict(dict_resumen, orient="index")
    df_resumen.rename({0: "Count"}, axis=1, inplace=True)

    return df_resumen 

    
def get_data(filename):
    """Lee el archivo indicado, retorna un dataframe de pandas con los datos
    Args:
        file (str): nombre del archivo de entrada
        dir (str): nombre del directorio donde se encuentran los datos
    Returns:
        pandas.dataframe: dataframe con los datos
    """
    data_dir = "raw"
    root_dir = Path(".").resolve()
    file_path = os.path.join(root_dir,"data", data_dir, filename)
    
    data = pd.read_csv(file_path, encoding="latin-1",sep=";")
    return data
    
if __name__ == "__main__":
    main()