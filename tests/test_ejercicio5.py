import unittest
import os
import pandas as pd
import ejercicio5

class TestEjercicio5(unittest.TestCase):
    def setUp(self):
        self.test_directory = os.path.join(os.path.dirname(__file__), 'dataset_cities/labels/')
        self.valid_files = ['berlin_000000_000019_leftImg8bit_20-10-2018.txt', 'berlin_000005_000019_leftImg8bit_14-02-2017.txt']
        self.invalid_files = ['invalid_file1.csv', 'invalid_file2.csv']

    def test_process_files2(self):
        df = ejercicio5.process_files2(self.test_directory, self.invalid_files)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 7510)

    def test_plot_cars_by_year_and_city(self):
        df = ejercicio5.process_files2(self.test_directory, self.invalid_files)
        ejercicio5.plot_cars_by_year_and_city(df)
        #  the function should not raise any exception
