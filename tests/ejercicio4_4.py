import pandas as pd
from collections import Counter
import pandas


def get_popular_values(df: pandas.DataFrame) -> Counter:
    """
    This function takes a pandas DataFrame as an input and returns a Counter
    object containing the popular values of the "col1" column in the files
    with "col6" value greater than 0.4.
    """
    # We create a list to store the objects of the txt.
    lista_populares = []

    # We filter de dataframe by column6.
    df = df[df["col6"] > 0.4]

    valid_files = [i for i in df.origin_file.unique()]

    # We iterate throgh echa of the txt files.
    for i in valid_files:

        df_unique = df[df["origin_file"] == i]
        valores = df_unique.col1.value_counts()

        if len(valores) < 4:
            for i in range(len(valores)):
                lista_populares.append(valores.index[i])
        else:
            conteo = 0
            most_frequent = valores.values[0]

            for j in range(len(valores)):
                if valores.values[j] != most_frequent:
                    break
                conteo += 1
                lista_populares.append(valores.index[j])

            if conteo == 1:
                if (valores.values[1] == valores.values[2]):

                    if (valores.values[2] != valores.values[3]):
                        for z in [1,2]:
                            lista_populares.append(valores.index[z])

                elif (valores.values[1] != valores.values[2]):
                    if (valores.values[2] == valores.values[3]):
                        lista_populares.append(valores.index[1])

                    elif (valores.values[2] != valores.values[3]):
                        for x in [1,2]:
                            lista_populares.append(valores.index[x])

            elif conteo == 2:
                if (valores.values[2] != valores.values[3]):
                    lista_populares.append(valores.index[2])

    frequencies = Counter(lista_populares)
    frequencies_dict = dict(frequencies)
    return frequencies_dict