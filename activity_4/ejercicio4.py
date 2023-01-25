import os
from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from itertools import islice


def process_files(directory: str, invalid_files: List[str]) -> List[str]:
    """
    Process files in a directory, ignoring specified invalid files and
    selecting values from valid files.

    Parameters:
        - directory (str): The directory containing the files to be processed.
        - invalid_files (List[str]): A list of file names to ignore.

    Returns:
        - List[str]: A list of selected values from the valid files.
    """
    # Get the absolute path of the directory
    abs_directory = os.path.abspath(directory)
    current_directory = os.getcwd()
    valid_files = [file for file in os.listdir(abs_directory) if file not in invalid_files]
    os.chdir(abs_directory)
    selected_values = []
    df_global = pd.DataFrame()
    for file in valid_files:
        df = pd.read_csv(file, sep=" ", header=None, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
        df = df[df['col6'] > 0.4]
        selected_values.extend(df["col1"])
    os.chdir(current_directory)
    return selected_values


def count_and_plot(selected_values: List[str]) -> pd.Series:
    """
    Count the frequency of each value in a list and plots the distribution.

    Parameters:
        selected_values (List[str]): A list of values to be counted and plotted.

    Returns:
        pd.Series: The top 5 most common values.
    """
    # Count the frequency of each value
    value_counts = pd.Series(selected_values).value_counts()

    # Plot the distribution of objects
    value_counts.plot(kind='bar')
    plt.show()
    # Get the top 5 most common objects
    top_5 = value_counts.nlargest(5)
    return top_5


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
        abs_file = os.path.abspath(os.path.join(directory,file))
        df = pd.read_csv(abs_file, sep=" ", header=None, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
        df = df[df['col6'] > 0.4]
        df['origin_file'] = file
        df_global = df_global.append(df)
    os.chdir(current_directory)
    return df_global


def create_histogram(df: pd.DataFrame) -> None:
    """
    The function create a normalized histogram of the top 5 categories from
    column 'col1' in the dataframe df and displays it.

    Parameters :
        df (pandas.core.frame.DataFrame)
    
    Returns:
        Display plot
    """
    categories_count = df["col1"].value_counts()
    top_categories = categories_count.sort_values(ascending=False).head(5)
    num_imagenes = df["origin_file"].nunique()
    data = []

    for i in range(5):
        unique = set(df[df["col1"] == top_categories.index[i]]["origin_file"].to_list())
        data.append(top_categories.index[i])
        for z in range(len(unique)-1):
            data.append(top_categories.index[i])

    categorias = [top_categories.index[i] for i in range(5)]
    datas = Counter(data)
    values = [datas[i] for i in categorias]

    # Configurar estilo de gráfico
    plt.style.use('ggplot')

    # Normalizar los valores
    values_norm =  [i/num_imagenes for i in values]

    # Crear histograma normalizado
    plt.bar(categorias, values_norm)

    # Agregar etiquetas al eje x e y y un título al gráfico
    plt.xlabel('Categorías')
    plt.ylabel('Valores normalizados')
    plt.title('Histograma normalizado')

    # Mostrar el gráfico
    plt.show()