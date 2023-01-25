import unittest
import ejercicio3
import pandas as pd

class TestDrawRectanglesFromTxt(unittest.TestCase):
    def test_draw_rectangles_from_txt_valid_paths(self):
        txt_path = 'dataset_cities/labels/berlin_000000_000019_leftImg8bit_20-10-2018.txt'
        image_path = 'dataset_cities/images/berlin_000000_000019_leftImg8bit_20-10-2018.png'
        ejercicio3.draw_rectangles_from_txt(txt_path, image_path)
        
# se puede asumir que si no genera un error al ejecutarse, 
# entonces se esta comportando de forma correcta.
        
    def test_draw_rectangles_from_txt_with_invalid_txt_path(self):
        txt_path = 'invalid/file.txt'
        image_path = 'dataset_cities/images/berlin_000000_000019_leftImg8bit_20-10-2018.png'
        with self.assertRaises(FileNotFoundError):
            ejercicio3.draw_rectangles_from_txt(txt_path, image_path)
            
    def test_draw_rectangles_from_txt_with_invalid_image_path(self):
        txt_path = 'dataset_cities/labels/berlin_000000_000019_leftImg8bit_20-10-2018.txt'
        image_path = 'invalid/image.png'
        with self.assertRaises(FileNotFoundError):
            ejercicio3.draw_rectangles_from_txt(txt_path, image_path)
