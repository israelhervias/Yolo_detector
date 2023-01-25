# python3 -m unittest test_ejercicio1.py

import unittest
import pandas as pd
import os
import cv2
import ejercicio1

class TestEjercicio1(unittest.TestCase):
    def test_read_txt_files_returns_dataframe(self):
        path = 'dataset_cities/labels'
        result = ejercicio1.read_txt_files(path)
        self.assertIsInstance(result, pd.DataFrame)
        
    def test_read_image_folder_returns_dataframe(self):
        folder = 'dataset_cities/images'
        result = ejercicio1.read_image_folder(folder)
        self.assertIsInstance(result, pd.DataFrame)

    def test_merge_returns_dataframe(self):
        path = 'dataset_cities/labels'
        folder = 'dataset_cities/images'
        result = ejercicio1.merge(path,folder)
        self.assertIsInstance(result, pd.DataFrame)

    def test_read_txt_files_with_invalid_path(self):
        path = 'dataset/images'
        with self.assertRaises(FileNotFoundError):
            ejercicio1.read_txt_files(path)
            
    def test_read_image_folder_with_invalid_path(self):
        folder = 'dataset/labels'
        with self.assertRaises(FileNotFoundError):
            ejercicio1.read_image_folder(folder)
