import os
from typing import List
import pandas as pd
import matplotlib.pyplot as plt


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


def plot_cars_by_year_and_city(df:pd.DataFrame) -> None:
    """
    The function "plot_cars_by_year_and_city" takes in a pandas DataFrame as a
    parameter and plots a stacked bar chart of cars by year and city. It first
    filters the DataFrame by the value in the 'col1' column, then creates new
    columns 'city' and 'year' by splitting the 'origin_file' column. It then
    fills any missing values in the 'year' column with the value '2015'. Next,
    it groups the DataFrame by the 'city' and 'year' columns and plots the
    resulting DataFrame using the 'bar' kind and stacked=True. The function
    requires one parameter, a pandas Dataframe and it returns None
    
    Parameters :
        df (pandas.core.frame.DataFrame)
    
    Returns:
        Display plot
    """
    df_car = df[df["col1"] == 2]
    df_car['city'] = df_car['origin_file'].str.split('_').str.get(0)
    df_car['year'] = df_car['origin_file'].str.split('.').str.get(0).str.split('_').str.get(4).str.split('-').str.get(2)
    df_car.loc[df_car['year'].isna(), 'year'] = '2015'
    df_grouped = df_car.groupby(['city', 'year']).size().unstack()
    df_grouped.plot(kind='bar', stacked=True)
    plt.show()