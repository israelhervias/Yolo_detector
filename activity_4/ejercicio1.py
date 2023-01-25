import cv2
import pandas as pd
import os
from typing import List


def read_txt_files(path: str) -> pd.DataFrame:
    """
    read_txt_files(path) - Reads all text files (.txt) within the specified
    path, adds a column called "label" with the name of the file (without the
    ".txt" extension), concatenates all the dataframes into one and resets the
    index. Finally, it removes the "index" column and returns the resulting
    dataframe.

    Parameters:
        path (str) - File path where the text files are located.
    Returns:
        result (pandas.Dataframe) - The concatenated dataframe containing all
        the information from the text files, with a label column indicating the
        name of the file.
    """
    dfs = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            df = pd.read_csv(os.path.join(path, file), delimiter=' ', header=None)
            df['label'] = file.split('.')[0]
            dfs.append(df)
    result = pd.concat(dfs).reset_index()
    result.drop('index', axis=1, inplace=True)
    return result


def read_image_folder(folder: str) -> pd.DataFrame:
    """
    read_image_folder(folder) - Reads all images with the .png extension within
    the specified folder, creates an empty dataframe with the columns 'image'
    and 'label', and add a row with the image and the label (name of the file
    without the ".png" extension) for each image file. Finally, it returns the
    dataframe with the images and labels.

    Parameters:
        folder (str) - File path where the image files are located.
    Returns:
        df (pandas.Dataframe) - The dataframe containing all the images and their
        corresponding labels.
    """
    df = pd.DataFrame(columns=['image', 'label'])
    for file in os.listdir(folder):
        if file.endswith('.png'):
            img = cv2.imread(os.path.join(folder, file))
            label = file.split('.')[0]
            df = df.append({'image': img, 'label': label}, ignore_index=True)
    return df


def merge(path: str, folder: str) -> pd.DataFrame:
    """
    The function "merge" explains that it takes two parameters, a file path
    and a folder. It uses the functions "read_txt_files" and
    "read_image_folder" to read the text files and images in the specified
    paths and save them in dataframes. Then, it uses the "pd.merge" function
    to join the dataframes based on the 'label' column using an "inner" join.
    Finally, it returns the resulting dataframe of the join of the two
    dataframes. The function requires two parameters, one for the path of the
    image files and one for the path of the text files, and returns a pandas
    Dataframe.

    Parameters:
        txt_path (str): File path where the text files are located.
        image_path (str): File path where the image files are located.
    Returns:
        pandas.Dataframe.
    """
    result = read_txt_files(path)
    df = read_image_folder(folder)
    results = pd.merge(result, df, on='label', how='inner')
    return results