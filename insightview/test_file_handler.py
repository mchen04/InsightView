# test_file_handler.py
# This file contains tests for the FileHandler class.

import unittest
from core.file_handler import FileHandler
import pandas as pd
import os

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()
        self.test_csv_path = 'test_data.csv'
        self.test_excel_path = 'test_data.xlsx'
        self.test_json_path = 'test_data.json'
        self.empty_file_path = 'empty_file.csv'

        # Create test CSV file
        test_data = {'col1': [1, 2], 'col2': [3, 4]}
        df = pd.DataFrame(test_data)
        df.to_csv(self.test_csv_path, index=False)

        # Create test Excel file
        df.to_excel(self.test_excel_path, index=False)

        # Create test JSON file
        df.to_json(self.test_json_path, orient='records')

        # Create empty CSV file
        with open(self.empty_file_path, 'w') as f:
            f.write('')

    def tearDown(self):
        # Remove test files
        for file_path in [self.test_csv_path, self.test_excel_path, self.test_json_path, self.empty_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_load_csv(self):
        data, metadata = self.file_handler.load_file(self.test_csv_path)
        self.assertIsNotNone(data)
        self.assertEqual(metadata['row_count'], 2)
        self.assertEqual(metadata['column_count'], 2)

    def test_load_excel(self):
        data, metadata = self.file_handler.load_file(self.test_excel_path)
        self.assertIsNotNone(data)
        self.assertEqual(metadata['row_count'], 2)
        self.assertEqual(metadata['column_count'], 2)

    def test_load_json(self):
        data, metadata = self.file_handler.load_file(self.test_json_path)
        self.assertIsNotNone(data)
        self.assertEqual(metadata['row_count'], 2)
        self.assertEqual(metadata['column_count'], 2)

    def test_load_empty_file(self):
        data, metadata = self.file_handler.load_file(self.empty_file_path)
        self.assertIsNone(data)
        self.assertIsNone(metadata)

if __name__ == '__main__':
    unittest.main()
