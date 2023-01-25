import unittest
import pandas as pd
import os
import ejercicio2

class TestEjercicio2(unittest.TestCase):
    def test_check_yolo_returns_bool(self):
        file = 'dataset_cities/labels/berlin_000000_000019_leftImg8bit_20-10-2018.txt'
        result = ejercicio2.check_yolo(file)
        self.assertIsInstance(result, bool)

    def test_check_yolo_with_valid_file(self):
        file = 'dataset_cities/labels/zurich_000125_000019_leftImg8bit_15-01-2019.txt'
        result = ejercicio2.check_yolo(file)
        self.assertTrue(result)

    def test_check_yolo_with_invalid_file(self):
        file = 'dataset_cities/labels/zurich_000117_000019_leftImg8bit_09-01-2018.txt'
        result = ejercicio2.check_yolo(file)
        self.assertFalse(result)

    def test_check_yolo_with_invalid_path(self):
        file = 'path/to/invalid/file.csv'
        with self.assertRaises(FileNotFoundError):
            ejercicio2.check_yolo(file)
