import pandas as pd
import os


def check_yolo(file: str) -> bool:
    """
    The function "check_yolo" explains that it takes a file as a parameter and
    reads it as a CSV using the "pd.read_csv" function, creating a dataframe.
    It then checks if any of the values in the columns 'col2', 'col3', 'col4',
    'col5', and 'col6' are less than 0 or greater than 1. If any values are
    found to be out of this range, the function returns False. Additionally,
    the function checks if the data type of the 'col1' column is 'int64' . If
    this condition is not met, the function returns False. Then check if any of
    the values in the column 'col1' is less than 0 or greater than or equal to
    80. If any values are found to be out of this range, the function returns
    False. If the function completes all these checks successfully, it returns
    True. In case of any exception it returns False.
    """
    try:
        df = pd.read_csv(file, header=None, sep=" ", names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
        if (df[['col2', 'col3', 'col4', 'col5', 'col6']] < 0).any().any() or (df[['col2', 'col3', 'col4', 'col5', 'col6']] > 1).any().any():
            return False
        if (df['col1'].dtype != 'int64'):
            return False
        if (df[['col1']] < 0).any().any() or (df[['col1']] >= 80).any().any():
            return False
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Archivo no encontrado")