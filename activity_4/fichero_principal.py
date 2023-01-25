# python3 fichero_principal.py
import warnings
import os
import pandas as pd
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio4_4
import ejercicio5
import ejercicio6
import ejercicio7
import matplotlib.pyplot as plt
from itertools import islice

warnings.filterwarnings("ignore")
# Ejercicio 1
print("Ejercicio 1")
path = "dataset_cities/labels"
folder = "dataset_cities/images"
print(ejercicio1.merge(path, folder).head())
print(" ")
print(""" 
En caso de tener millones de archivos o archivos muy pesados tenemos diferentes
alternativas para llevar a cabo el proceso. Pero siempre la elección dependerá
de los recursos disponibles y de las necesidades específicas del proyecto. 

Podríamos utilizar técnicas de procesamiento distribuido para analizar los
datos. Esto podría incluir la distribución de la carga de procesamiento entre
varios servidores.

Utilización de sistemas de almacenamiento en la nube como por ejemplo Google
Cloud o Azure entre otros sistemas que  permiten un escalado fácil y una mayor
flexibilidad en cuanto a los recursos necesarios para llevar a cabo el
proyecto. 

También podríamos utilizar algoritmos de aprendizaje automático escalables para
analizar los datos. Esto podría permitir un procesamiento automatizado y
escalable.

Podríamos también utilizar técnicas de muestreo para seleccionar un subconjunto
representativo (muestra) de los datos para analizar, en lugar de procesar todos
los datos. 

Al final dependerá en gran medida del origen de los datos, los recursos con los
que contamos y la finalidad que tengamos en el proyecto.
""")
print(" ")

# Ejercicio 2
print("Ejercicio 2")
# Código principal
path = 'dataset_cities/labels'
invalid_files = []
valid_files = []
for file in os.listdir(path):
    if not ejercicio2.check_yolo(os.path.join(path, file)):
        invalid_files.append(file)
    else:
        valid_files.append(file)

if invalid_files:
    print("Los siguientes archivos no tienen el formato YOLO:")
    for file in invalid_files:
        print(file)
else:
    print("No se ha encontrado ningún archivo incompatible.")
print(" ")

# Ejercicio 3
print("Ejercicio 3")
# Imagen Berlin
ruta_txt = "dataset_cities/labels/berlin_000000_000019_leftImg8bit_20-10-2018.txt"
ruta_imagen = "dataset_cities/images/berlin_000000_000019_leftImg8bit_20-10-2018.png"
ejercicio3.draw_rectangles_from_txt(ruta_txt, ruta_imagen)
# Imagen Bonn
ruta_txt2 = "dataset_cities/labels/bonn_000000_000019_leftImg8bit_18-07-2017.txt"
ruta_imagen2 = "dataset_cities/images/bonn_000000_000019_leftImg8bit_18-07-2017.png"
ejercicio3.draw_rectangles_from_txt(ruta_txt2, ruta_imagen2)
# Imagen Zurich
ruta_txt3 = "dataset_cities/labels/zurich_000000_000019_leftImg8bit_20-08-2015.txt"
ruta_imagen3 = "dataset_cities/images/zurich_000000_000019_leftImg8bit_20-08-2015.png"
ejercicio3.draw_rectangles_from_txt(ruta_txt3, ruta_imagen3)
print(" ")

# Ejercicio 4
# Ejercicio 4.1
print("Ejercicio 4.1")
path_labels = "dataset_cities/labels"
selected_values = ejercicio4.process_files(path_labels, invalid_files)
print(ejercicio4.count_and_plot(selected_values))
print(" ")

# Ejercicio 4.2
print("Ejercicio 4.2")
path_labels = "dataset_cities/labels"
df_global = ejercicio4.process_files2(path_labels, invalid_files)
print(ejercicio4.create_histogram(df_global))
print(" ")

# Ejercicio 4.3
print("Ejercicio 4.3")
# Solo tomamos como referencias los documentos con objetos > 0.4.
total_imagenes = set(df_global["origin_file"].to_list())
mean_objects = df_global.shape[0] / len(total_imagenes)
print("La media de objetos sería: ",round(mean_objects,2))
print("""Para su cálculo hemos tomado en cuanta el número total de
registros dividiendolo por el número total de imagenes que forman
el conjunto.""")
print(" ")

# Ejercicio 4.4
print("Ejercicio 4.4")
d = ejercicio4_4.get_popular_values(df_global)
first_3 = dict(islice(sorted(d.items(), key=lambda x: x[1], reverse=True), 3))
print(first_3) 
print("""No coinciden lo valores. En el apartado 1 agrupamos
todos los valores sin tener en cuenta ningún criterio en cambio esta vez
hemos seguido las instrucciones del apartado 4.4 por lo cual conlleva la no
coincidencia de resultados.""")
print(" ")

# Ejercicio 5
print("Ejercicio 5")
path_labels = "dataset_cities/labels"
df_global = ejercicio5.process_files2(path_labels, invalid_files)
df_car = ejercicio5.plot_cars_by_year_and_city(df_global)
print(df_car)
print(" ")

# Ejercicio 6
print("Ejercicio 6")
path = "dataset_cities/images"
print(ejercicio6.group_images_by_folder(path, 2))
print(" ")

# Ejercicio 7
print("Ejercicio 7")
path_labels = "dataset_cities/labels"
df_global = ejercicio7.process_files2(path_labels, invalid_files)
final = ejercicio7.process(df_global, "origin_file")
path = "dataset_cities/images"
df = ejercicio7.classify_images(final, path, "origin_file", 2)
df.to_csv('new_data.csv')
print(df.head())
print(" ")
print(os.getcwd(), "Indica donde se encuentra el CSV guardado.")
print(" ")