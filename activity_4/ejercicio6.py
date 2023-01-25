import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from typing import Dict


def group_images_by_folder(folder_path: str, n_clusters: int) -> Dict:
    """
    Group images by folder and cluster them based on their file size
    Parameters:
        - folder_path (str): The path to the folder containing the images.
        - n_clusters (int): The number of clusters to use in the k-means
         algorithm.
    Returns:
        - Dict[int, List[str]]: A dictionary where the keys are integers
        representing the cluster label, and the values are lists of strings
        representing the file names of the images in each cluster.
    """
    # Crear un diccionario para almacenar los tamaños de las imágenes
    image_dict = {}
    
    # Recorrer todos los archivos en el directorio
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Comprobar si el archivo es una imagen y si su nombre comienza con
            # "zurich"
            if file.endswith(".png") and file.startswith("zurich"):
                file_path = os.path.join(root, file)
                # Obtener el tamaño del archivo en bytes
                file_size = os.path.getsize(file_path)
                # Agregar el nombre del archivo y el tamaño al diccionario
                image_dict[file] = file_size

    # Obtener solo los valores del diccionario
    values = list(image_dict.values())
    values = np.array(values)
    values = values.reshape(-1,1)

    # Entrenar el modelo k-means con 2 clusters
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(values)

    # Obtener las etiquetas de cada punto
    labels = kmeans.labels_

    # Agrupar las imágenes según su etiqueta
    groups = {}
    for i, label in enumerate(labels):
        if label not in groups:
            groups[label] = []
        groups[label].append(list(image_dict.keys())[i])

    return groups[1]