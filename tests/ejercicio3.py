import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_rectangles_from_txt(txt_path:str, image_path:str) -> None:
    """ 
    Draw rectangles on an image using coordinates from a text file that
    identifies objects in the image using YOLO.

    Parameters:
        txt_path (str): The path to the txt file containing the coordinates of 
        the rectangles.
        image_path (str): The path to the image on which the rectangles will be
        drawn.

    Returns:
        None
    """
    # Read the txt file and create a DataFrame
    df = pd.read_csv(txt_path, sep=' ', header=None, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
    
    # Add new columns
    W = 2048
    H = 1024
    df["x1"] = df["col2"] * W - df["col4"] * W / 2
    df["y1"] = df["col3"] * H - df["col5"] * H / 2
    df["x2"] = df["col2"] * W + df["col4"] * W / 2
    df["y2"] = df["col3"] * H + df["col5"] * H / 2

    # Read the image
    img = plt.imread(image_path)

    # Create a figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(img)

    # Iterate through the DataFrame and draw rectangles
    for i, row in df.iterrows():
        rect = Rectangle((row['x1'], row['y1']), row['x2']-row['x1'], row['y2']-row['y1'], linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

    # Show the plot
    plt.show()