# file_handler.py
# This file contains the implementation for file upload and parsing.

import pandas as pd
import logging

class FileHandler:
    def __init__(self):
        logging.basicConfig(level=logging.ERROR)

    def load_file(self, file_path):
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                data = pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                data = pd.read_json(file_path)
            else:
                raise ValueError("Unsupported file format. Please upload a CSV, Excel, or JSON file.")
            
            if data.empty:
                raise ValueError("The file is empty. Please upload a file with data.")
            
            metadata = {
                'row_count': data.shape[0],
                'column_count': data.shape[1]
            }
            return data, metadata
        
        except Exception as e:
            logging.error(f"Error loading file: {str(e)}")
            return None, None

    def select_and_parse_file(self):
        from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
        import sys

        app = QApplication(sys.argv)
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Select a File", "", "CSV Files (*.csv);;Excel Files (*.xlsx *.xls);;JSON Files (*.json)", options=options)
        if not file_path:
            QMessageBox.critical(None, "File Selection Error", "No file selected.")
            return None, None
        
        return self.load_file(file_path)
