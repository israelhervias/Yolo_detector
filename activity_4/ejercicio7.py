import os
from typing import List
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def process_files2(directory: str, invalid_files: List[str]) -> pd.DataFrame:
    """
    Process files in a directory, ignoring specified invalid files and creating
    a DataFrame.
    This version of the function uses the absolute path of the directory and
    files, so it does not change the current working directory.

    Parameters:
        directory (str): The directory containing the files to be processed.
        invalid_files (List[str]): A list of file names to ignore.

    Returns:
        pd.DataFrame: A DataFrame containing values from the valid files.
    """
    abs_directory = os.path.abspath(directory)
    current_directory = os.getcwd()
    valid_files = [file for file in os.listdir(abs_directory) if file not in invalid_files]
    df_global = pd.DataFrame()
    for file in valid_files:
        abs_file = os.path.abspath(os.path.join(directory, file))
        df = pd.read_csv(abs_file, sep=" ", header=None, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
        df = df[df['col6'] > 0.4]
        df['origin_file'] = file
        df_global = df_global.append(df)
    os.chdir(current_directory)
    return df_global


def process(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Process the dataframe by grouping the values by column_name, counting the
    number of rows where col1 is 2, 0 or 9, renaming the columns, merging the
    resulting dataframes and adding the city and year columns to the final
    dataframe.
    
    Parameters:
        - df (pd.DataFrame): The dataframe to be processed.
        - column_name (str): The name of the column by which the dataframe will
        be grouped.
    
    Returns:
        - pd.DataFrame: The processed dataframe with columns "origin_file",
        "coches", "personas", "semáforos", "city" and "year".
    """
    final1 = df.groupby(column_name)["col1"].agg({lambda x: x[x==2].count()}).reset_index()
    final1 = final1.rename(columns={"<lambda>": "coches"})
    final2 = df.groupby(column_name)["col1"].agg({lambda x: x[x==0].count()}).reset_index()
    final2 = final2.rename(columns={"<lambda>": "personas"})
    final3 = df.groupby(column_name)["col1"].agg({lambda x: x[x==9].count()}).reset_index()
    final3 = final3.rename(columns={"<lambda>": "semáforos"})
    # Merge dataframe.
    final = pd.merge(final1, final2, on="origin_file")
    # Merge dataframe.
    total_final = pd.merge(final, final3, on="origin_file")
    # Añado ciudad y año al dataframe
    total_final["city"] = final['origin_file'].str.split('_').str.get(0)
    total_final["year"] = final['origin_file'].str.split('.').str.get(0).str.split('_').str.get(4).str.split('-').str.get(2)  
    total_final.loc[total_final['year'].isna(), 'year'] = '2015'
    return total_final


def classify_images(df: pd.DataFrame, folder_path: str, column_name: str, n_clusters: int) -> pd.DataFrame:
    """
    Classify images in a folder by size and add the labels as a new column in
    the dataframe.
    Parameters:
        - df (pd.DataFrame): The dataframe containing the image file names
        - folder_path (str): The path to the folder containing the images.
        - column_name (str): The name of the column in the dataframe containing
        the image file names.
        - n_clusters (int): The number of clusters to use in the k-means
        algorithm.
    Returns:
        - pd.DataFrame: The input dataframe with an additional column "label"
        indicating the cluster label of each image.
    """
    # Crear un diccionario para almacenar los tamaños de las imágenes
    image_dict = {}
    # Recorrer cada fila del dataframe
    for i, row in df.iterrows():
        # Obtener el nombre de la imagen de la columna especificada
        file_name = row[column_name]
        # Reemplazar la extensión del archivo de .txt a .png
        file_name = file_name.replace(".txt", ".png")
        # Unir el nombre del archivo con el path de la carpeta
        file_path = os.path.join(folder_path, file_name)
        # Comprobar si el archivo existe
        if os.path.exists(file_path):
            # Obtener el tamaño del archivo en bytes
            file_size = os.path.getsize(file_path)
            # Agregar el nombre del archivo y el tamaño al diccionario
            image_dict[file_name] = file_size
    # Obtener solo los valores del diccionario
    values = list(image_dict.values())
    values = np.array(values)
    values = values.reshape(-1, 1)
    # Entrenar el modelo k-means con 2 clusters
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(values)
    # Obtener las etiquetas de cada punto
    labels = kmeans.labels_
    # Añadir las etiquetas como una nueva columna en el dataframe
    df["label"] = labels
    return df